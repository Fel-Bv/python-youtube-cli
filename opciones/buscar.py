#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from consola.animacion import terminar_animacion
from consola.animacion import iniciar_animacion
from consola.colores import Colores
from web.peticiones import hacer_sopa
from opciones.abrir import abrir
from consola import mensajes
from youtube import BUSQUEDA, BUSQUEDA_GOOGLE
from youtube import GOOGLE

colores = Colores()

def mostrar_opciones():
    from consola.mostrar_tutorial import mostrar_opciones

    mostrar_opciones(
        f'{colores.blanco}./youtube.com buscar [OPCIÓN] BUSQUEDA{colores.default}',
        [
            {
                'corto': '-h',
                'opcion': '--help',
                'descripcion': 'Muestra este mensaje y sale.',
            },
            {
                'corto': '-a',
                'opcion': '--abrir',
                'descripcion': 'Abre el primer resultado de la busqueda.',
            },
        ],
        [
            {
                'argumento': 'BUSQUEDA',
                'descripcion': (
                    'La busqueda del video se hará en YouTube o en Google, por lo que te recomiendo\n'
                    '\t\t\t\tescribir un texto de busqueda como lo harías en el buscador de Google.'
                ),
            }
        ]
    )

def buscar(busqueda: str) -> None:
    iniciar_animacion()

    busqueda = busqueda.replace(' ', '+')
    abrir(BUSQUEDA % busqueda)

    terminar_animacion()

def buscar_y_abrir_primer_resultado(busqueda: str, silencioso: bool = False) -> None:
    iniciar_animacion()

    busqueda = BUSQUEDA_GOOGLE % busqueda.replace(' ', '+')
    sopa = hacer_sopa(busqueda)
    links = []

    for elemento in filter(lambda elemento: elemento.get('href').find('youtube.com') != -1, sopa.find_all('a')):
        links.append(GOOGLE + elemento.get('href'))

    if not silencioso:
        mensajes.exito('Se han encontrado resultados.')
        mensajes.log('Resultados obtenidos:')

        for link in links:
            print(
                colores.blanco,
                ' · ',
                colores.default,
                sep='',
                end='',
            )
            print(link.replace(GOOGLE + '/url?q=', ''))

    terminar_animacion()

    if not silencioso: mensajes.info('Abriendo el primer resultado...')

    iniciar_animacion()
    abrir(links[0])
    terminar_animacion()

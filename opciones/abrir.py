#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from consola.animacion import terminar_animacion
from consola.animacion import iniciar_animacion
from consola.colores import Colores
import subprocess

colores = Colores()

def mostrar_modo_de_uso():
    from consola.mostrar_tutorial import mostrar_opciones

    mostrar_opciones(
        f'{colores.blanco}./youtube.com abrir [OPCIONES] VIDEO{colores.default}',
        [
            {
                'corto': '-h',
                'opcion': '--help',
                'descripcion': 'Muestra este mensaje y sale.',
            },
            {
                'corto': '-s',
                'opcion': '--segundo SEGUNDO',
                'descripcion': 'Reproducir el video desde el segundo especificado.',
            }
        ],
        argumentos=[
            {
                'argumento': 'VIDEO',
                'descripcion': (
                    f'ID del video. Ejemplo: {colores.blanco}"OBswlyZ6UUE"{colores.default}.\n'
                    '\t\t\tEste se puede obtener del link del video:\n'
                    '\t\t\t\thttps://www.youtube.com/watch?v=VYr3jRXe26E -> '
                    f'ID: {colores.blanco}"VYr3jRXe26E"{colores.default}.'
                )
            }
        ]
    )

def abrir(URL: str) -> None:
    iniciar_animacion()
    subprocess.run(f'xdg-open {URL}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    terminar_animacion()

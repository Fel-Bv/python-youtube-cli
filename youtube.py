#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from consola.colores import Colores
from consola import mensajes
from sys import argv as args
from sys import exit

YOUTUBE = 'https://www.youtube.com'
GOOGLE = 'https://www.google.com'
BUSQUEDA_GOOGLE = f'{GOOGLE}/search?q=%s&tbm=vid'
BUSQUEDA = f'{YOUTUBE}/results?search_query=%s'
VIDEO = f'https://youtu.be/%s'

colores = Colores()

def main():
    if 'buscar' in args[:2]:
        args_buscar = args[args.index('buscar') + 1:]

        if '-h' in args_buscar or '--help' in args_buscar or len(args_buscar) < 1:
            from opciones.buscar import mostrar_opciones

            mostrar_opciones()
            exit(0)
        if '-a' in args_buscar or '--abrir' in args_buscar:
            from opciones.buscar import buscar_y_abrir_primer_resultado

            if '-a' in args_buscar: del args_buscar[args_buscar.index('-a')]
            else: del args_buscar[args_buscar.index('--abrir')]

            busqueda = ' '.join(args_buscar).strip()
            if not busqueda:
                mensajes.error('Falta un argumento.')

                from opciones.buscar import mostrar_opciones

                mostrar_opciones()
                exit(0)

            buscar_y_abrir_primer_resultado(busqueda, '-s' in args)
            exit(0)

        from opciones.buscar import buscar

        busqueda = ' '.join(args_buscar).strip()
        if not busqueda:
            mensajes.error('Falta un argumento.')

            from opciones.buscar import mostrar_opciones

            mostrar_opciones()
            exit(0)

        buscar(busqueda)
        exit(0)
    elif 'abrir' in args[:2]:
        args_abrir = args[args.index('abrir') + 1:]

        if '-h' in args_abrir or '--help' in args_abrir or len(args_abrir) < 1:
            from opciones.abrir import mostrar_modo_de_uso

            mostrar_modo_de_uso()
            exit(0)

        from opciones.abrir import abrir

        if '-S' in args_abrir or '--segundo' in args_abrir:
            if '-S' in args_abrir: indice = args_abrir.index('-S')
            if '--segundo' in args_abrir: indice = args_abrir.index('--segundo')

            try: segundos = args_abrir[indice + 1]
            except IndexError:
                mensajes.error('No se han especificado los segundos.')

                from opciones.abrir import mostrar_modo_de_uso

                mostrar_modo_de_uso()
                exit(0)


            del args_abrir[indice + 1]
            del args_abrir[indice]

            ID_video = args_abrir[0]
            if not ID_video:
                mensajes.error('Falta un argumento.')

                from opciones.abrir import mostrar_modo_de_uso

                mostrar_modo_de_uso()
                exit(1)

            if not '-s' in args_abrir:
                mensajes.info(f'Abriendo video {ID_video}...')
                mensajes.info(f'El video empezará desde el segundo {segundos}.')

            abrir(VIDEO % ID_video + f'?t={segundos}s')
            exit(0)

        ID_video = args_abrir[0]
        if not ID_video:
            mensajes.error('Falta un argumento.')

            from opciones.buscar import mostrar_opciones

            mostrar_opciones()
            exit(1)

        if not '-s' in args_abrir: mensajes.info(f'Abriendo video {ID_video}...')
        abrir(VIDEO % ID_video)
    else:
        mensajes.log(
            f'{colores["fondo negro"] + colores.blanco}Escrito por: {colores.azul}Felipe Alcantar{colores.blanco}. '
            f'https://github.com/Fel-Bv/.{colores.default}\n'
        )

        from consola.mostrar_tutorial import mostrar_opciones

        mostrar_opciones(
            f'{colores.blanco}./youtube.com OPCIÓN{colores.default}',
            argumentos=[
                {
                    'argumento': 'buscar',
                    'descripcion': 'Buscar un video',
                },
                {
                    'argumento': 'abrir',
                    'descripcion': 'Abrir un video',
                },
            ],
            extra='Escribe una opción seguida de "-h" o "--help" para obtener más información.'
        )
        exit(0)

if __name__ == '__main__':
    try: main()
    except KeyboardInterrupt: print(f'\b\b  \n{colores.verde}Saliendo...')

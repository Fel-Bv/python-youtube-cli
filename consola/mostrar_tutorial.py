#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from consola.colores import Colores

def mostrar_opciones(
        modo_de_uso: str,
        opciones: list = [],
        argumentos: list = [],
        extra: str = '',

    ):
    print(f'Modo de uso: {modo_de_uso}\n')

    if opciones:
        print('OPCIONES:')

        for opcion in opciones:
            print(f'\t{opcion["corto"]}, {opcion["opcion"]}\t-\t{opcion["descripcion"]}')

    if argumentos:
        print('ARGUMENTOS:')

        for argumento in argumentos:
            print(f'\t{argumento["argumento"]}\t-\t{argumento["descripcion"]}')

    if extra: print('\n' + extra)

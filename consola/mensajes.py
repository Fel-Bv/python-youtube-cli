#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from consola.consola import tamaño_terminal
from consola.colores import Colores

colores = Colores()

def log(mensaje: str, final: str = '\n') -> None:
    columnas = tamaño_terminal()
    if len(mensaje) < columnas: mensaje += ' ' * (columnas - len(mensaje))

    print(mensaje, end=final)

def debug(mensaje: str, final: str = '\n') -> None:
    mensaje_ = f'[Debug] {mensaje}'
    columnas = tamaño_terminal()
    espacios = ''
    if len(mensaje_) < columnas: espacios += ' ' * (columnas - len(mensaje_))

    print(f'[{colores.morado}Debug{colores.default}] {mensaje}{espacios}', end=final)

def info(mensaje: str, final: str = '\n') -> None:
    mensaje_ = f'[Info] {mensaje}'
    columnas = tamaño_terminal()
    espacios = ''
    if len(mensaje_) < columnas: espacios += ' ' * (columnas - len(mensaje_))

    print(f'[{colores.azul}Info{colores.default}] {mensaje}{espacios}', end=final)

def advertencia(mensaje: str, final: str = '\n') -> None:
    mensaje_ = f'[Advertencia] {mensaje}'
    columnas = tamaño_terminal()
    espacios = ''
    if len(mensaje_) < columnas: espacios += ' ' * (columnas - len(mensaje_))

    print(f'[{colores.amarillo}Advertencia{colores.default}] {mensaje}{espacios}', end=final)

def error(mensaje: str, final: str = '\n') -> None:
    mensaje_ = f'[Error] {mensaje}'
    columnas = tamaño_terminal()
    espacios = ''
    if len(mensaje_) < columnas: espacios += ' ' * (columnas - len(mensaje_))

    print(f'[{colores.rojo}Error{colores.default}] {mensaje}{espacios}', end=final)

def exito(mensaje: str, final: str = '\n') -> None:
    mensaje_ = f'[Éxito] {mensaje}'
    columnas = tamaño_terminal()
    espacios = ''
    if len(mensaje_) < columnas: espacios += ' ' * (columnas - len(mensaje_))

    print(f'[{colores.verde}Éxito{colores.default}] {mensaje}{espacios}', end=final)

def main() -> None:
    debug('Mensaje.')
    info('Mensaje.')
    advertencia('Mensaje.')
    error('Mensaje.')
    exito('Mensaje.')

if __name__ == '__main__':
    try: main()
    except KeyboardInterrupt: info('Saliendo...')

#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from shutil import get_terminal_size as tamaño
from os import terminal_size
from os import system

def tamaño_terminal(solo_columnas: bool = True) -> terminal_size or int:
    return tamaño().columns if solo_columnas else tamaño()

def limpiar() -> None:
    system('clear || cls')

#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from consola.consola import tamaño_terminal
from consola.colores import Colores
from threading import Thread
from time import sleep

animacion = None
colores = Colores()

class Animacion(Thread):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.terminar = False
		self.setDaemon(True)

	def __call__(self): self.start()

	def run(self, *args, **kwargs):
		while True:
			if self.terminar: break

			columnas = tamaño_terminal()
			for i in range(columnas):
				if self.terminar: break

				columnas = tamaño_terminal()
				texto = colores.verde
				texto += '=' * (3 if i + 3 < columnas else columnas - i)
				print(' ' * i, texto, ' ' * (columnas - i - 3), sep = colores.default, end = '\r')
				sleep(.02)

		columnas = tamaño_terminal()
		print('[', end = colores.verde)
		print('=' * ((columnas - 9) // 2), end = colores.default)
		print(' Listo ', end = colores.verde)
		print('=' * ((columnas - 9) // 2), end = colores.default)
		print(']')

def iniciar_animacion():
    global animacion

    animacion = Animacion()
    animacion()

def terminar_animacion():
    global animacion

    animacion.terminar = 1
    sleep(.3)

def main():
    global animacion

    iniciar_animacion()

    while True: sleep(1)

if __name__ == '__main__':
    try: main()
    except KeyboardInterrupt:
        try: terminar_animacion()
        except: pass

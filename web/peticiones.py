#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re

def quitar_protocolo(link: str) -> str:
    protocolo = re.search('(?P<protocolo>http\w{0,1}://)', link)
    if protocolo: link = link.replace(protocolo.group('protocolo'), '')

    return link

def peticion(
        dominio: str, metodo: str = 'get', cookies: dict = {}, datos: dict = {}, 
        cabeceras: dict = {}, timeout: int = 8
    ) -> requests.models.Response:
    dominio = quitar_protocolo(dominio)

    respuestas = {
        'get': lambda: requests.get(f'https://{dominio}', cookies = cookies, headers = cabeceras, timeout=timeout),
        'post': lambda: requests.post(f'https://{dominio}', cookies = cookies, data = datos, headers = cabeceras, timeout=timeout),
    }
    return respuestas[metodo]()

def hacer_sopa(dominio: str) -> BeautifulSoup:
    response = peticion(dominio)

    return BeautifulSoup(response.content, 'html.parser')

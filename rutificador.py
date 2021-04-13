#!/usr/bin/python

__version__="1.0"

from requests import RequestException
from requests import ConnectionError
import requests, json
import html_to_json
import time
import re
import argparse

### TASKS
# Debemos parsear la info del json para arrojarla de forma bonita
# Ordenar en clases las funciones
# Peticion del registro civil y gmail temp
# Crear el script de pdf

def rutificador_nombre(search):

    URL = 'https://www.nombrerutyfirma.com/buscar'
    params = {'term': search}

    peticion = requests.post(URL, data = params)

    if peticion.status_code == 200:
        x = peticion.text
        json_ = html_to_json.convert_tables(x)
        print(json_)

def rutificador_rut(rut):
    
    regex = "^\d{1,2}\.\d{3}\.\d{3}[-][0-9kK]{1}$"
    URL = 'https://www.nombrerutyfirma.com/rut'
    params = {'term': rut}
    
    x = re.search(regex, rut)
    
    if(x != None):
        peticion = requests.post(URL, data = params)
        if peticion.status_code == 200:
            x = peticion.text

            json_ = html_to_json.convert_tables(x)

            print(json_)

    else:
        print("Formato invalido. Escribe el rut correctamente (XX.XXX.XXX-X)")

def main(objetivo):
    if type(objetivo) == str:
        regex = "^\d{1,2}\.\d{3}\.\d{3}[-][0-9kK]{1}$"
        x = re.search(regex, objetivo)
        if(x != None):
            rutificador_rut(objetivo)
        else:
            rutificador_nombre(objetivo)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog='rutificador-chile.py',epilog="Version: 1.0 | Autor: Aaron Silva | Github: https://github.com/xsilvamo")
    parser.add_argument("--target", help="Target name/rut for search in the database.")
    args = parser.parse_args()

    objetivo = input("Ingresa el Nombre o Rut: ")

    try:
        main(objetivo)

    except Exception as e:
        print("[X] ERROR: ", e)
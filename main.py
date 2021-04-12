#!/usr/bin/python

import requests, json
import html_to_json

search = input("Escribe aqui a quien buscas: ")
URL = 'https://www.nombrerutyfirma.com/buscar'
params = {'term': search}

peticion = requests.post(URL, data = params)

x = peticion.text

json_ = html_to_json.convert_tables(x)

print(json_)

# PYTHON PACKAGE MANAGER

# PIP

import numpy
import pandas
import xlrd

arreglo = numpy.array([35,24,62,52,30,30,17])
print(arreglo)
print(type(arreglo))

import requests

responde = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(responde)
print(responde.status_code)
# print(responde.json())

from mypackage import arithmetics

print(arithmetics.suma_value(5,5))
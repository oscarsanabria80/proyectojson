from ctypes.wintypes import 
from http import client
import json
from funciones import *
#leer json
with open("tiendadeproducto.json") as fichero:
    doc=json.load(fichero)

#listar produductos
print(listar_productos(doc))

#introducir el nombre de un cliente y contar los productos comprado.
nombre=input("introduce un nombre de clientes: ")
for calcular in clientes_productos(nombre,doc):
    print(calcular)

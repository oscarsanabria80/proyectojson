import json 
from funciones import *
#leer json
with open("tiendadeproducto.json") as fichero:
    doc=json.load(fichero)

#1.Listas todos los productos que contenga la tienda
print(listar_productos(doc))

#2.introducir el nombre de un cliente y contar los productos comprado.
for calcular in clientes_productos(doc):
 print(calcular)

#3.Mostrar el producto que contenga el precio que se ha introducido por teclado.
print(precio_productos(doc))


#4.Pedir por teclado el nombre de un cliente y un dia (day1,day2,day3) y que muestres el color del producto comprado ese día.
for calcularr in buscar_productos(doc):
    print(calcularr)
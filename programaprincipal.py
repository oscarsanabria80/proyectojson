import json
from funciones import *

#leer json
with open("tiendadeproducto.json") as fichero:
    doc=json.load(fichero)

print(''' 
1.Listas todos los productos que contenga la tienda
2.introducir el nombre de un cliente y contar los productos comprado. 
3.Mostrar el producto que contenga el precio que se ha introducido por teclado.
4.Pedir por teclado el nombre de un cliente y un dia (day1,day2,day3) y que muestres el color del producto comprado ese día.
5.Mostrar el nombre del producto y sus ventas, con el precio más alto del que indiquemos.
6.Salir''')

print("\n\n")


menu=int(input("Introduce una de las opciones que se le indica:  "))

print("\n\n")
while menu !=6:

#1.Listas todos los productos que contenga la tienda
    if menu==1:
        print(listar_productos(doc))

#2.introducir el nombre de un cliente y contar los productos comprado.
    if menu==2:
        for calcular in clientes_productos(doc):
            print(calcular)

#3.Mostrar el producto que contenga el precio que se ha introducido por teclado.
    if menu==3:
        print(precio_productos(doc))


#4.Pedir por teclado el nombre de un cliente y un dia (day1,day2,day3) y que muestres el color del producto comprado ese día.
    if menu==4:
        for calcularr in buscar_productos(doc):
                print("\n\n")
                print("Color del producto es:  ",calcularr)
                print("\n\n")

#5. Mostrar el nombre del producto y sus ventas, con el precio más alto del que indiquemos.
    if menu==5:
        for hola in producto_precio(doc):
            print(doc["name"])

    menu=int(input("Introduce una de las opciones que se le indica:  "))
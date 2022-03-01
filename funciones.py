import json


# 1.Listas todos los productos que contenga la tienda
def listar_productos(tienda):
    lista=[]
    contar= tienda.get("products")
    for i in contar:
        if i.get("name"):
            lista.append(i.get("name"))
    return lista

#2.introducir el nombre de un cliente y contar los productos comprado.
def clientes_productos(nombre,doc):
    lista1=[]
    for cliente in doc["users"]:
        if cliente["name"]==nombre:
            lista1.append(cliente.get("name"))
            lista1.append(cliente.get("purchase"))
        if not cliente["name"]==nombre:
            print("CLIENTE NO REGISTRADO EN LA BASE DE DATO.")
    return lista1
        
#3.Mostrar el producto que contenga el precio que se ha introducido por teclado.

def precio_productos(precio):
    lista=[]
    pre= float(input("Intoduce un precio:  "))
    productos=precio.get("products")
    for p in productos:
        if p["price"]== pre:
            lista.append(p.get("name"))
    return lista


#4.Pedir por teclado el nombre de un cliente y un dia (day1,day2,day3) y que muestres el color del producto comprado ese día.

def buscar_productos(dia,nombre,doc):
    lista=[]
    nombre=input("Introduce el nombre:  ")
    dia=input("Un dia:  ")
    docc= doc.get("users")
    for i in docc:
        if i["name"]== nombre:
    return lista
#5. Mostrar el nombre del producto y sus ventas, con el precio más alto del que indiquemos.

def precio_alto(precio,doc):
    lista=[]
    lista3=[]
    precio=float(input("Precio estimado: "))
    do= doc.get("products")
    for c in do:
        if c["price"] < precio:
            #lista.append(c.get("name"))
            lista3.append(c.get("sold"))

    return lista3


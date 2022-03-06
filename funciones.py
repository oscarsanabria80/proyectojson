import json


# 1.1.Listar todos los productos que contenga la tienda.
def listar_productos(tienda):
    for i in tienda["products"]:
        if i.get("name"):
            print(i["name"])
    return print(i["name"])

#2.introducir el nombre de un cliente (Admin...) y contar los productos comprado.
def clientes_productos(doc):
    lista1=[]
    nombre=input("introduce un nombre:  ")
    for cliente in doc["users"]:
        if cliente["name"]==nombre:
            lista1.append(len(cliente.get("purchase")))

    return lista1
        
#3.Mostrar el producto que contenga el precio ("13.5", "16.3", "190", "353.53", "9.5"...) que se ha introducido por teclado.

def precio_productos(precio):
    pre= float(input("Intoduce un precio:  "))
    productos=precio.get("products")
    for p in productos:
        if p["price"]== pre:
            print(p.get("name"))
    return print(p.get("name"))

#4.Pedir por teclado el nombre de un cliente y un dia (dia1,dia2,dia3,dia4,dia5,dia6....) y que muestres el color del producto comprado ese día.

def buscar_productos(tienda):
    listaproductos=[]
    nombre=input("Introduce el nombre:  ")
    dia=input("Un dia:  ")
    for e in tienda["users"]:
        if e["name"]==nombre:
            compra=e["purchase"]
            for dias in compra:
                arti=dias["day"]
                for d in arti:
                    if d["dia"]==dia:
                        listaproductos.append(d["color"])
    return listaproductos

#5. Mostrar el nombre del producto y sus ventas, con el precio ("13.5", "16.3", "190", "353.5.3", "9.5"...) más alto del que indiquemos.

def producto_precio(tiend):
    lista3=[]
    precio=float(input("Precio estimado:  "))
    for p in tiend["products"]:
        if p["price"]>precio:
            lista3.append(p["name"])
            lista3.append(p["sold"])
    return lista3

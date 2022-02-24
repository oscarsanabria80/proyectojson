import json


# .Listas todos los productos que contenga la tienda
def listar_productos(tienda):
    lista=[]
    contar= tienda.get("products")
    for i in contar:
        if i.get("name"):
            lista.append(i.get("name"))
    return lista

#introducir el nombre de un cliente y contar los productos comprado.
def clientes_productos(nombre,doc):
    lista1=[]
    for cliente in doc["users"]:
        if cliente["name"]==nombre:
            lista1.append(cliente.get("name"))
            lista1.append(cliente.get("purchase"))
        if not cliente["name"]==nombre:
            print("CLIENTE NO REGISTRADO EN LA BASE DE DATO.")
    return lista1
        
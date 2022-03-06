import json
from funciones import *

#leer json
with open("tiendadeproducto.json") as fichero:
    doc=json.load(fichero)
print("----------------------------------------------------------------------------------------------------------------------")
print(''' 
1.Listar todos los productos que contenga la tienda.
2.introducir el nombre de un cliente (Admin) y contar los productos comprado. 
3.Mostrar el producto que contenga el precio ("13.5", "16.3", "190", "353.5.3", "9.5") que se ha introducido por teclado.
4.Pedir por teclado el nombre de un cliente y un dia (dia1,dia2,dia3,dia4,dia5,dia6....) y que muestres el color del producto comprado ese día.
5.Mostrar el nombre del producto y sus ventas, con el precio ("13.5", "16.3", "190", "353.5.3", "9.5") más alto del que indiquemos.
6.Salir''')
print("----------------------------------------------------------------------------------------------------------------------")
print("\n\n")


menu=int(input("Introduce una de las opciones que se le indica:  "))

print("\n\n")
while menu !=6:

#1.Listas todos los productos que contenga la tienda
    if menu==1:
        print("***************************************************") 
        print("*                                                 *")
        print("*         PRODUCTOS QUE CONTIENEN LA LISTA        *")
        print("*                                                 *")
        print("***************************************************")
        print("\n\n")
        print(listar_productos(doc))

#2.introducir el nombre de un cliente y contar los productos comprado.
    if menu==2:
        for calcular in clientes_productos(doc):
            print("****************************************") 
            print("*                                      *")
            print("*          COMPRAS DEL USUARIO         *")
            print("*                                      *")
            print("****************************************")
            print("\n\n")
            print(calcular,"Productos")

#3.Mostrar el producto que contenga el precio que se ha introducido por teclado.
    if menu==3:
        print("***************************************************") 
        print("*                                                 *")
        print("*    LOS PRODUCTOS CON EL PRECIO INDICADOS SON    *")
        print("*                                                 *")
        print("***************************************************")
        print(precio_productos(doc))


#4.Pedir por teclado el nombre de un cliente y un dia (day1,day2,day3) y que muestres el color del producto comprado ese día.
    if menu==4:
        for calcularr in buscar_productos(doc):
                print("****************************************") 
                print("*                                      *")
                print("*          COLOR DEL PRODUCTO          *")
                print("*                                      *")
                print("****************************************") 
                print("-",calcularr)

#5. Mostrar el nombre del producto y sus ventas, con el precio más alto del que indiquemos.
    if menu==5:
        print("****************************************") 
        print("*                                      *")
        print("*        PRODUCTOS Y SUS VENTAS        *")
        print("*                                      *")
        print("****************************************")  
        for hola in producto_precio(doc):
            print(hola)
            
    
    print("\n\n")
    menu=int(input("Introduce una de las opciones que se le indica:  "))
#Programa para gestion de productos
#En una lista de mercado
nombreUsuario=None

#Declarando las variables
productos=[]
producto={}

#crear un menu de opciones
print("*** MerqueoAPP ***")
print("1. Agregar Producto a tu lista de mercado")
print("2. Mostrar tu lista de mercado")
print("3. Modificar tu lista de mercado")
print("4. Retirar producto de tu lista de mercado")
print(" Presiona 5 para SALIR")

opcion=100
while opcion != 5:
    opcion=int(input("Digita una opcion del menu: "))

    if opcion == 1:
        #print("Creando la lista")
        #Poblando listas y diccionarios en python 

        #Asignando claves a un diccionario
        producto["id"]=5 #generar de forma alatoria este numero (unico)
        producto["nombre"]=input("Digita el nombre del producto: ")
        producto["presentacion"]=input(" Digita la presentacion del producto: ")
        producto["cantidad"]=int(input("Digita la cantidad: "))
        producto["precio"]=int(input("Digita el precio del producto: "))

        #Asignando a una lista un diccionario
        productos.append(producto)
        #print(productos)


    elif opcion == 2:
        #recorrer una lista``
        for productoIterado in productos:
            print(productoIterado["nombre"])
            print(productoIterado["precio"])
    elif opcion == 3:
        #preguntarle al usuario cual producto quiere cambiar 
        idProductoABuscar=int(input("cual es el id del producto a modificar "))
        #recorrer la lista para buscar o identificar 
        for productobuscado in productos:
            if idProductoABuscar ==productobuscado["id"]:#trae el primer id y compararlo con idProductoABuscar.
                print("encontrado")
            else:
                print("no encontrado")   

                 

        #acondicionar este pedazo   
        #modificar la o las propiedades pedidas

    elif opcion == 4:
        print("Retirando un producto")
    else:
        print("Opcion invalida")

    #como cuando genero un numero que sea unico.
    #cuando agrego cosas en una lista esas cosas no se sobreescriban.
    #recorre, lista diccionario, 
    
    

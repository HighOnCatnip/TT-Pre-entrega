lista_prod=[]
while True:
    print("***********************************")
    print("\t\tMENU")
    print("***********************************")
    print("""
        1. Agregar producto
        2. Mostrar productos
        3. Buscar producto
        4. Eliminar producto
        5. Salir
          """)
    opcion=int(input("Ingrese una opcion: "))
    match opcion:
        case 1:
            while True:
                nombre=input("Ingrese el nombre del producto: ").strip()
                if nombre== "":
                    continue
                else:
                    break
            while True:
                categoria=input("Ingrese la categoria del producto: ").strip()
                if categoria== "":
                    continue
                else:
                    break
            while True:
                precio=input("Ingrese el precio del producto: ").strip()
                if precio.isdigit()==True:
                    precio=int(precio)
                    break     
                else:
                    continue
            producto=[nombre,categoria,precio]
            lista_prod.append(producto)
            
        case 2:
            for indice in range(len(lista_prod)):
                print(f"\t{indice+1}.{lista_prod[indice][0]} - {lista_prod[indice][1]} - {lista_prod[indice][2]}") 
        case 3:
            lista_buscada=[]
            while True:
                resultado=input("Ingrese el nombre del producto buscado: ").strip()
                if resultado=="":
                    continue
                else:
                    break
            for producto in lista_prod:
                if resultado in producto[0]:
                    lista_buscada.append(producto)
            if len(lista_buscada)>0:
                for i in lista_buscada:
                  print(f"{i[0]} - {i[1]} - {i[2]}")
        case 4:
            while True:
                prodAborrar=input("Ingrese el numero de producto a borrar: ")
                if prodAborrar.isdigit():
                    prodAborrar=int(prodAborrar)
                    if prodAborrar > len(lista_prod):
                        print("Producto no encontrado en al lista") 
                    elif prodAborrar>0:
                        lista_prod.pop(prodAborrar-1)
                        break
                else:
                    continue
        case 5:
            print("Saliendo del programa...")
            break     
        case _:
            print("La opcion ingresada no es valida")

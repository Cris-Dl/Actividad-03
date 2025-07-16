print(f"Bienvenido al restaurante")
option = 0
while option != 3:
    print(f"1- Ordenar")
    print(f"2- Ver pedido")
    print(f"3- Salir")

    option = int(input(f"Ingrese el numero de la acción que desea hacer: "))

    if option == 1:
        print("Ordenar")
        order = 0
        while order != 4:
            print("1.- Hamburguesa")
            print("2.- Pizza")
            print("3.- Taco")
            print("4.- Volver")
            order = int(input("Ingrese el número de la opción que desea ordenar:"))
    elif option == 2:
        print("Ver pedido")

    elif option == 3:
        print("Ha salido del programa, gracias por visitarnos")

    else:
        print("Ingreso mal un digito, vuelve a intentarlo \n")

from ipykernel.eventloops import loop_qt

print(f"Bienvenido al restaurante")
option = True
lista = []
while option:
    print(f"1- Ordenar")
    print(f"2- Ver pedido")
    print(f"3- Salir")

    option2 = int(input(f"Ingrese el numero de la acción que desea hacer: "))
    print("")
    if option2 == 1:
        print("Ordenar")
        order = True
        while order:
            print("1.- Hamburguesa")
            print("2.- Pizza")
            print("3.- Taco")
            print("4.- Volver")
            order2 = int(input("Ingrese el número de la opción que desea ordenar:"))
            print("")
            if order2 == 1:
                hm = True
                while hm:
                    print("Hamburguesa")
                    print("1.- Quesoburguesa")
                    print("2.- Cuarto de Libra")
                    print("3.- The Classic")
                    burger = int(input("Ingrese la opción de la hamburguesa que desea ordenar:"))
                    print("")
                    if burger == 1:
                        print("Ha seleccionado una quesoburguesa")
                        burger = "Quesoburguesa"
                        lista.append(burger)
                        more = int(input("Ingrese 1 si quieres agregar otra hamburguesa o 2 para regresar al menu:"))
                        print("")
                        if more == 1:
                            print("Volviendo a las opciones de hamburguesas...")
                            print("")
                        elif more == 2:
                            break
                        else:
                            print("Valor invalido, vuelva a intentar. Se ha guardado el pedido")
                            break
                    elif burger == 2:
                        print("Ha seleccionado un cuarto de libra")
                        burger = "Cuarto de Libra"
                        lista.append(burger)
                        more = int(input("Ingrese 1 si quieres agregar otra hamburguesa o 2 para regresar al menu:"))
                        print("")
                        if more == 1:
                            print("Volviendo a las opciones de hamburguesas...")
                            print("")
                        elif more == 2:
                            break
                        else:
                            print("Valor invalido, vuelva a intentar. Se ha guardado el pedido")
                            break
                    elif burger == 3:
                        print("Ha seleccionado the classic")
                        burger = "The Classic"
                        lista.append(burger)
                        more = int(input("Ingrese 1 si quieres agregar otra hamburguesa o 2 para regresar al menu:"))
                        print("")
                        if more == 1:
                            print("Volviendo a las opciones de hamburguesas...")
                            print("")
                        elif more == 2:
                            break
                        else:
                            print("Valor invalido, vuelva a intentar. Se ha guardado el pedido")
                            break
                    else:
                        print("Valor invalido, vuelva a intentar")
                        more = int(input("Ingrese 1 si quieres agregar alguna hamburguesa o 2 para regresar al menu:"))
                        print("")
                        if more == 1:
                            print("Volviendo a las opciones de hamburguesas...")
                            print("")
                        elif more == 2:
                            break
            if order2 == 2:
                pm = True
                while pm:
                    print("Pizza")
                    print("1.- Pizza de peperoni")
                    print("2.- Pizza de queso")
                    print("3.- Pizza deluxe")
                    pizza1 = int(input("Ingrese la opción de la pizza que desea ordenar:"))
                    print("")
                    if pizza1 == 1:
                        print("Ha seleccionado una pizza de peperoni")
                        pizza1 = "Pizza de peperoni"
                        lista.append(pizza1)
                        more = int(input("Ingrese 1 si quieres agregar otra pizza o 2 para regresar al menu:"))
                        print("")
                        if more == 1:
                            print("Volviendo a las opciones de pizzas...")
                            print("")
                        elif more == 2:
                            break
                        else:
                            print("Valor invalido, vuelva a intentar. Se ha guardado el pedido")
                            break
                    elif pizza1 == 2:
                        print("Ha seleccionado una pizza de queso")
                        pizza1 = "Pizza de Queso"
                        lista.append(pizza1)
                        more = int(input("Ingrese 1 si quieres agregar otra pizza o 2 para regresar al menu:"))
                        print("")
                        if more == 1:
                            print("Volviendo a las opciones de pizzas...")
                            print("")
                        elif more == 2:
                            break
                        else:
                            print("Valor invalido, vuelva a intentar. Se ha guardado el pedido")
                            break
                    elif pizza1 == 3:
                        print("Ha seleccionado la pizza deluxe")
                        pizza1 = "Pizza Deluxe"
                        lista.append(pizza1)
                        more = int(input("Ingrese 1 si quieres agregar otra pizza o 2 para regresar al menu:"))
                        print("")
                        if more == 1:
                            print("Volviendo a las opciones de pizzas...")
                            print("")
                        elif more == 2:
                            break
                        else:
                            print("Valor invalido, vuelva a intentar. Se ha guardado el pedido")
                            break
                    else:
                        print("Valor invalido, vuelva a intentar")
                        more = int(input("Ingrese 1 si quieres agregar alguna pizza o 2 para regresar al menu:"))
                        print("")
                        if more == 1:
                            print("Volviendo a las opciones de pizzas...")
                            print("")
                        elif more == 2:
                            break
    elif option == 2:
        print("Ver pedido")
        print()
    elif option == 3:
        print("Ha salido del programa, gracias por visitarnos")

    else:
        print("Ingreso mal un digito, vuelve a intentarlo \n")

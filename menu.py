print(f"Bienvenido al restaurante")
option = True
foodList = []
while option:
    print(f"1- Ordenar")
    print(f"2- Ver pedido")
    print(f"3- Cancelar pedido")
    print(f"4- Confirmación de pedido")

    option2 = int(input(f"Ingrese el numero de la acción que desea hacer: "))
    print("")
    if option2 == 1:
        print("Ordenar")
        order = True
        while order:
            print("1.- Hamburguesa")
            print("2.- Pizza")
            print("3.- Taco")
            print("4.- Volver al inicio")
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
                        burger = "quesoburguesa"
                        foodList.append(burger)
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
                        burger = "cuarto de libra"
                        foodList.append(burger)
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
                        burger = "the classic"
                        foodList.append(burger)
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
                    pizza1 = int(input("Ingrese la opción de la pizza que desea ordenar: "))
                    print("")
                    if pizza1 == 1:
                        print("Ha seleccionado una pizza de peperoni")
                        pizza1 = "pizza de peperoni"
                        foodList.append(pizza1)
                        more = int(input("Ingrese 1 si quieres agregar otra pizza o 2 para regresar al menu: "))
                        print("")
                        if more == 1:
                            print("Volviendo a las opciones de pizzas... \n")
                        elif more == 2:
                            break
                        else:
                            print("Valor invalido, vuelva a intentar. Se ha guardado el pedido")
                            break
                    elif pizza1 == 2:
                        print("Ha seleccionado una pizza de queso")
                        pizza1 = "pizza de queso"
                        foodList.append(pizza1)
                        more = int(input("Ingrese 1 si quieres agregar otra pizza o 2 para regresar al menu: "))
                        print("")
                        if more == 1:
                            print("Volviendo a las opciones de pizzas... \n")
                        elif more == 2:
                            break
                        else:
                            print("Valor invalido, vuelva a intentar. Se ha guardado el pedido")
                            break
                    elif pizza1 == 3:
                        print("Ha seleccionado la pizza deluxe")
                        pizza1 = "pizza deluxe"
                        foodList.append(pizza1)
                        more = int(input("Ingrese 1 si quieres agregar otra pizza o 2 para regresar al menu: "))
                        print("")
                        if more == 1:
                            print("Volviendo a las opciones de pizzas...\n")
                        elif more == 2:
                            break
                        else:
                            print("Valor invalido, vuelva a intentar. Se ha guardado el pedido")
                            break
                    else:
                        print("Valor invalido, vuelva a intentar")
                        more = int(input("Ingrese 1 si quieres agregar alguna pizza o 2 para regresar al menu: "))
                        print("")
                        if more == 1:
                            print("Volviendo a las opciones de pizzas...\n")
                        elif more == 2:
                            break
            elif order2 == 3:
                tm = True
                while tm:
                    print("Taco")
                    print("1.- Tacos de birria")
                    print("2.- Tacos al pastor")
                    print("3.- Tacos de cochinita pibil")
                    tacos1 = int(input(f"Ingrese la opción de taco que desea ordenar: "))
                    print("")
                    if tacos1 == 1:
                        print("Ha seleccionado tacos de birria")
                        tacos1 = "tacos de birria"
                        foodList.append(tacos1)
                        more = int(input("Ingrese 1 si quieres agregar otros tacos o 2 para regresar al menu: "))
                        print("")
                        if more == 1:
                            print("Volviendo a las opciones de tacos... \n")
                        elif more == 2:
                            break
                        else:
                            print("Valor invalido, vuelva a intentar. Se ha guardado el pedido")
                            break
                    elif tacos1 == 2:
                        print("Ha seleccionado tacos al pastor")
                        tacos1 = "tacos al pastor"
                        foodList.append(tacos1)
                        more = int(input("Ingrese 1 si quieres agregar otros tacos o 2 para regresar al menu: "))
                        print("")
                        if more == 1:
                            print("Volviendo a las opciones de tacos...\n")
                        elif more == 2:
                            break
                        else:
                            print("Valor invalido, vuelva a intentar. Se ha guardado el pedido")
                            break
                    elif tacos1 == 3:
                        print("Ha seleccionado tacos de cochinita pibil")
                        tacos1 = "tacos de cochinita pibil"
                        foodList.append(tacos1)
                        more = int(input("Ingrese 1 si quieres agregar otros tacos o 2 para regresar al menu: "))
                        print("")
                        if more == 1:
                            print("Volviendo a las opciones de tacos... \n")
                        elif more == 2:
                            break
                        else:
                            print("Valor invalido, vuelva a intentar. Se ha guardado el pedido")
                            break
                    else:
                        print("Valor invalido, vuelva a intentar")
                        more = int(input("Ingrese 1 si quieres agregar alguna porción de tacos o 2 para regresar al menu: "))
                        print("")
                        if more == 1:
                            print("Volviendo a las opciones de tacos...")
                        elif more == 2:
                            break
            elif order2 == 4:
                print("Volviendo al inicio...")
                break

    elif option2 == 2:
        print("Ver pedido")
        print(f"Este es tu pedido: {foodList} \n")

    elif option2 == 3:
        print(f"Cancelar pedido")
        print(f"Lista de pedido: {foodList}")
        food = input("¿Qué producto deseas eliminar? ").lower()

        if food in foodList:
            foodList.remove(food)
            print(f"\n{food} eliminado del pedido.\n")
        else:
            print(f"\n{food} no está en el pedido.\n")


    elif option2 == 4:
        print("Se ha confirmado tu pedido, gracias por tu preferencia")
        break

    else:
        print("Ingreso mal un digito, vuelve a intentarlo \n")
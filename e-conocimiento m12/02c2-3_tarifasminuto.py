tarifa_eeuu = 900   # punto 2 tarifas para cada región
tarifa_canada = 800
tarifa_europa = 950
tarifa_resto_mundo = 1250
umbral_descuento = 15   # duración para aplicar 20% menos


def op_costo(cobromin, duracion):
    costo_total = cobromin * duracion
    if duracion >= umbral_descuento:
        costo_total *= 0.8  # Aplicar 20% desc si dura mayor al umbral
    return costo_total


while True:   # menú regiones
    print("punto 2c \nSeleccione la región de la llamada:")
    print("1. Estados Unidos")
    print("2. Canadá")
    print("3. Europa")
    print("4. Resto del mundo")
    print("5. Salir")
    opcion = input("pon el número del menu región (1-5): ")

    if opcion == '5':
        print("Saliendo del programa.")
        break
    elif opcion in ['1', '2', '3', '4']:  # input duracion para determinar si desc
        duracion = int(input("pon la duración, 20% off si es mas de 15 : "))
        if opcion == '1':   # condional de cada region
            tarifa = tarifa_eeuu
        elif opcion == '2':
            tarifa = tarifa_canada
        elif opcion == '3':
            tarifa = tarifa_europa
        else:
            tarifa = tarifa_resto_mundo
        costo_total = op_costo(tarifa, duracion)   # costo total punto 3
        print("\n El costo total de la llamada es: $", costo_total)
        print("             \t tarifa original a: $", tarifa)
    else:
        print("Opción no válida, pon una opción del 1 al 5.")

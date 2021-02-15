print("CALCULADORA DE ÁREAS, CIRCULO, TRIANGULO Y CUADRILÁTEROS")
a = input("De qué figura quiere calcular el área?\n")
if a == "circunferencia":
    r = float(input("Introduzca el radio de la circunferencia:\n"))
    print(f"El área de la circunferencia es: {3.141592 * pow(r, 2)} unidades cuadradas")
elif a == "cuadrilátero":
    base = float(input("Introduzca la base del cuadrilátero:\n"))
    altura = float(input("Introduzca la altura del cuadrilátero:\n"))
    print(f"El área de su cuadrilátero es: {base * altura} unidades cuadradas")
else:
    if a == "triangulo":
        base = float(input("Introduzca la base del triangulo:\n"))
        altura = float(input("Introduzca la altura del triangulo:\n"))
        print(f"El área de su triangulo es: {base * altura / 2} unidades cuadradas")
    else:
        print("Este programa no puede calcular el área de esta figura")

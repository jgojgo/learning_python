print("¿Es año bisiesto?")
a = int(input("Introduzca el año que le gustaría comprobar si es bisiesto o no\n"))
if a <= 0:
    print("Los años no pueden ser ni 0 ni negativos")
else:
    if a % 4 == 0 and a % 100 != 0:
        print(f"{a} es un año bisiesto")
    elif a % 100 == 0 and a % 400 == 0:
        print(f"{a} es un año bisiesto")
    else:
        print(f"{a} no es un año bisiesto")

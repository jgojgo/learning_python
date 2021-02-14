print("COMPARADOR DE MÚLTIPLOS")
a=float(input("Introduzca el primer número\n"))
b=float(input("Introduzca el segundo número\n"))
if a==0 or b==0:
    print("Lo siento, este programa no admite el 0")
elif a<0 or b<0:
    print("Lo siento, este programa no admite valores negativos")
else:
    if a>b:
        if a%b==0:
            print(f"{a} es múltiplo de {b}")
        else:
            print(f"{a} no es múltiplo de {b}")
    elif a<b:
        if b%a==0:
            print(f"{b} es múltiplo de {a}")
        else:
            print(f"{b} no es múltiplo de {a}")
    else:
        print(f"Ambos números son iguales")

print("COMPARADOR DE TRES NÚMEROS")
a = float(input("Introduzca el primer número\n"))
b = float(input("Introduzca el segundo número\n"))
c = float(input("Introduzca el tercer número\n"))
if a == b == c:
    print(f"Usted ha introducido tres veces el número {a}")
elif a != b and b != c and c != a:
    print(f"Todos los números que ha introducido son diferentes,")
    print(f"el primero es {a}, el segundo es {b} y el tercero es {c}")
else:
    if a == b:
        print(f"Usted ha introducido dos veces el número {a}")
    elif b == c:
        print(f"Usted ha introducido dos veces el número {b}")
    if a == c:
        print(f"Usted ha introducido dos veces el número {a}")

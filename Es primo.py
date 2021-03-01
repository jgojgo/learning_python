from math import *
print("Es primo?\n")
a = int(input("Introduce el número entero que deseas verificar:\n"))
c = 2
while a <= 0:
    a = int(input("Introduzca un número entero POSITIVO mayor que 0"))
if a == 1 or a == 2:
    print(f"El número {a} es primo")
else:
    b = float
    b = sqrt(a)
    while c <= b:
        d = a % c
        if d == 0:
            c = c + b
        else:
            c = c + 1
    if d == 0:
        print(f"El número {a} no es primo:")
    else:
        print(f"El número {a} es primo")
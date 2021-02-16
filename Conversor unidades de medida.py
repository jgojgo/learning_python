print("CONVERSOR DE CENTÍMETROS A KILOMETROS, METROS Y CENTÍMETROS")
a = float(input("Introduzca una distancia en centímetros:\n"))
if a <= 0:
    print("Este programa no admite valores negativos o nulos.")
else:
    if a >= 100000:
        print(f"{a} centímetros son {a // 100000}km, {(a % 100000) // 100}m y {((a % 1000) % 100)}cm")
    elif 100 <= a < 100000:
        print(f"{a} centímetros son {a // 100}m y {a % 100}cm")
    else:
        print(f"Es lo mismo, {a} centímetros son {a}cm")

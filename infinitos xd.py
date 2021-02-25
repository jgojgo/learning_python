print("NÚMEROS CADA VEZ MÁS GRANDES")
a = float(input("Introduzca un número:\n"))
b = float(input(f"Introduzca un número mayor que {a}:\n"))
while b <= a:
    b = float(input(f"Le he dicho mayor que {a}:\n"))
while b > a:
    a = b
    b = float(input(f"Introduzca un número mayor que {a}:\n"))
    while b <= a:
        b = float(input(f"Le he dicho mayor que {a}:\n"))

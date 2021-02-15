print("CM a KM, M y CM")
d = float(input("Introduzca una distancia en centímetros:\n"))
if d >= 100000:
    print(f"{d} centímetros son: {d / 100000}KM, {d / 100}M, {d}CM.")
elif 100 <= d < 100000:
    print(f"{d} centímetros son: 0KM, {d / 100}M, {d}CM.")
else:
    if 0 < d <100:
        print(f"{d} centímetros son: 0KM, 0M, {d}CM.")
    else:
        print("Este programa no acepta ni valores nulos ni valores negativos")

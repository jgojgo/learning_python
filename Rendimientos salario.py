print("SALARIO SEGÚN RENDIMIENTO")
p = float(input("Introduce la puntuación del trabajador:\n"))
if p == 0 or p == 0.4 or p >= 0.6:
    if p == 0:
        print(f"Trabajador nefasto, inaceptable!\nQueda despedido, su salario será de {0 * 2400}€")
    elif p == 0.4:
        print(f"Trabajador normal, aceptable.\nEste trabajador cobrará {0.4 * 2400}€")
    else:
        print(f"Trabajador genial, meritorio!\nEl empleado cobrará un salario de {p * 2400}€")
else:
    print("Introduzca un nivel de trabajo equivalente a 0, 0.4, 0.6 o superior")
print("SUMA TODOS LOS NÚMEROS QUE INTRODUZCAS\nINSTRUCCIONES:\nEscriba todos los números que desea sumar diferentes"
      " a 0, una vez hecho eso, introduzca un 0 para realizar la suma\n\n")
a = 0
b = float(input("Introduce un número que no sea 0:\n"))
while b == 0:
    b = float(input("Introduce un número que no sea 0:\n"))
while b != 0:
    a = a + b
    b = float(input("Introduce el siguiente número:\n"))
print(f"El resultado es {a}")
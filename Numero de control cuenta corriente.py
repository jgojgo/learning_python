print("NÚMRO DE CONTROL DE LA CUENTA:")
e1 = int(input("\nIntroduzca el CÓDIGO DE SU ENTIDAD:\n\nIntroduzca el primer número:"))
e2 = int(input("Introduzca el segundo número:"))
e3 = int(input("Introduzca el tercer número:"))
e4 = int(input("Introduzca el cuarto número:"))

n1 = int(input("\nIntroduzca el NÚMERO DE SU OFICINA:\nIntroduzca el primer número:"))
n2 = int(input("Introduzca el segundo número:"))
n3 = int(input("Introduzca el tercer número:"))
n4 = int(input("Introduzca el cuarto número:"))


if 0 < e1 < 10  and 0 < e2 < 10 and 0 < e3 < 10 and 0 < e4 < 10 and 0 < n1 < 10 and 0 < n2 < 10 and 0 < n3 < 10 and 0 < n4 < 10:
    c = (e1 * 4 + e2 * 8 + e3 * 5 + e4 * 10 + n1 * 9 + n2 * 7 + n3 * 3 + n4 * 6) % 11
    print(f"\nSu número de control es {c}")

else:
    print("Los números deben ser positivos de una sola cifra")

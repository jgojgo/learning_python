print("RESOLVEDOR DE ECUACIONES DE LA FORMA AX+B=0")
a = float(input("Introduzca el valor de A\n"))
b = float(input("Introduzca el valor de B\n"))
if a == 0 and b == 0:
    print("X=R")
elif a == 0:
    print("La ecuación no tiene solución real")
else:
    print(f"{-b/a}=X")

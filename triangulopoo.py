
#triangulo, lado mayor, equilátero, escaleno, isósceles
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    def tipo(self):
        if self.lado1 == self.lado2 == self.lado3:
            print("El triángulo es equilátero.")
        elif self.lado1 != self.lado2 and self.lado1 != self.lado3 and self.lado2 != self.lado3:
            print("El triángulo es escaleno.")
        else:
            print("El triángulo es isósceles")
    def long(self):
        if self.lado1 > self.lado2 and self.lado3:
            print("El lado más largo mide " + str(self.lado1))
        elif self.lado2 > self.lado1 and self.lado3:
            print("El lado más largo mide " + str(self.lado2))
        else:
            print("El lado más largo mide " + str(self.lado3))
#code
lado1 = float(input("Introduzca la longitud del primer lado:\t"))
while lado1 <= 0:
    lado1 = float(input("Introduzca una longitud adecuada:\t"))
lado2 = float(input("Introduzca la longitud del segundo lado:\t"))
while lado2 <= 0:
    lado2 = float(input("Introduzca una longitud adecuada:\t"))
lado3 = float(input("Introduzca la longitud del tercer lado:\t"))
while lado3 <= 0:
    lado3 = float(input("Introduzca una longitud adecuada:\t"))
while lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
    print("El triángulo no existe, elige un lado a modificar:\n1, 2, 3\n")
    mod = int(input())
    while mod < 1 or mod > 3:
        mod = int(input("Escribe una opción válida:\t"))
    if mod == 1:
        lado1 = float(input("Introduzca la longitud del primer lado:\t"))
        while lado1 <= 0:
            lado1 = float(input("Introduzca una longitud adecuada:\t"))
    elif mod == 2:
        lado2 = float(input("Introduzca la longitud del segundo lado:\t"))
        while lado2 <= 0:
            lado2 = float(input("Introduzca una longitud adecuada:\t"))
    else:
        lado3 = float(input("Introduzca la longitud del tercer lado:\t"))
        while lado3 <= 0:
            lado3 = float(input("Introduzca una longitud adecuada:\t"))
triangulo = Triangulo(lado1, lado2, lado3)
triangulo.long()
triangulo.tipo()
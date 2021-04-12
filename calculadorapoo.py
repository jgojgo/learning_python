#Calculadora poo
class Calculadora:
    def __init__(self):
        self.numero1 = float(input("Introduzca un número:\t"))
        self.numero2 = float(input("Introduzca un segundo número:\t"))
    def imprimir(self):
        print(f"El primer número es {self.numero1} y el segundo es {self.numero2}")
    def suma(self):
        print(f"El resultado es {self.numero1 + self.numero2}")
    def resta(self):
        print(f"1. Minuendo {self.numero1}\n2. Minuendo {self.numero2}")
        optresta = int(input())
        while optresta < 1 or optresta > 2:
            optresta = int(input("Introduzca una opción adecuada:\t"))
        if optresta == 1:
            print(f"El resultado es {self.numero1 - self.numero2}")
        else:
            print(f"El resultado es {self.numero2 - self.numero1}")
    def multiplicacion(self):
        print(f"El resultado es {self.numero1 * self.numero2}")
    def division(self):
        print(f"1. Numerador {self.numero1}\n2. Numerador {self.numero2}")
        optdivision = int(input())
        while optdivision < 1 or optdivision > 2:
            optdivision = int(input("Introduzca una opción adecuada:\t"))
        if optdivision == 1:
            while self.numero2 == 0:
                self.numero2 = float(input("No se puede dividir por cero, cámbie el número:\t"))
            print(f"El resultado es: {self.numero1 / self.numero2}")
        else:
            while self.numero1 == 0:
                self.numero1 = float(input("No se puede dividir por cero, cámbie el número:\t"))
            print(f"El resultado es: {self.numero2 / self.numero1}")
opcion = int(input("Escoja qué cálculo desea realizar:\n1. Suma\t\t\t\t2. Resta\n3. Multiplicación\t4.División\n"))
while opcion < 1 or opcion > 4:
    opcion = int(input("Escoja una opción adecuada:\t"))
calculo1 = Calculadora()
if opcion == 1:
    calculo1.suma()
elif opcion == 2:
    calculo1.resta()
elif opcion == 3:
    calculo1.multiplicacion()
elif opcion == 4:
    calculo1.division()


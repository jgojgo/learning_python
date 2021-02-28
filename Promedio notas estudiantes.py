nestudiantes = int(input("Introduzca el número de estudiantes:\n"))
nnotas = int(input("Introduzca el número total de notas:\n"))
list = []
nombres = []
for i in range(nestudiantes):
    nombres.append(input("Introduzca el nombre del estudiante:\n"))
    contador_notas = 1
    b = 0
    while contador_notas <= nnotas:
        nota = float(input("Introduzca una nota:\n"))
        while nota < 0 or nota > 10:
            nota = float(input("Las notas no pueden ser ni inferiores a cero ni superiores a 10, MAMAGUEBO:\n"))
        b = b + nota
        contador_notas += 1
    list.append(b / nnotas)
for j in range(nestudiantes):
    print(nombres[int(j)],"tiene un  promedio de" ,list[int(j)])


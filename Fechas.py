print("¿EXISTE UNA FECHA?")
a = int(input("Introduzca el año:\n"))
m = int(input("Introduzca el número del mes:\n"))
d = int(input("Introduzca el número del día:\n"))
dia_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if a >= 1582:
    if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
        dia_mes[1] += 1
    if m < 1 or m > 12:
        print("La fecha no existe")
    else:
        m -= 1
        if d < 1 or d > dia_mes[m]:
            print("La fecha no existe")
        elif 1 <= d <= dia_mes[m]:
            print("La fecha existe")
else:
    print("La fecha ha de ser superior a 1582")

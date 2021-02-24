from math import *

print("CALCULADORA BÁSICA, SI ERES COMUNISTA NO LA INTENTES USAR, TE SERÁ COMPLICADO"
      "\nINTRODUZCA LOS NÚMEROS QUE DESEA OPERAR\n")
a = float(input("a =\t"))
b = float(input("b =\t"))
print("\nElija la opción que desea realizar:\n1) Sumar\n2) Restar\n3) Multiplicar\n4) Dividir\n5) Potencia\n6) "
      "Logaritmo\n7) Raíz")
opcion = int(input("\nEscriba una opción:\t"))
while opcion != 1 and opcion != 2 and opcion != 3 \
        and opcion != 4 and opcion != 5 and opcion != 4 and opcion != 5 and opcion != 6 and opcion != 7:
    opcion = int(input("Vamos a ver gilipollas, tienes que meter un número del 1 al 7, Pensé que te daba el "
                       "cerebro:\n"))
if opcion == 1:
    orden1 = int(input(f"Escoja el orden de los sumandos:\n1) {a} + {b} \t2) {b} + {a}\n"))
    while orden1 != 1 and orden1 != 2:
        orden1 = int(input("Tú comes piedras no? hay DOS opciones, pon el UNO o el DOS!:\n"))
    if orden1 == 1:
        print(f"El resultado es: {a + b}")
    else:
        print(f"El resultado es: {b + a}")
elif opcion == 2:
    orden2 = int(input(f"Escoja el minuendo (recuerde que el minuendo ocupa la primera posición):\n"
                       f"1) {a} \t2) {b}\n"))
    while orden2 != 1 and orden2 != 2:
        orden2 = int(input("A ti te cagaron y te le caiste al médico. Pon el puto UNO o el DOS gilipollas:\n"))
    if orden2 == 1:
        print(f"El resultado es: {a - b}")
    else:
        print(f"El resultado es: {b - a}")
elif opcion == 3:
    orden3 = int(input("Recuerde que como en la suma, el orden de los factores no altera el producto,\n"
                       "pero para complicar el algoritmo, escoja el orden de los factores:\n"
                       f"1) {a} * {b} \t2) {b} * {a}\n"))
    while orden3 != 1 and orden3 != 2:
        orden3 = int(input("Eres una cagada, asquerosa, repelente, malnacido, coprofágico, ruin, rastrera,\ndeleznable,"
                           " subnormal, retrasada, COMUNISTA. Solo tienes que poner un número, el\nUNO o el DOS, hazlo"
                           " gilipollas:\n"))
    if orden3 == 1:
        print(f"El resultado es: {a * b}")
    else:
        print(f"El resultado es: {b * a}")
elif opcion == 4:
    orden4 = int(input(f"Seleccione el orden del dividendo y el divisor:\n1) {a}/{b} \t2) {b}/{a}\n"))
    while orden4 != 1 and orden4 != 2:
        orden4 = int(input("Te he metido un virus espía en el PC por no saber poner el 1 o el 2\n"
                           "Sinceramente no pensé que fueses tan tonta xd, hazlo:\n"))
    if orden4 == 1:
        while a == 0:
            a = float(input("Eres consciente de que si el numerador es cero, la división da infinito no?\nah es verdad "
                            "que eres un aborto fallido que ni puede pensar.\nA VER GORRINAPIO SI QUIERES"
                            " QUE LA DIVISIÓN"
                            " FUNCIONE, NO COMO EL SOCIALISMO,\n METE UN NÚMERO QUE NO SEA CERO:\n"))
        print(f"El resultado es: {a / b}")
    else:
        while b == 0:
            b = float(input("Tú seguro que eres de los que quieren que el sueldo mínimo sea de 2000€ al mes."
                            " Eres consciente de que si el numerador es cero, la división vale infinito?\n"
                            "Anda, mete un número adecuado campeón, ya verás que el socialismo se te curará pronto"
                            ", estamos contigo, mucho ánimo:\n"))
        print(f"El resultado es: {b / a}")
elif opcion == 5:
    orden5 = int(input(f"Cuál es la base, y cuál es el exponente?\n1) La base es {a} y el exponente es {b} \t2) La base"
                       f" es {b} y el exponente es {a}\n"))
    while orden5 != 1 and orden5 != 2:
        orden5 = int(input("Seguro que tu madre te limpia el culo, mete el número 1 o el número 2"
                           ", se hace con los dedos y el teclado que tienes delante:\n"))
    if orden5 == 1:
        print(f"El resultado es: {pow(a, b)}")
    else:
        print(f"El resultado es: {pow(b, a)}")
elif opcion == 6:
    while a <= 0 or b <= 0:
        print("A ver subnormal, ninguna de las partes de un logaritmo puedes ser cero o inferior. ¡CÁMBIALO AHORA MISMO"
              "MARRAN@!")
        a = float(input(f"Dale Carla, méteme un número mayor que 0:\n"))
        b = float(
            input(f"Como vuelvas a poner un número igual a 0 o inferior te juro que salgo del pc y dormiré contigo"
                  " esta noche:\n"))
    orden6 = int(input(f"Escriba la forma del logaritmo:\n1) log{a}({b}) \t2) log{b}({a})\n"))
    while orden6 != 1 and orden6 != 2:
        orden6 = int(input(f"MONKEEEE uuuuuu mete el uno o el dos retragorricomunazi:\n"))
    if orden6 == 1:
        print(f"El resultado es: {log(b, a)}")
    else:
        print(f"El resultado es: {log(a, b)}")
elif opcion == 7:
    orden7 = float(input(f"Escriba el radicando con el teclado:\n"))
    while orden7 != a and orden7 != b:
        orden7 = float(input(f"Has metido el {a} y el {b} en serio tienes tantas piedras\nen el cerebro como "
                             f"para poner un número distinto?\nAnda y ve a comer cemento o mete uno de los"
                             f" números que has introducido:\n"))
    if orden7 == a:
        while b == 0:
            b = float(input("De verdad que tú dentro del cerebro tienes a Eduardo Garzón\n con la impresora xddd"
                            ". Eres consciente de que el índice no puedes ser cero, no?. Modificalo guarro:\n"))
        print(f"El resultado de sqrt{b}({a}) es: {pow(a, (1 / b))}")
    else:
        while a == 0:
            a = float(input("Se nota que no has tenido a la Lurdes, el índice no puede ser cero\n COMUNAZI"
                            " mete uno adecuado:\n"))
        print(f"El resultado de sqrt{a}({b}) es: {pow(b, (1 / a))}")
input()

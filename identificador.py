#Funciones
def DNI ():
    dni = str(input("Introduzca su DNI:\n"))
    while len(dni) != 9:
        dni = str(input("Introduzca un DNI real:\n"))
    return dni

def nombre_y_apellidos():
    nombre_completo = []
    name = str(input("Introduzca su nombre y sus apellidos, el segundo nom"
                       "bre cuenta como un apellido.\n Para finalizar, escriba ^fin^\n"))
    while not name.isalpha():
        name = str(input("Solo están permitidos caracteres alfanuméricos, introduzca otro nombre:\n"))
    nombre_completo.append(name)
    while name != "fin":
        name = str(input("Introduzca su apellido:\n"))
        while not name.isalpha():
            name = str(input("Solo están permitidos caracteres alfanuméricos, introduzca otro apellido:\n"))
        nombre_completo.append(name)
    nombre_completo.pop()
    return nombre_completo

def nombre (i):
    nombre = " ".join(i)
    return nombre

def resultado (i, b, a):
    print(f"Nombre: {i}\n")
    print(f"DNI: {b}\n")
    print(f"Identificador: {a[1]}{b[:5]}")

#Código
a = nombre_y_apellidos()
i = nombre(a)
b = DNI()
resultado(i, b, a)


"""
preg = open("utn/random/asd.txt", "r+")
text = preg.readline()
input = input(text)
preg.write(input + "\n")
preg.close()
"""

"""
def calcular_plata(cantidad_personas : int) -> int:
    return cantidad_personas * 1000


contador = 0
archivo = open("utn/random/asd.txt", "r+")
lista = archivo.readlines()
for persona in lista:
    persona = persona.strip("\n")
    if persona.lower() == "santi":
        archivo.write("Tomi" + "\n")
archivo.close()
archivo = open("utn/random/asd.txt", "r")
lista2 = archivo.readlines()
print("Lista de personas")
for persona in lista2:
    persona = persona.strip("\n")
    contador += 1
    print(f"Persona {contador}: {persona}")
cantidad_plata = calcular_plata(contador)
print(f"Cantidad de plata: {cantidad_plata}")
archivo.close()
"""

"""
#SEMANA 6 /// EJERCICIO 4: Se pide hacer un programa que pida dos palabras: una que se quiera reemplazar y la palabra por la que
#se quiera reemplazar, cambie el texto y lo guarde en el archivo otra vez.

mensaje = ""
palabra_cambiar = input("Nombre la palabra que desee cambiar: ").lower()
reemplazo = input("Palabra con la que quiere reemplazarla: ").lower()

archivo = open("utn/random/6_4.txt", "r")
lista_lineas = archivo.readlines()
for linea in lista_lineas:
    linea = linea.strip("\n")
    linea = linea.lower()
    linea = linea.replace(palabra_cambiar, reemplazo)
    mensaje = mensaje + linea + "\n"
archivo.close()

archivo2 = open("utn/random/6_4.txt", "w")
archivo2.write(mensaje)
archivo2.close()

"""

#ejer5
"""
dicc_producto = {
    "Nombre" : "Hoja A4",
    "Codigo" : "35662",
    "Precio" : "600",
    "Stock" : "45"
}

def agregar_dicc_csv(dicc : dict, archivo) -> None:
    archivo.write(f"{dicc['Nombre']},{dicc['Codigo']},{dicc['Precio']},{dicc['Stock']}")

archivo = open("utn/random/infoStock.csv", "r+")
lista_Stock = archivo.readlines()
archivo.close()
for linea in lista_Stock:
    linea = linea.strip("\n")
    linea = linea.split(",")
    print(f"""# Nombre del producto: {linea[0]}
#Codigo del producto: {linea[1]}
#Precio por unidad: {linea[2]}
#Stock: {linea[3]}
""")
archivo.close()
agregar_dicc_csv(dicc_producto, archivo)
"""

"""
#ejer6

lista_alumnos =\
[
    {
        "Nombre" : "Juan",
        "Apellido" : "Perez",
        "DNI" : "12345678",
        "Nota" : "7"
    },
    {
        "Nombre" : "Pedro",
        "Apellido" : "Gomez",
        "DNI" : "87654321",
        "Nota" : "4"
    },
    {
        "Nombre" : "Maria",
        "Apellido" : "Lopez",
        "DNI" : "98765432",
        "Nota" : "9"
    },
    {
        "Nombre" : "Ana",
        "Apellido" : "Garcia",
        "DNI" : "76543218",
        "Nota" : "3"
    }
]

def leer_dicc_alumno(dicc : dict, archivo : str) -> None:
    mensaje = f"{dicc['Nombre']},{dicc['Apellido']},{dicc['DNI']},{dicc['Nota']}"
    return mensaje

csv_packet = ""

for alumno in lista_alumnos:
    csv_packet = csv_packet + leer_dicc_alumno(alumno, "utn/random/notas.csv") + "\n"

archivo = open("utn/random/notas.csv", "w")
archivo.write(csv_packet)
archivo.close()

archivo2 = open("utn/random/notas.csv", "r")
lista_alumnos_csv = archivo2.readlines()
archivo2.close()

lista_notas = []
contador_desaprobados = 0

for alumno in lista_alumnos_csv:
    alumno = alumno.strip("\n")
    alumno = alumno.split(",")
    lista_notas.append(alumno[3])

for nota in lista_notas:
    print(nota)
    if int(nota) < 4:
        contador_desaprobados += 1
print(f"Cantidad de alumnos desaprobados: {contador_desaprobados}")
"""

"""
#ejer4

try:
    archivo = open("utn/random/asd.csv", "r")
    archivo.close()
except FileNotFoundError:
    print("El archivo no existe")
"""

"""
#ejer5

def mostrar_elemnto(lista : list, indice : int):
    try:
        print(lista[indice])
    except IndexError:
        print("Indice fuera de rango")

lista = [1, 2, 3, 4, 5]

mostrar_elemnto(lista, 6)
"""

#ejer6
"""
def pedir_jugadores():
    cantidad_jugadores = int(input("Cuantos jugadores son?: "))
    return cantidad_jugadores

try:
    cantidad_jugadores = pedir_jugadores()
except ValueError:
    print("Debe ingresar un numero")

if cantidad_jugadores > 4 or cantidad_jugadores < 2:
    if cantidad_jugadores > 4:
        print("La cantidad de jugadores no puede ser mayor a 4")
    else:
        print("La cantidad de jugadores no puede ser menor a 2")
else:
    print(f"Cantidad de jugadores: {cantidad_jugadores}")
"""
#ejer7
"""
def pedir_jugadores():
    cantidad_jugadores = int(input("Cuantos jugadores son?: "))
    return cantidad_jugadores

try:
    cantidad_jugadores = pedir_jugadores()
    if cantidad_jugadores % 2 == 0:
        if cantidad_jugadores > 6 or cantidad_jugadores < 2:
            print("deben ser 2, 4 o 6 jugadores")
        else:
            print(f"Cantidad de jugadores: {cantidad_jugadores}")
    else:
        print("No pueden jugar si con impares")
except ValueError:
    print("Debe ingresar un numero")
"""
#ejer8
"""
opciones = {
    1 : "Hamburguesas",
    2 : "Milanesas",
    3 : "Gaseosa",
    4 : "Alfajor",
    5 : "Papas Fritas",
    6 : "Agua"
}

valores = {
    1 : 1000,
    2 : 1500,
    3 : 500,
    4 : 300,
    5 : 600,
    6 : 350
}

print("Opciones: ")
for i in range(1, len(opciones)+1):
    print(f"{i}. {opciones[i]} -> {valores[i]}")

while True:
    try:
        opcion = int(input("Cual opcion va a elegir?: "))
        cantidad = int(input("Cuantas quiere llevar?: "))
        print(f"Total a pagar: {valores[opcion] * cantidad}")
        break
    except ValueError:
        print("Debe ingresar un numero")
    except KeyError:
        print("No existe esa opcion")
"""
#modificado
"""
total = 0
while True:
    try:
        compra = int(input("Que desea comprar? (0 para cerrar la compra): "))
        if compra == 0:
            break
        total += valores[compra]
    except KeyError:
        print("No existe esa opcion")
    except ValueError:
        print("Debe ingresar un numero")
print(f"Total a pagar{total}")
"""
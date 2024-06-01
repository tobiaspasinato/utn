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

with open("archivo.txt", "w") as archivo:
    archivo.write("Esta es una línea de texto.")

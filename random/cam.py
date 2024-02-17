"""contador = 0
acumulador = 0
cantidad_de_numeros = 5

while contador < cantidad_de_numeros:
    num = int(input("Ingrese un numero: "))
    acumulador = acumulador + num
    contador += 1

resultado = acumulador / cantidad_de_numeros

print(f"El promedio es {resultado}")"""

lista = ["hola", 3, "asd", "jajaja", 3.14]
lista2 = []
contador = 0

for elemento in lista:
    if type(elemento) == int:
        lista2.append(elemento)
    else:
        contador += 1

for e in lista2:
    print(e)
print(contador)
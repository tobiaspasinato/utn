contador = 0
acumulador = 0
cantidad_de_numeros = 5

while contador < cantidad_de_numeros:
    num = int(input("Ingrese un numero: "))
    acumulador = acumulador + num
    contador += 1

resultado = acumulador / cantidad_de_numeros

print(f"El promedio es {resultado}")
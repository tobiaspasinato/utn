lista_num = [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
num_mayor = lista_num[0]
for numero in lista_num:
    if num_mayor < numero:
        num_mayor = numero

print(f"El numero mayor es: {num_mayor}")
contador_while = 0
contador_num_par = 0
contador_num_impar = 0
flag_menor = True
flag_mayor_par = True
acumulador_positivo = 0
acumulador_negativo = 0
contador_negativos = 0


while contador_while < 5:
    numero_ingresado = int(input("Ingrese un numero: "))
    while numero_ingresado == 0:
        numero_ingresado = int(input("Ingrese un numero: "))

    if numero_ingresado / 2 == 0:
        contador_num_par += 1
        if numero_ingresado > numero_par_mayor or flag_mayor_par == True:
            numero_par_mayor = numero_ingresado
            flag_mayor_par == False
    else:
        contador_num_impar += 1
    
    if numero_ingresado < numero_menor or flag_menor == True:
        numero_menor = numero_ingresado
        flag_menor == False
    
    if numero_ingresado >= 0:
        acumulador_positivo += numero_ingresado
    else:
        acumulador_negativo += numero_ingresado
        contador_negativos += 1

    contador_while += 1

producto_negativo = acumulador_negativo * contador_negativos

print(f"""Cantidad de pares: {contador_num_par}
    Cantidad de impares: {contador_num_impar}
    Menor numero ingresado: {numero_menor}
    De los pares el mayor número ingresado: {numero_par_mayor}
    Suma de los positivos: {acumulador_positivo}
    Producto de los negativos: {producto_negativo}
    """)
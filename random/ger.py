def pedir_clima() -> list:
    lista_clima = []
    contador = 0
    while True:
        if contador == 6:
            break
        clima_dia = int(input(f"El clima del dia {contador+1}: "))
        while clima_dia < -5 or clima_dia > 45:
            clima_dia = int(input(f"ERROR, El clima del dia {contador+1}: "))
        lista_clima.append(clima_dia)
        contador += 1
    return lista_clima

def mostrar_promedio_clima(lista_dias : list) -> int:
    acumulador_promedio = 0
    for dia in lista_dias:
        acumulador_promedio += dia
    promedio = acumulador_promedio / len(lista_dias)
    return promedio

def mostrar_clima_mayor(lista_dias : list) -> int:
    bandera_mayor = False
    contador = 0
    lista = []
    for dia in lista_dias:
        contador += 1
        if bandera_mayor == False or dia > mayor:
            mayor = dia
            dia_mayor = contador
            bandera_mayor = True
    return dia_mayor

def mostrar_info() -> None:
    contador_dia = 0
    lista_dias = pedir_clima()
    promedio = mostrar_promedio_clima(lista_dias)
    dia_mayor = mostrar_clima_mayor(lista_dias)
    for dia in lista_dias:
        contador_dia += 1
        if dia > promedio:
            print(f"El dia {contador_dia} tiene una temperatura mayor al promedio ({dia})")
    print(f"El promedio de los dias es: {promedio}\nEl dia con mayor temperatura es: {dia_mayor}")

mostrar_info()
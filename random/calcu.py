#La funcion "calcular_suma" toma por parametros 2 numeros y retorna el resultado de su suma
def calcular_suma(a : int, b : int):
    return a + b
#La funcion "calcular_resta" toma por parametros 2 numeros y retorna el resultado de su resta
def calcular_resta(a : int, b : int):
    return a - b
#La funcion "calcular_multiplicacion" toma por parametros 2 numeros y retorna el resultado de su multiplicacion
def calcular_multiplicacion(a, b):
    return a * b
#La funcion "calcular_division" toma por parametros 2 numeros y retorna el resultado de su division
def calcular_division(a, b):
    if b == 0:
        return False
    else:
        return a / b
#La funcion "calcular_factorial" toma por parametro 1 numero y retorna el resultado de su factorial
def calcular_factorial(a):
    pass

def mostrar_suma(a : int, b : int,r : int):
    """
    Esta funcion imprime el retorno de la funcion "calcular_suma()"
    """
    print(f"El resultado de {a} + {b} es : {r}")

def mostrar_resta(a : int, b : int,r : int):
    """
    Esta funcion imprime el retorno de la funcion "calcular_resta()"
    """
    print(f"El resultado de {a} - {b} es : {r}")

def mostrar_multiplicacion(a : int, b : int,r : int):
    """
    Esta funcion imprime el retorno de la funcion "calcular_multiplicacion()"
    """
    print(f"El resultado de {a} * {b} es : {r}")

def mostrar_division(a : int, b : int,r : int):
    """
    Esta funcion imprime el retorno de la funcion "calcular_division()"
    """
    if r == False:
        print("No se puede dividir por 0")
    else:
        print(f"El resultado de {a} / {b} es : {r}")

def mostrar_factorial(a : int, b : int, r1 : int, r2 : int):
    """
    Esta funcion muestra el retorno de la funcion "calcular_factorial(r1)" y "calcular_factorial(r2)
    """
    print(f"El factorial de {a} es : {r1} y el factorial de {b} es : {r2}")

from functions import *
from data import *

menu = """A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB
        B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
        C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
        D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
        E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
        F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB
        G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
        H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
        I. Listar todos los superhéroes agrupados por color de ojos.
        J. Listar todos los superhéroes agrupados por tipo de inteligencia.
        K. Normalizar datos.
        L. SALIR
    """

while True:
    imprimir(menu)
    opcion = input("Opción: ")
    opcion.upper()
    match opcion:
        case "L":
            break
        case "K":
            stark_normalizar_dato(lista_personajes)
        case "A":
            sumar_dato_heroe(lista_personajes, "altura")
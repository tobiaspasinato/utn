from data import *
from functions import *

mensaje = """A. Imprimir la lista de heroes junto a sos caracteristicas.
            \nB.Heroe mas fuerte.
            \nC.heroe mas bajo.
            \nD.Peso promedio
            \nE.Heroes que superen la fuerza promedio femenina
            \nF.Salir"""

while True:
    imprimir(mensaje)
    opcion = input("cual opcion quiere? ")

    match opcion:
        case "F":
            break
        case "A":
            recorrer_lista(lista_personajes)
        case "B":
            imprimir(fuerza_max(normalizar_dato(lista_personajes)))

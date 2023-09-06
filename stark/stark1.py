from data import *
from functions import *

normalizar_dato(lista_personajes)

mensaje = """A.Imprimir la lista de heroes junto a sos caracteristicas.
            \nB.Heroe mas fuerte.
            \nC.heroe mas bajo.
            \nD.Peso promedio de los personajes masculinos.
            \nE.Heroes que superen la fuerza promedio femenina
            \nF.Salir"""

while True:
    imprimir(mensaje)
    opcion = input("cual opcion quiere? ")

    match opcion:
        case "A":
            recorrer_lista(lista_personajes)
        case "B":
            imprimir(max_min(lista_personajes, "max", "fuerza"))
        case "C":
            imprimir(max_min(lista_personajes, "min", "altura"))
        case "D":
            imprimir(peso_promedio_masculino(lista_personajes))
        case "E":
            mostrar_heroes_fmasf(lista_personajes, promedio_fuerza_fem(lista_personajes))
        case "F":
            break
from data import *
from functions_stark import *

normalizar_dato(lista_personajes)

mensaje = """A.Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB
        \nB.Recorrer la lista y determinar cuál es el superhéroe más alto de género F
        \nC.Recorrer la lista y determinar cuál es el superhéroe más alto de género M
        \nD.Recorrer la lista y determinar cuál es el superhéroe más débil de género M
        \nE.Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
        \nF.Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB
        \nG.Determinar cuántos superhéroes tienen cada tipo de color de ojos
        \nH.Determinar cuántos superhéroes tienen cada tipo de color de pelo
        \nI.Listar todos los superhéroes agrupados por color de ojos
        \nJ.Listar todos los superhéroes agrupados por tipo de inteligencia
        \nK.SALIR
"""

while True:
    imprimir(mensaje)
    opcion = input("Cual opción quiere?: ")
    opcion = opcion.upper()
    match opcion:
        case "K":
            break
        case "A":
            mostrar_perso_gen(lista_personajes, "NB" ,"genero")
        case "B":
            imprimir(mostrar(personaje_alto_debil(lista_personajes, "altura", "F", "max")))
        case "C":
            imprimir(mostrar(personaje_alto_debil(lista_personajes, "altura", "M", "max")))
        case "D":
            imprimir(mostrar(personaje_alto_debil(lista_personajes, "fuerza", "M", "min")))
        case "E":
            imprimir(mostrar(personaje_alto_debil(lista_personajes, "fuerza", "NB", "min")))
        case "F":
            imprimir(fuerza_promedio_nb(lista_personajes))
        case "G":
            imprimir(contador_de_ojos(lista_personajes))
        case "H":
            imprimir(contador_de_pelo(lista_personajes))
        case "I":
            imprimir(listar_perso_ojos(lista_personajes))
        case "J":
            imprimir(listar_type_iq(lista_personajes))
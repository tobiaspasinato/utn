from datos import *

lista_preguntas = []
lista_a = []
lista_b = []
lista_c = []
lista_correcta = []

for pregunta in lista:
    lista_preguntas.append(pregunta["pregunta"])
    lista_a.append(pregunta["a"])
    lista_b.append(pregunta["b"])
    lista_c.append(pregunta["c"])
    lista_correcta.append(pregunta["correcta"])


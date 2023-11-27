import os
import re
import json
import csv
from data import lista_personajes

def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
        return contenido
    except:
        print(f"Error al leer el archivo {nombre_archivo}")
        return False

def guardar_archivo(nombre_archivo, contenido):
    try:
        with open(nombre_archivo, 'w+') as archivo:
            archivo.write(contenido)
        print(f"Se creó el archivo: {nombre_archivo}")
        return True
    except:
        print(f"Error al intentar crear el archivo")
        return False

def generar_csv(nombre_ruta : str, lista_personajes : list):
    if len(lista_personajes) > 0:
        contenido = "nombre,identidad,empresa,altura,peso,genero,color_ojos,color_pelo,fuerza,inteligencia\n"
        for personaje in lista_personajes:
            contenido = contenido + f"{personaje['nombre']},{personaje['identidad']},{personaje['empresa']},{personaje['altura']},{personaje['peso']},{personaje['genero']},{personaje['color_ojos']},{personaje['color_pelo']},{personaje['fuerza']},{personaje['inteligencia']}\n"
        guardar_archivo(nombre_ruta, contenido)
    else:
        return False

def leer_csv(nombre_ruta) -> list:
    lista = []
    contenido = leer_archivo(nombre_ruta)
    if not contenido:
        return False
    contenido = contenido.split("\n")
    cabecera = contenido[0].split(",")
    for elemento in contenido[1:-1]:
        dicc = {}
        personaje = elemento.split(",")
        for indice in range(len(cabecera)):
            dicc[cabecera[indice]] = personaje[indice]
        lista.append(dicc)
    return lista

def generar_json(nombre_archivo: str, lista_heroes: list, nombre_lista: str):
    data = {}
    data[nombre_lista] = []
    
    for personaje in lista_heroes:
        data[nombre_lista].append({
            'nombre': personaje['nombre'],
            'identidad': personaje['identidad'],
            'empresa': personaje['empresa'],
            'altura': personaje['altura'],
            'peso': personaje['peso'],
            'genero': personaje['genero'],
            'color_ojos': personaje['color_ojos'],
            'color_pelo': personaje['color_pelo'],
            'fuerza': personaje['fuerza'],
            'inteligencia': personaje['inteligencia']
        })
    
    with open(nombre_archivo, 'w') as file:
        json.dump(data, file, indent = 4, ensure_ascii = False)

def leer_json(nombre_archivo : str, nombre_lista : str):
    if len(nombre_lista) > 0:
        with open(nombre_archivo) as nombre_lista:
            data = json.load(nombre_lista)
            return data
    else:
        return False

def ordenar(lista:list, key:str):
    # va a obtener una lista y key como parametro
    opcion = input("Ordenar de manera ascendente (asc) o descendente (desc)? ").lower()
    # le pedimos al usuario de la consola que escriba la forma de ordenar la lisata

    while not re.search("asc|desc", opcion) or opcion == "":
        opcion = input("Ordenar de manera ascendente (asc) o descendente (desc)? ").lower()
        # verifica que el usuario ingrese una de las dos opciones dadas por el programa

    for i in range(len(lista)-1):
        # itera en la menos en el ultimo dato de esta
        for j in range(i+1,len(lista)):
            # itera en la lista una posicion adelante del primer for
            if opcion == "asc":
                # si la opcion elegida es la que busca el if entra en el
                if(lista[i][key] > lista[j][key]):
                    # compara si el elemoento de la lista i es mayor que el de la lista j
                    aux = lista[i]
                    # si ingreso al if porcede a guardar el elemento i en la variable auxiliar
                    lista[i] = lista[j]
                    # sobre escribe los datos de "lista[i]" por los de "lista[j]"
                    lista[j] = aux
                    # y usamos el aux para mover el valor que se sobrescribio anteriormente
            else:
                # este else lo que hace es mandar al usuario a la opcion que eligio (al ser solo 2 posibles rutas)
                if(lista[i][key] < lista[j][key]):
                    # compara si el elemoento de la lista i es mayor que el de la lista j
                    aux = lista[i]
                    # si ingreso al if porcede a guardar el elemento i en la variable auxiliar
                    lista[i] = lista[j]
                    # sobre escribe los datos de "lista[i]" por los de "lista[j]"
                    lista[j] = aux
                    # y usamos el aux para mover el valor que se sobrescribio anteriormente
    for personaje in lista:
        # con la lista ya ordenada como el usuario quiere iteramon en cada elemento de la lista
        personaje_ordenado = personaje[key]
        # guarda el dato del personaje que queremos mostrar
        personaje_ordenado_name = personaje["name"]
        # para no confundir al usuario guardamos el nombre del personaje del dato anterior
        print(f"Personaje: {personaje_ordenado_name} | {personaje_ordenado}")
        # imprimimos los datos anteriores cada vez que el for itere en algun elemoento
    return lista
    # retornamos la lista ordenada para el uso de la exportacion al csv



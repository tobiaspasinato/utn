import os
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
        with open(nombre_archivo, 'r+') as archivo:
            archivo.write(contenido)
        print(f"Se creó el archivo: {nombre_archivo}")
        return True
    except:
        print(f"Error al intentar crear el archivo")
        return False

def generar_csv(nombre_del_archivo : str, lista : list, key1 = "nombre", key2 = "edad", key3 = "altura"):
    if len(lista) > 0:
        cabecera = "Nombre,Identidad,Altura\n"
        contenido_csv = cabecera + "\n".join(f"{lista[key1]}, {lista[key2]}, {lista[key3]}" for superheroe in lista)
        if guardar_archivo(nombre_del_archivo, contenido_csv):
            return True
        else:
            return False
    else:
        return False

def leer_csv(path) -> list:
    lista = []
    if os.path.exists(path):
        with open(path, "r",encoding="utf-8") as archivo:
            claves = archivo.readline()
            claves = claves.replace("\n","")
            lista_claves = claves.split(",")
        
        for linea in archivo:
            # dicc = {}
            lista_elemento = linea.replace("\n", "").split(",")
            for clave,elemento in lista_claves,lista_elemento:
                elemento[clave] = elemento
            for i in range(len(lista_claves)):
                clave = lista_claves[i]
                elemento[clave] = lista_elemento[i]
            lista.append(elemento)
    
    return lista

# def generar_json(nombre_archivo : str, lista_heroes : list, nombre_lista):
#     if len(lista_heroes) > 0:
        
#     else:
#         return False

print(generar_csv("prueba1.csv", lista_personajes, "nombre", "identidad", "altura"))
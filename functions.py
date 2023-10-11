import os

def leer_csv(path) -> list:
    lista = []
    if os.path.exists(path):
        with open(path, "r",encoding="utf-8") as archivo:
            claves = archivo.readline()
            claves = claves.replace("\n","")
            lista_claves = claves.split(",")
        
        for linea in archivo:
            dicc = {}
            lista_elemento = linea.replace("\n", "").split(",")
            for clave,elemento in lista_claves,lista_elemento:
                elemento[clave] = elemento
            for i in range(len(lista_claves)):
                clave = lista_claves[i]
                elemento[clave] = lista_elemento[i]
            lista.append(elemento)
    
    return lista

def crear_csv(nombre_archivo : str, lista : list):
    if len(lista) > 0:
        lista_claves = list(lista[0].keys())
        cabecera = ",".join(lista_claves)
        print(cabecera)
        with open(nombre_archivo, "w") as archivo:
            for elemento in lista:
                lista_valores = list(elemento.values())
                datos = ",".join(lista_valores)
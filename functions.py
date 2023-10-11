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
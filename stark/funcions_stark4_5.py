import re
from re import *
import json
from data import lista_personajes

def extraer_iniciales(nombre_personaje : str) -> str:
    flag_mayusculas = True
    if nombre_personaje == "":
        vacio = "N/A"
        return vacio
    check_the = search(r"the", nombre_personaje)
    check_guion = nombre_personaje.count("-")
    if check_the == True:
        nombre_personaje = nombre_personaje.replace("the", "")
    no_iniciales = findall(r"[a-z]", nombre_personaje)
    for letra in no_iniciales:
        if flag_mayusculas == True:
            iniciales = nombre_personaje.replace(letra, "")
            flag_mayusculas = False
        iniciales = iniciales.replace(letra, "")
    if check_guion == True:
        iniciales = iniciales.replace("-", " ")
    iniciales = iniciales + " "
    iniciales = iniciales.replace(" ", ".")
    return iniciales

def obtener_dato_formato(dato : str) -> str:
    if type(dato) == str:
        dato_modificado = dato.replace(" ", "_")
        dato_modificado = dato_modificado.lower()
        return dato_modificado
    else:
        return False

def stark_imprimir_nombre_con_iniciales(dict_personaje : dict) -> str:
    if type(dict_personaje) == dict:
        if "nombre" in dict_personaje:
            nombre_modificado = f"* {obtener_dato_formato(dict_personaje['nombre'])} ({extraer_iniciales(dict_personaje['nombre'])})"
            return nombre_modificado
        else:
            return False
    else:
        return False

def stark_imprimir_nombres_con_iniciales(lista_personajes : list) -> None:
    if type(lista_personajes) == list:
        if len(lista_personajes) > 0:
            for personaje in lista_personajes:
                print(stark_imprimir_nombre_con_iniciales(personaje))
        else:
            return False
    else:
            return False

def generar_codigo_heroe(dict_personaje : dict, id : int) -> str:
    if dict_personaje["genero"] == "M" or dict_personaje["genero"] == "F" or dict_personaje["genero"] == "NB":
        if id < 10:
            if dict_personaje["genero"] == "M":
                codigo_personaje = f"M-1000000{id}"
            if dict_personaje["genero"] == "F":
                codigo_personaje = f"F-2000000{id}"
            if dict_personaje["genero"] == "NB":
                codigo_personaje = f"NB-000000{id}"
        else:
            if dict_personaje["genero"] == "M":
                codigo_personaje = f"M-100000{id}"
            if dict_personaje["genero"] == "F":
                codigo_personaje = f"F-200000{id}"
            if dict_personaje["genero"] == "NB":
                codigo_personaje = f"NB-00000{id}"
        return codigo_personaje
    return "N/A"

def stark_generar_codigos_heroes(lista_personajes : list) -> None:
    id = 0
    if len(lista_personajes) > 0:
        for personaje in lista_personajes:
            if type(personaje) == dict:
                id += 1
                print(f"{stark_imprimir_nombre_con_iniciales(personaje)} | {generar_codigo_heroe(personaje, id)}")
            else:
                return False
    else:
        return False

def sanitizar_entero(numero_str : str) -> int:
    if type(numero_str) == str:
        numero_str = numero_str.strip()
        if match("^-[0-9]+$", numero_str):
            return -2
        elif match("[0-9]+$", numero_str) == None:
            return -1
        else:
            try:
                numero_str = int(numero_str)
            except:
                return -3
            else:
                return numero_str
    else:
        return -3

def sanitizar_flotante(numero_str : str) -> float:
    if type(numero_str) == str:
        numero_str = numero_str.strip()
        if match("^-[0-9].+$", numero_str):
            return -2
        elif match("[0-9].+$", numero_str) == None:
            return -1
        else:
            try:
                numero_str = float(numero_str)
            except:
                return -3
            else:
                return numero_str
    else:
        return -3

def sanitizar_string(valor_str : str, valor_por_defecto = "-") -> str:
    if len(valor_str) > 0:
        if type(valor_str) == str:
            valor_str = valor_str.strip()
            if match("[0-9]", valor_str):
                return "n/a"
            valor_str = re.sub("/", " ", valor_str)
            return valor_str.lower()
    else:
        return valor_por_defecto.upper()

def sanitizar_dato(dict_personaje : dict, key : str, tipo_de_dato) -> bool:
    if len(dict_personaje) > 0:
        if key in dict_personaje:
            if tipo_de_dato.lower() == "float":
                dict_personaje[key] = sanitizar_flotante(dict_personaje[key])
                return True
            elif tipo_de_dato.lower() == "int":
                dict_personaje[key] = sanitizar_flotante(dict_personaje[key])
                return True
            elif tipo_de_dato.lower() == "str":
                dict_personaje[key] = sanitizar_flotante(dict_personaje[key])
                return True
            else:
                return "Tipo de dato no reconocido"
        else:
            return False
    else:
        return False

def stark_normalizar_datos(lista_personajes : list) -> None:
    if len(lista_personajes) > 0:
        for personaje in lista_personajes:
            personaje["altura"] = sanitizar_dato(personaje, "altura", "float")
            personaje["peso"] = sanitizar_dato(personaje, "altura", "float")
            personaje["color_ojos"] = sanitizar_dato(personaje, "color_ojos", "str")
            personaje["color_pelo"] = sanitizar_dato(personaje, "color_pelo", "str")
            personaje["fuerza"] = sanitizar_dato(personaje, "fuerza", "int")
            personaje["inteligencia"] = sanitizar_dato(personaje, "inteligencia", "str")
            print("Datos normalizados")
    else:
        print("Error: Lista de héroes vacía")

def normalizar_dato(lista : list):
    contador_modific = 0
    if(len(lista) > 0):
        for personaje in lista:
            if type(personaje["peso"]) != float:
                personaje["peso"] = float(personaje["peso"])
                contador_modific += 1
            if type(personaje["altura"]) != float:
                personaje["altura"] = float(personaje["altura"])
                contador_modific += 1
            if type(personaje["peso"]) != int:
                personaje["fuerza"] = int(personaje["fuerza"])
                contador_modific += 1
    if contador_modific > 0:
        print("Datos Normalizados")
        return True
    else:
        print("Hubo un error al normalizar los datos. Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente")
        return False

def stark_imprimir_indice_nombre(lista_de_personajes : list) -> None:
    lista = []
    for personaje in lista_de_personajes:
        nombre = personaje["nombre"].replace("the", "")
        nombre.replace(" ", "-")
        lista.append(nombre)
    nombres = "-".join(lista)
    print(nombres)

def generar_separador(patron : str, largo : int, imprimir = True) -> str:
    if not (1 <= len(patron) <= 2):
        return "N/A"
    if largo < 1 or largo > 235:
        return "N/A"
    separador = patron * largo
    if imprimir == True:
        print(separador)
    else:
        return separador

def generar_encabezado(titulo : str) -> None:
    generar_separador("*", 150)
    print(titulo.upper())
    generar_separador("*", 150)

def imprimir_ficha_heroe(dict_personaje : dict, id : int) -> None:
    generar_encabezado("principal")
    print(f"NOMBRE DEL HEROE:                {stark_imprimir_nombre_con_iniciales(dict_personaje)}")
    print(f"IDENTIDAD SECRETA:               {obtener_dato_formato(dict_personaje['identidad'])}")
    print(f"CONSULTORA:                      {obtener_dato_formato(dict_personaje['empresa'])}")
    print(f"CÓDIGO DE HÉROE:                 {generar_codigo_heroe(dict_personaje, id)}")
    generar_encabezado("fisico")
    print(f"ALTURA:                          {dict_personaje['altura']} cm.")
    print(f"PESO:                            {dict_personaje['peso']} kg.")
    print(f"FUERZA:                          {dict_personaje['fuerza']} N")
    generar_encabezado("SEÑAS PARTICULARES")
    print(f"COLOR DE OJOS:                   {dict_personaje['color_ojos']} N")
    print(f"COLOR DE PELO:                   {dict_personaje['color_pelo']} N")

def stark_navegar_fichas(lista_personajes : list):
    i = 0
    while True:
        imprimir_ficha_heroe(lista_personajes[i], i + 1)
        print("[ 1 ] Ir a la izquierda [ 2 ] Ir a la derecha [ 3 ] Salir")
        opcion = int(input("opcion: "))
        if i > 0:
            if opcion == 1:
                i -= 1
        if i < len(lista_personajes)-1:
            if opcion == 2:
                i += 1
        if opcion == 3:
            break
        if opcion > 3:
            opcion = int(input("opcion: "))

def stark_marvel_app(lista : list):
    while True:
        print("""1 - Imprimir la lista de nombres junto con sus iniciales
        2 - Imprimir la lista de nombres y el código del mismo
        3 - Normalizar datos
        4 - Imprimir índice de nombres
        5 - Navegar fichas
        6 - Salir
        """)
        opcion = int(input("opcion: "))
        match opcion:
            case 1:
                stark_imprimir_nombres_con_iniciales(lista)
            case 2:
                stark_generar_codigos_heroes(lista)
            case 3:
                stark_normalizar_datos(lista)
            case 4:
                stark_imprimir_indice_nombre(lista)
            case 5:
                stark_navegar_fichas(lista)
            case 6:
                break

#stark5 --------------------------------------------------------------------------------------------------------------------------
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
    opcion = input("Ordenar de manera ascendente (asc) o descendente (desc)? ").lower()
    while not re.search("asc|desc", opcion) or opcion == "":
        opcion = input("Ordenar de manera ascendente (asc) o descendente (desc)? ").lower()
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if opcion == "asc":
                if(lista[i][key] > lista[j][key]):
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
            else:
                if(lista[i][key] < lista[j][key]):
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
    for personaje in lista:
        personaje_ordenado = personaje[key]
        personaje_ordenado_name = personaje["nombre"]
        print(f"Personaje: {personaje_ordenado_name} | {personaje_ordenado}")
    return lista

def ordenar_asc(lista : list, key : str):
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if(lista[i] > lista[j]):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    for personaje in lista:
        personaje_ordenado = personaje[key]
        personaje_ordenado_name = personaje["nombre"]
        print(f"Personaje: {personaje_ordenado_name} | {personaje_ordenado}")
    return lista

def ordenar_desc(lista : list, key : str):
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if(lista[i] < lista[j]):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    for personaje in lista:
        personaje_ordenado = personaje[key]
        personaje_ordenado_name = personaje["nombre"]
        print(f"Personaje: {personaje_ordenado_name} | {personaje_ordenado}")
    return lista

def stark5_marvel_app(lista : list):
    while True:
        print("""1-Normalizar datos (No debe dejar de entrar a las otras opciones)
        ● 2-Generar CSV (Guardar la lista generada en otra variable)
        ● 3-Listar heroes del archivo CSV ordenados por altura ASC (Validar si el mismo existe)
        ● 4-Generar JSON (Guardar la lista generada en otra variable)
        ● 5-Listar heroes del archivo JSON ordenados por peso DESC (Validar si el mismo existe)
        ● 6-Ordenar Lista por fuerza (Se le tiene que preguntar al usuario si ordenar de manera ASC o DESC
        ● 7-Salir
        """)
        opcion = int(input("opcion: "))
        match opcion:
            case 1:
                stark_normalizar_datos(lista)
            case 2:
                generar_csv("game.csv", lista)
            case 3:
                ordenar_asc(leer_csv("game.csv"), "altura")
            case 4:
                generar_json("asd1.json", lista, "asd2")
            case 5:
                ordenar_desc(leer_json("asd1.json", "asd2"), "peso")
            case 6:
                ordenar(lista, "peso")
            case 7:
                break
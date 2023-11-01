import re

def imprimir(all : any):
    print(all)

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

def mostrar(dicc : dict):
    mensaje =   (f"""personaje:
                Nombre: {dicc["nombre"]}
                Identidad: {dicc["identidad"]}
                Empresa: {dicc["empresa"]}
                Altura: {dicc["altura"]}
                Peso: {dicc["peso"]}
                Genero: {dicc["genero"]}
                Color de ojos: {dicc["color_ojos"]}
                Color de Pelo: {dicc["color_pelo"]}
                Fuerza: {dicc["fuerza"]}
                Inteligencia: {dicc["inteligencia"]}""")
    return mensaje

def recorrer_lista(lista : list):
    for elemento in lista:
        imprimir(mostrar(elemento))

def max_min(lista : list, max_min : str, key : str):
    personaje_max_min = lista[0]
    
    for personaje in lista:
        if max_min == "min":
            if personaje_max_min[key] > personaje[key]:
                personaje_max_min = personaje
        elif max_min == "max":
            if personaje_max_min[key] < personaje[key]:
                personaje_max_min = personaje
                
    return personaje_max_min

def peso_promedio_masculino(lista : list):
    acumulador_peso = 0
    acumulador_perso_masculinos = 0

    for personaje in lista:
        if personaje["genero"] == "M":
            acumulador_peso = acumulador_peso + personaje["peso"]
            acumulador_perso_masculinos += 1
    
    resultado = acumulador_peso / acumulador_perso_masculinos
    mensaje = f"Peso promedio de los personajes masculinos: {resultado}"
    return mensaje

def promedio_fuerza_fem(lista : list):
    acumulador_fuerza_fem = 0
    contador_fem = 0
    
    for personaje in lista:
        if personaje["genero"] == "F":
            acumulador_fuerza_fem = acumulador_fuerza_fem + personaje["fuerza"]
            contador_fem += 1
    
    promedio_fuerza_fem = acumulador_fuerza_fem / contador_fem
    
    return promedio_fuerza_fem

def mostrar_heroes_fmasf(lista:list, promedio : int):
    for personaje in lista:
        if personaje["fuerza"] > promedio:
            imprimir(f"""Personaje:
                    Nombre: {personaje["nombre"]}
                    Peso: {personaje["peso"]}""")

# stark2------------------------------------------------------------------------------------------------------------------------------------

def mostrar_perso_gen(lista : list, gen : str, key : str):
    for personaje in lista:
        if personaje[key] == gen:
            imprimir(f"Nombre: {personaje['nombre']}")

def personaje_alto_debil(lista : list, key : str, gen : str, max_min : str):
    bandera = False
    
    for personaje in lista:
        if personaje["genero"] == gen:
            if bandera == False:
                personaje_flag = personaje
                bandera = True
            if max_min == "min":
                if personaje[key] < personaje_flag[key]:
                    personaje_flag = personaje
            elif max_min == "max":
                if personaje[key] > personaje_flag[key]:
                    personaje_flag = personaje
    
    return personaje_flag

def fuerza_promedio_nb(lista : list):
    acumulador_perso = 0
    contador_perso = 0
    for personaje in lista:
        if personaje["genero"].upper() == "NB":
            acumulador_perso = acumulador_perso + personaje["fuerza"]
            contador_perso += 1
    resultado = acumulador_perso / contador_perso
    
    return resultado

def contador_de_ojos(lista : list):
    brown_cont = 0
    blue_cont = 0
    green_cont = 0
    hazel_cont = 0
    yellow_cont = 0
    silver_cont = 0
    red_cont = 0
    for personaje in lista:
        if personaje["color_ojos"].upper() == "BROWN":
            brown_cont += 1
        if personaje["color_ojos"].upper() == "BLUE":
            blue_cont += 1
        if personaje["color_ojos"].upper() == "GREEN":
            green_cont += 1
        if personaje["color_ojos"].upper() == "YELLOW" or personaje["color_ojos"].upper() == "YELLOW (WITHOUT IRISES)":
            yellow_cont += 1
        if personaje["color_ojos"].upper() == "SILVER":
            silver_cont += 1
        if personaje["color_ojos"].upper() == "RED":
            red_cont += 1
        if personaje["color_ojos"].upper() == "HAZEL":
            hazel_cont += 1
    
    mensaje = f"""Color de Ojos:
    Brown: {brown_cont}
    Blue: {blue_cont}
    Green: {green_cont}
    Hazel: {hazel_cont}
    Yellow: {yellow_cont}
    Silver: {silver_cont}
    Red: {red_cont}
    """
    return mensaje

def contador_de_pelo(lista : list):
    yellow_cont = 0
    brown_cont = 0
    black_cont = 0
    auburn_cont = 0
    red_orange = 0
    white_cont = 0
    no_Hair_cont = 0
    blond_cont = 0
    green_cont = 0

    for personaje in lista:
        if personaje["color_pelo"].upper() == "YELLOW":
            yellow_cont += 1
        if personaje["color_pelo"].upper() == "BROWN" or personaje["color_pelo"] == "BROWN / WHITE":
            brown_cont += 1
        if personaje["color_pelo"].upper() == "BLACK":
            black_cont += 1
        if personaje["color_pelo"].upper() == "AUBURN":
            auburn_cont += 1
        if personaje["color_pelo"].upper() == "WHITE":
            white_cont += 1
        if personaje["color_pelo"].upper() == "NO HAIR" or personaje["color_pelo"].upper() == "":
            no_Hair_cont += 1
        if personaje["color_pelo"].upper() == "BLOND":
            blond_cont += 1
        if personaje["color_pelo"].upper() == "GREEN":
            green_cont += 1
        if personaje["color_pelo"].upper() == "RED / ORANGE":
            red_orange += 1
    mensaje = f"""Color de Pelo:
    Yelow: {yellow_cont}
    Brown: {brown_cont}
    Black: {black_cont}
    Auburn: {auburn_cont}
    White: {white_cont}
    No Hair: {no_Hair_cont}
    Blond: {blond_cont}
    Green: {green_cont}
    Red / Orange: {red_orange}
    """
    return mensaje

def listar_perso_ojos(lista : list):
    brown_list = []
    blue_list = []
    green_list = []
    hazel_list = []
    yellow_list = []
    silver_list = []
    red_list = []
    for personaje in lista:
        if personaje["color_ojos"].upper() == "BROWN":
            brown_list.append(personaje["nombre"])
        if personaje["color_ojos"].upper() == "BLUE":
            blue_list.append(personaje["nombre"])
        if personaje["color_ojos"].upper() == "GREEN":
            green_list.append(personaje["nombre"])
        if personaje["color_ojos"].upper() == "YELLOW" or personaje["color_ojos"].upper() == "YELLOW (WITHOUT IRISES)":
            yellow_list.append(personaje["nombre"])
        if personaje["color_ojos"].upper() == "SILVER":
            silver_list.append(personaje["nombre"])
        if personaje["color_ojos"].upper() == "RED":
            red_list.append(personaje["nombre"])
        if personaje["color_ojos"].upper() == "HAZEL":
            hazel_list.append(personaje["nombre"])
    mensaje = f"""Listas:
    Brown: {brown_list}
    Blue: {blue_list}
    Green: {green_list}
    Hazel: {hazel_list}
    Yellow: {yellow_list}
    Silver: {silver_list}
    Red: {red_list}
    """
    return mensaje

def listar_type_iq(lista : list):
    average_list = []
    good_list = []
    high_list = []
    non_iq = []
    for personaje in lista:
        if personaje["inteligencia"].upper() == "HIGH":
            high_list.append(personaje["nombre"])
        if personaje["inteligencia"].upper() == "GOOD":
            good_list.append(personaje["nombre"])
        if personaje["inteligencia"].upper() == "AVERAGE":
            average_list.append(personaje["nombre"])
        if personaje["inteligencia"].upper() == "":
            non_iq.append(personaje["nombre"])
    mensaje = f"""Listas:
    High: {high_list}
    Good: {good_list}
    Average: {average_list}
    No Iq: {non_iq}"""
    return mensaje

#stark3--------------------------------------------------------------------------------------------------------------------------------

def stark_normalizar_dato(lista : list):
    contador_modific = 0
    bandera_normalizar = False
    if bandera_normalizar == False:
        if len(lista) > 0:
            for personaje in lista:
                if type(personaje["peso"]) != float:
                    bandera_normalizar = True
                    personaje["peso"] = float(personaje["peso"])
                    contador_modific += 1
                if type(personaje["altura"]) != float:
                    bandera_normalizar = True
                    personaje["altura"] = float(personaje["altura"])
                    contador_modific += 1
                if type(personaje["peso"]) != int:
                    bandera_normalizar = True
                    personaje["fuerza"] = int(personaje["fuerza"])
                    contador_modific += 1
    
    if contador_modific > 0:
        print("Datos Normalizados")
        return True
    else:
        print("Hubo un error al normalizar los datos. Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente")
        return False

def obtener_dato(dicc : dict, key : str) -> str:
    if len(dicc) > 0 and key == "nombre":
        mensaje = f"""Nombre: {dicc[key]}"""
        return mensaje
    else:
        return False

def obtener_nombre_y_dato(dicc : dict, key : str) -> str:
    if len(dicc) != 0:
        mensaje = f"Nombre : {dicc['nombre']} | {key} : {dicc[key]}"
        return mensaje
    else:
        return False

def obtener_max(lista : list, key : str) -> dict:
    personaje_max = lista[0]
    if len(lista) != 0:
        for personaje in lista:
            if personaje_max[key] < personaje[key]:
                personaje_max = personaje
        return personaje_max
    else:
        return False

def obtener_min(lista : list, key : str) -> dict:
    personaje_min = lista[0]
    if len(lista) != 0:
        for personaje in lista:
            if personaje_min[key] > personaje[key]:
                personaje_min = personaje
        return personaje_min
    else:
        return False

def obtener_dato_cantidad(lista : list, min_max : str, key : str) -> dict:
    if min_max.upper() == "MAX":
        personaje_max = obtener_max(lista, key)
        return personaje_max
    elif min_max.upper() == "MIN":
        personaje_min = obtener_min(lista, key)
        return personaje_min
    else:
        return False

def stark_imprimir_heroes(lista : list) -> str:
    if len(lista) != 0:
        for personaje in lista:
            print(obtener_dato(personaje, "nombre"))
    else:
        return False

def sumar_dato_heroe(lista : list, key : str) -> int or float:
    acumulador_personaje = 0
    if len(lista) != 0:
        for personaje in lista:
            if type(personaje) == dict and len(personaje) != 0:
                acumulador_personaje = acumulador_personaje + personaje[key]
        return acumulador_personaje
    else:
        return False

def dividir(dividendo : int, divisor : int) -> int:
    if divisor == 0:
        return False
    else:
        resultado = dividendo / divisor
        return resultado

def calcular_promedio(lista : list, key : str) -> int:
    acumulador_personaje = sumar_dato_heroe(lista, key)
    cantidad_elementos = len(lista)
    promedio = dividir(acumulador_personaje, cantidad_elementos)
    return promedio

def mostrar_promedio_dato(lista : list, key : str) -> str:
    if len(lista) == 0:
        if type(lista[0][key]) == int or type(lista[0][key]) == float:
            promedio = calcular_promedio(lista, key)
            mensaje = f"el promedio es {promedio}"
            return mensaje
        else:
            return False
    else:
        return False

def lista_gen(lista : list, gen : str) -> list:
    lista_fem = []
    for personaje in lista:
        if personaje["genero"].upper() == gen.upper():
            lista_fem.append(personaje)
    return lista_fem

def agrupar_por_(lista : list, key : str):
    diccionario_perso = {}
    for personaje in lista:
        caracteristica = personaje.get(key, "Otro")
        nombre = personaje.get("nombre")
        diccionario_perso.setdefault(caracteristica, []).append(nombre)
    return diccionario_perso

def imprimir_menu():
    menu = """1. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB
            2. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
            3. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
            4. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
            5. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
            6. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB
            7. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
            8. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
            9. Listar todos los superhéroes agrupados por color de ojos.
            10. Listar todos los superhéroes agrupados por tipo de inteligencia.
            11. Normalizar datos.
            0. SALIR
            """
    imprimir(menu)

def validar_entero(str : str):
    num = int(str)
    if num >= 0 or num <= 0:
        return num
    else:
        return False

def stark_menu_principal() -> int:
    imprimir_menu()
    num = input("Cual va a ser su opcion?: ")
    opcion = validar_entero(num)
    return opcion

def stark_marvel_app(lista : list):
    datos_normalizados = False
    while True:
        opcion = stark_menu_principal()
        match opcion:
            case 0:
                break
            case 11:
                if datos_normalizados == False:
                    datos_normalizados = stark_normalizar_dato(lista)
            case 1:
                mostrar_perso_gen(lista, "NB", "genero")
            case 2:
                imprimir(obtener_dato(obtener_max(lista_gen(lista, "F"), "altura"), "nombre"))
            case 3:
                imprimir(obtener_dato(obtener_max(lista_gen(lista, "M"), "altura"), "nombre"))
            case 4:
                imprimir(obtener_dato(obtener_min(lista_gen(lista, "M"), "fuerza"), "nombre"))
            case 5:
                imprimir(obtener_dato(obtener_min(lista_gen(lista, "NB"), "fuerza"), "nombre"))
            case 6:
                imprimir(calcular_promedio(lista_gen(lista, "NB"), "fuerza"))
            case 7:
                imprimir(agrupar_por_(lista, "color_ojos"))
            case 8:
                imprimir(agrupar_por_(lista, "color_pelo"))
            case 9:
                imprimir(agrupar_por_(lista, "color_ojos"))
            case 10:
                imprimir(agrupar_por_(lista, "inteligencia"))

#stark4 --------------------------------------------------------------------------------------------------------------------------------------------------------

def extraer_iniciales(nombre_personaje : str) -> str:
    lista_nombre = re.split(" ", nombre_personaje)
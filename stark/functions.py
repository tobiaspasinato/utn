def imprimir(all : any):
    print(all)

def normalizar_dato(lista : list):
    for personaje in lista:
        personaje["peso"] = float(personaje["peso"])
        personaje["altura"] = float(personaje["altura"])
        personaje["fuerza"] = float(personaje["fuerza"])
    
    return lista


def recorrer_lista(lista : list):
    for personaje in lista:
        imprimir(f"""personaje:
                Nombre: {personaje["nombre"]}
                Identidad: {personaje["identidad"]}
                Empresa: {personaje["empresa"]}
                Altura: {personaje["altura"]}
                Peso: {personaje["peso"]}
                Genero: {personaje["genero"]}
                Color de ojos: {personaje["color_ojos"]}
                Color de Pelo: {personaje["color_pelo"]}
                Fuerza: {personaje["fuerza"]}
                Inteligencia: {personaje["inteligencia"]}""")

def fuerza_max(lista : list):
    personaje_mas_fuerte = lista[0]
    for personaje in lista:
        if personaje_mas_fuerte["fuerza"] < personaje["fuerza"]:
            personaje_mas_fuerte = personaje
    
    mensaje = f"""Personaje:
            Identidad: {personaje_mas_fuerte["identidad"]}
            Peso: {personaje_mas_fuerte["peso"]}"""
    
    return mensaje

def mas_bajo(lista : list):
    personaje_mas_bajo = lista[0]
    for personaje in lista:
        if personaje_mas_bajo["altura"] > personaje["altura"]:
            personaje_mas_bajo = personaje
    
    mensaje = f"""Personaje:
            Identidad: {personaje_mas_bajo["identidad"]}
            Peso: {personaje_mas_bajo["nombre"]}"""
    
    return mensaje

def peso_promedio_masculino(lista : list):
    acumulador_peso = 0
    acumulador_perso_masculinos = 0

    for personaje in lista:
        if personaje["genero"] == "M":
            acumulador_peso = acumulador_peso + personaje["peso"]
            acumulador_perso_masculinos += 1
    
    resultado = acumulador_peso / acumulador_perso_masculinos
    mensaje = f"Peso promedio de los personajes masculinos: {resultado}"
    return resultado

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
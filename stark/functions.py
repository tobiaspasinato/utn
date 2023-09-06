def imprimir(all : any):
    print(all)

def normalizar_dato(lista : list):
    for personaje in lista:
        personaje["peso"] = float(personaje["peso"])
        personaje["altura"] = float(personaje["altura"])
        personaje["fuerza"] = float(personaje["fuerza"])
    
    return lista

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





# def fuerza_max(lista : list):
#     personaje_mas_fuerte = lista[0]
#     for personaje in lista:
#         if personaje_mas_fuerte["fuerza"] < personaje["fuerza"]:
#             personaje_mas_fuerte = personaje
    
#     mensaje = f"""Personaje:
#             Identidad: {personaje_mas_fuerte["identidad"]}
#             Peso: {personaje_mas_fuerte["peso"]}"""
    
#     return mensaje

# def mas_bajo(lista : list):
#     personaje_mas_bajo = lista[0]
#     for personaje in lista:
#         if personaje_mas_bajo["altura"] > personaje["altura"]:
#             personaje_mas_bajo = personaje
    
#     mensaje = f"""Personaje:
#             Identidad: {personaje_mas_bajo["identidad"]}
#             Peso: {personaje_mas_bajo["nombre"]}"""
    
#     return mensaje
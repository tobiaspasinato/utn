def imprimir(all : any):
    print(all)

def normalizar_dato(lista:list):
    for personaje in lista:
        personaje["peso"] = float(personaje["peso"])
        personaje["altura"] = float(personaje["altura"])
    
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
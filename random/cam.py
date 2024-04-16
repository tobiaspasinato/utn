"""
def muestra_vocales(palabra : str) -> str:
    palabra = palabra.lower()
    mensaje = ""
    for letra in palabra:
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
            mensaje = mensaje + f"{letra} "
    return mensaje

word = input("Ingrese una palabra para mostrar sus vocales: ")
print(muestra_vocales(word))
"""
#Hacer una función que reciba un string y que lo invierta.
def invertir_palabra(palabra):
    nueva_palabra = ""
    longitud = len(palabra)
    for numero in range(1,longitud+1):
        nueva_palabra = nueva_palabra + palabra[-numero]
    return nueva_palabra

word = "padre"
print(invertir_palabra(word))
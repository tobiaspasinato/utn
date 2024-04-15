
"""
jugada_usuario = input("Elegi una jugada(T para tijera, R para piedra, P para papel): ")
jugada_usuario = jugada_usuario.lower()
if jugada_usuario == "t" or jugada_usuario == "r" or jugada_usuario == "p" or jugada_usuario == "goku":
    match jugada_usuario:
        case "t":
            print("Te gane elegi R (Piedra)")
        case "r":
            print("Te gane elegi P (Papel)")
        case "p":
            print("Te gane elegi T (Tijera)")
        case "goku":
            print("Perdi, nada le gana a Goku")
else:
    print("Eso no es una jugada valida")
"""
def get_primo(num):
    x = 1
    c = 0
    while x <= num:
        if num % x == 0:
            c += 1
        x += 1
    if c == 2:
        return True
    else:
        return False

rango = int(input("Cual es el rango de numero primos que queres mostrar? "))

for i in range(1, rango):
    if get_primo(i) == True:
        print(i)
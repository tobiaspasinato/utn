lista_num = [82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]
posi_list = 0
for numero in lista_num:
    posi_list += 1
    for numero2 in lista_num[posi_list]:
        if numero2 == numero:
            print(numero)

producto1 = ("pollo", 600)
producto2 = ("carne", 500)
producto3 = ("queso", 200)
producto4 = ("pan", 300)
lista_productos = [producto1, producto2, producto3, producto4]

def tomar_pedido(lista : list) -> list:
    on = True
    lista_compra = []
    while on:
        eleccion = int(input("¿Qué desea comprar? (1 para detergente, 2 para jabon, 3 para esponja y 4 para trapo); 5 para salir "))
        if eleccion == 5:
            on = False
        elif eleccion == 1:
            var1 = lista_productos[0]
            var2 = var1[1]
            lista_compra.append(int(var2))
        elif eleccion == 2:
            var1 = lista_productos[1]
            var2 = var1[1]
            lista_compra.append(int(var2))
        elif eleccion == 3:
            var1 = lista_productos[2]
            var2 = var1[1]
            lista_compra.append(int(var2))
        elif eleccion == 4:
            var1 = lista_productos[3]
            var2 = var1[1]
            lista_compra.append(int(var2))
    return lista_compra

def calcular_precio(lista : list) -> int:
    acumulador_precio = 0
    for i in lista:
        acumulador_precio = acumulador_precio + i
    return acumulador_precio

print(f"El precio total es de {calcular_precio(tomar_pedido(lista_productos))}")
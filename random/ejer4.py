edad = int(input("cual es tu edad? "))
estado_civil = input("cual es tu estado civil? ")

if edad < 18 and estado_civil != "soltero":
    print("Es muy pequeño para NO ser soltero.")
else:
    print("Todo bien")
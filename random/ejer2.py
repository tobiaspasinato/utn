edad = int(input("Cual es tu edad? "))

if edad > 17:
    print("Sos mayor de edad")
else:
    if edad < 18 and edad > 12:
        print("Sos un adolescente")
    else:
        if edad < 13:
            print("Sos un niño")
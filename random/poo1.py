class persona:
    def __init__(self, id, nombre, apellido, edad) -> None:
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def mostrar(self) -> str:
        mensaje = f"Nombre: {self.nombre} | Apellido: {self.apellido}\nEdad: {self.edad}\nDNI: {self.id}"
        return mensaje

name = input("Cual es tu nombre? ")
lastname = input("Cual es tu apellido? ")
age = int(input("Cual es tu edad? "))
dni = int(input("Cual es tu dni? "))

persona_one = persona(dni, name, lastname, age)

print(persona_one.mostrar())
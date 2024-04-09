class Libro:
    def __init__(self, titulo, autor, año_publicacion) -> None:
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
    
    def mostrar(self) -> str:
        mensaje = f"Libro : {self.titulo}\nAutor: {self.autor}\nAño de publicación: {self.año_publicacion}"
        return mensaje

title = input("Titulo del libro? ")
author = input("Cual es el autor? ")
year = input("Cual es el año de publicación? ")

libro_A = Libro(title, author, year)

print(libro_A.mostrar())
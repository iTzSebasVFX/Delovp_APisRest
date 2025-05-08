class Libro:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo;
        self.autor = autor;
        self.año = año;
    
    def mostrarLibros(self):
        return f"El libro ingresado es: {self.titulo}, creado por: {self.autor} en el año: {self.año}";
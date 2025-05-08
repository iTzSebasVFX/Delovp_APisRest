class Users():
    def __init__(self, nombre, contrasena):
        self.nombre = nombre;
        self.contrasena = contrasena;
        
    def __str__(self):
        return self.nombre
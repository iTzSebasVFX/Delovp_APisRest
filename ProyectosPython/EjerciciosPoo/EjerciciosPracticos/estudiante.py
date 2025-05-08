class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre;
        self.edad = edad;
    

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad);
        self.__carrera = carrera;
        
    def mostrarEstudiante(self):
        """El return solamente enviara la información, para mostralos necesitaremos realizar un print(), puede ser en la clase o en el codigo"""
        return f"Bienvenido estudiante: {self.nombre}, con edad {self.edad}, su carrera a desempeñar es {self.__carrera}" 
    # Carrera se enviara aunque sea privada, ya que esta dentro de un metodo de envio de datos.
        
        
    
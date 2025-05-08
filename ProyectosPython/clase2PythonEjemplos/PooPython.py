# Ejemplo de los 4 pilares de la Programación Orientada a Objetos (POO)
        
# Palabras clave:
#class : Define una clase.
# __init__ : Método constructor que se llama al crear una instancia de la clase.
# self : Referencia a la instancia actual de la clase.
# super() : Llama a un método de la clase padre.
# __atributo : Atributo que no debe ser accedido directamente desde fuera de la clase.

# Crear clase persona con atributos nombre y edad, y un método para mostrar la información.
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre;
        self.edad = edad;
        
    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.";
    
# Crear un objeto, es decir, una instancia de la clase Persona.
persona1 = Persona("Juan", 30);
print(persona1.saludar());

# Paradigmas - 1 Encapsulamiento: Ocultamos detalles internos y controlamos el acceso a los atributos.
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular;
        self.__saldo = saldo; # atributos privados
        
    def mostrar_saldo(self):
        print(f"Saldo de {self.__titular}: ${self.__saldo}");
        
    def depositar(self, cantidad):
        if (cantidad > 0):
            self.__saldo += cantidad;
        
# Instanciamos
cuenta = CuentaBancaria("Wilson", 1000);
cuenta.depositar(500);
cuenta.mostrar_saldo(); # Al ser privados los atributos se muestran los datos por medio de metodos getter.
# print(cuenta.__saldo) # Esto daria error

# Paradigma - 2 Herencia: # Una clase hija hereda atributos y métodos de una clase padre.
class Empleado(Persona):
    def __init__(self, nombre, edad, cargo):
        super().__init__(nombre, edad);
        self.cargo = cargo;

    def presentar(self):
        print(f"La persona {self.nombre}, tiene una edad de {self.edad} y su cargo es {self.cargo}");

persona1 = Empleado("Juan", 18, "Administrador de baños");
persona1.presentar();

# Paradigma - 3 Abstracción: # Representamos un concepto del mundo real como una clase.
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"
    
    # 4. Polimorfismo
# Diferentes clases pueden implementar el mismo método de diferentes maneras.
class Ave:
    def hacer_sonido(self):
        return "Canto genérico"

class Perro:
    def hacer_sonido(self):
        return "Ladrido"

# Uso de los conceptos
if __name__ == "__main__":
    # Herencia
    emp1 = Empleado("Juan", 18, "Ingeniero")
    print(emp1.presentar())
    
    # Abstracción
    vehiculo = Vehiculo("Toyota", "Corolla")
    print(vehiculo.mostrar_info())

    # Encapsulamiento
    cuenta = CuentaBancaria("Juan", 1000)
    cuenta.depositar(500)
    cuenta.retirar(300)
    print(cuenta.mostrar_saldo())

    # Polimorfismo
    animales = [Ave(), Perro()]
    for animal in animales:
        print(animal.hacer_sonido())
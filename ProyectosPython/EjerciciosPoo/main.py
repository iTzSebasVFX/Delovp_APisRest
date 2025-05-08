from EjerciciosPracticos.estudiante import Estudiante as est
from EjerciciosPracticos.rectangulo import Rectangulo as rec
from EjerciciosPracticos.libros import Libro as lib

est1 = est("Juan", 20, "Analisis y desarrollo de software");
print(est1.mostrarEstudiante());

rect1 = rec();
print(rect1.areaRectangulo(20,3.5));
print(rect1.perimetroRectangulo(20,50));

lib1 = lib("Frankenstein", "Marry Shelley", 1818);
print(lib1.mostrarLibros());
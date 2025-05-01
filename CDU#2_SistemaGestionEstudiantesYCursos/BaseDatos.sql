--Creamos La base de datos--
CREATE DATABASE GestionEstYCur;
go

--Usamos la base de datos--
USE GestionEstYCur

--Para este caso de uso necesitaremos dos tablas las cuales seran relacionales--
--Tabla Cursos
CREATE TABLE Cursos(
	id INT IDENTITY(1,1) PRIMARY KEY,
	nombre VARCHAR(100) NOT NULL,
	descripcion TEXT NOT NULL,
	cantidadCreditos INT NOT NULL,
);
GO
--Tabla Estudiante
CREATE TABLE Estudiante(
	id INT IDENTITY(1,1) PRIMARY KEY,
	nombre VARCHAR(100) NOT NULL,
	correoElectronico VARCHAR(100) NOT NULL,
	cursoId INT NOT NULL,
	FOREIGN KEY (cursoId) REFERENCES Cursos(id)
);
GO

--Insertamos cursos por defecto--
INSERT INTO Cursos (nombre, descripcion, cantidadCreditos) VALUES
('Programación I', 'Introducción a la programación estructurada utilizando C# y resolución de problemas básicos.', 4),
('Bases de Datos', 'Fundamentos de bases de datos relacionales, modelado, consultas SQL y normalización.', 3),
('Matemáticas Discretas', 'Lógica matemática, teoría de conjuntos, relaciones y funciones aplicadas a la informática.', 3),
('Estructura de Datos', 'Uso de listas, pilas, colas, árboles y algoritmos para manipular estructuras dinámicas.', 4),
('Sistemas Operativos', 'Estudio del funcionamiento interno de sistemas operativos, procesos, memoria y archivos.', 3),
('Redes de Computadores', 'Principios de redes, modelos OSI/TCP-IP, protocolos y configuración básica.', 3),
('Desarrollo Web', 'Creación de sitios web usando HTML, CSS, JavaScript y conceptos básicos de backend.', 3),
('Ingeniería de Software', 'Ciclo de vida del software, análisis, diseño, pruebas y documentación.', 4),
('Fundamentos de Hardware', 'Componentes físicos del computador, mantenimiento y ensamblaje.', 2),
('Algoritmos y Lógica', 'Diseño de algoritmos eficientes, lógica computacional y resolución de problemas.', 3);


--Prueba de insercion de estudiantes--
INSERT INTO Estudiante (nombre, correoElectronico, cursoId) VALUES ('Yeferson', 'fefe@gmail.com', '3');

--Realizamos un select para ver que se hayan creado exitosamente las tablas--
SELECT * FROM Cursos;
SELECT * FROM Estudiante;
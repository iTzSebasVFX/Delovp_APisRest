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
('Programaci�n I', 'Introducci�n a la programaci�n estructurada utilizando C# y resoluci�n de problemas b�sicos.', 4),
('Bases de Datos', 'Fundamentos de bases de datos relacionales, modelado, consultas SQL y normalizaci�n.', 3),
('Matem�ticas Discretas', 'L�gica matem�tica, teor�a de conjuntos, relaciones y funciones aplicadas a la inform�tica.', 3),
('Estructura de Datos', 'Uso de listas, pilas, colas, �rboles y algoritmos para manipular estructuras din�micas.', 4),
('Sistemas Operativos', 'Estudio del funcionamiento interno de sistemas operativos, procesos, memoria y archivos.', 3),
('Redes de Computadores', 'Principios de redes, modelos OSI/TCP-IP, protocolos y configuraci�n b�sica.', 3),
('Desarrollo Web', 'Creaci�n de sitios web usando HTML, CSS, JavaScript y conceptos b�sicos de backend.', 3),
('Ingenier�a de Software', 'Ciclo de vida del software, an�lisis, dise�o, pruebas y documentaci�n.', 4),
('Fundamentos de Hardware', 'Componentes f�sicos del computador, mantenimiento y ensamblaje.', 2),
('Algoritmos y L�gica', 'Dise�o de algoritmos eficientes, l�gica computacional y resoluci�n de problemas.', 3);


--Prueba de insercion de estudiantes--
INSERT INTO Estudiante (nombre, correoElectronico, cursoId) VALUES ('Yeferson', 'fefe@gmail.com', '3');

--Realizamos un select para ver que se hayan creado exitosamente las tablas--
SELECT * FROM Cursos;
SELECT * FROM Estudiante;
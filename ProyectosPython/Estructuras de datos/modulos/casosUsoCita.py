
from collections import deque, defaultdict, Counter
import mysql.connector

# Conexion
def conn():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="caso_uso_est_datos"
    )
    return conexion;

# Verifica conexión
con = conn();
if con.is_connected():
    print("Conexión exitosa a la base de datos");

# Caso de uso 1: Debe permitir crear y almacenar una nueva cita
def registrarCita(nombre, apellido, tipoDoc, numDoc, nomDoc, opcion):
    try:
        cursor = con.cursor();
        query = ("INSERT INTO `pacientes`(`nombre`, `apellido`, `tipoDoc`, `numDoc`, `nomDoc`, `opcion`) VALUES (%s,%s,%s,%s,%s,%s);")
        nuevaCita = (nombre, apellido, tipoDoc, numDoc, nomDoc, opcion);
        cursor.execute(query, nuevaCita);
        con.commit();
        cursor.close();
        con.close();
        print("Datos insertados correctamente")
    except mysql.connector.Error as e:
        print("Error, los datos no se pudieron insertar: ", e)

#Caso de uso 2: Debe permitir ver los tipos de documento más comunes y los tipos de cita más comunes
def docCommons():
    pacientes = mostrar();
    print(pacientes);
    docComun = [];
    for item in pacientes:
        docComun.append(item[2]);
    contador = Counter(docComun);
    print(contador);
    return contador;

def citaCommons():
    pacientes = mostrar();
    print(pacientes);
    citaComun = [];
    for item2 in pacientes:
        citaComun.append(item2[5]);
    contador2 = Counter(citaComun);
    print(contador2.values());
    return contador2;

# Caso de uso 3: Mostrar pacientes agrupados por tipo de cita
def pacPorTipCita():
    pacientes = mostrar();
    pacientePorCita = defaultdict(list);
    for item in pacientes:
        pacientePorCita[item[5]].append(item[0])
        # En la lista de defaultdic creamos un clave con el tipo de cita y le damos de valor el nombre y el apellido
        # En defaultdict la claves que se crean son unica, entonces si la lista encuentra una clave igual, simplemente le asignara el valor a la clave ya existente
    print(pacientePorCita)
    return pacientePorCita;

# enviar lista
def mostrar():
    try:
        cursor = con.cursor();
        query = ("SELECT nombre, apellido, tipoDoc, numDoc, nomDoc, opcion FROM `pacientes`");
        cursor.execute(query);
        pacientes = cursor.fetchall();
        cursor.close;
        con.close
        print(pacientes);
        return pacientes;
    except mysql.connector.Error as e:
        print("Error en la busqueda", e);
        return e;
    
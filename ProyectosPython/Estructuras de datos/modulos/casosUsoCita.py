from collections import deque, defaultdict, Counter

citas = deque();

# Caso de uso 1: Debe permitir crear y almacenar una nueva cita
def registrarCita(nombre, apellido, tipoDoc, numDoc, nomDoc, opcion):
    nuevaCita = [nombre, apellido, tipoDoc, numDoc, nomDoc, opcion];
    citas.append(nuevaCita)

#Caso de uso 2: Debe permitir ver los tipos de documento más comunes y los tipos de cita más comunes
def docCommons():
    docComun = [];
    for item in citas:
        docComun.append(item[2]);
    contador = Counter(docComun);
    print(contador);
    return contador;

def citaCommons():
    citaComun = [];
    for item2 in citas:
        citaComun.append(item2[5]);
    contador2 = Counter(citaComun);
    print(contador2);
    return contador2;

# Caso de uso 3: Mostrar pacientes agrupados por tipo de cita
def pacPorTipCita():
    pacientePorCita = defaultdict(list);
    for item in citas:
        pacientePorCita[item[5]].append(item[0])
        # En la lista de defaultdic creamos un clave con el tipo de cita y le damos de valor el nombre y el apellido
        # En defaultdict la claves que se crean son unica, entonces si la lista encuentra una clave igual, simplemente le asignara el valor a la clave ya existente
    print(pacientePorCita)
    return pacientePorCita;

# enviar lista
def mostrar():
    return citas;
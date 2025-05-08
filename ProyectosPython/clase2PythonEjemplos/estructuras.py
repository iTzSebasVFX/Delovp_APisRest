# Libreria para el manejo de fechas
from datetime import date, datetime, timedelta

print("Hello world, desde el archivo estructuras.py");

#manejo de variables
nombre = "Wilson";
edad = 30;
estatura = 1.75;
print(f"Su nombre: {nombre}, Su edad {edad} y su estatura {estatura}");

# conversion de tipos
edad_str = "30";
edad_int = int(edad_str);
f = float(57);
x = bool(edad_int);
print(edad_int + 5, f, x);

# manejo de fechas
fecha_hoy = date.today();
fecha_hora_actual = datetime.now();
cumpleaños = date(1990, 4, 15);
mañana = date.today() + timedelta(days=1);
dias_transcurridos = (fecha_hoy - date(2025, 1, 1)).days;
print(dias_transcurridos);

# manejo de booleans e if-else
es_mayor_de_edad = True;
tiene_licencia = False;
if es_mayor_de_edad and tiene_licencia:
    print("Puedes conducir");
else:
    print("No puede conducir");
    
# manejo de rangos 
nota = 85 ;
if nota >= 90:
    print("exelente");
elif nota >= 70:
    print("bien");
else: 
    print("nota mala");

#simulacion de casos 
opccion = 0 ;
if opccion ==1:
    print("opccion1");
elif opccion == 2:
    print("opccion 2");
else: 
    print("error");
    
# simulación de casos con diccionario
def opcion1():
    return "opcion 1";
def opcion2():
    return "opcion 2";
switch = {1: opcion1, 2: opcion2};
# lambda: "Opcion no valida" (es decir, una función anónima que al ejecutarse devuelve esa cadena).
resultado = switch.get(2, lambda: "Opcion no valida");
print(resultado);

# Bucles (for y while)
# Bucle for tradicional:
for i in range (1, 6):
    print(i);
    
# Bucle while tradicional:
contador = 3;
while contador > 0:
    print(contador);
    contador -= 1;

# Simulacion bucle do while:
while True:
    numero = int(input("ingresa un numero mayor que 0: "));
    if numero > 0:
        break;

# bucle tipo forech con lista y diccionario 
animales = ["gato", "perro", "conejo"];
for animal in animales: 
    print(animal);
persona = {"persona": "wilson", "edad": 30};
for clave, valor in persona.items():
    print(f"{clave} and {valor}");
    

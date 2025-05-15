from collections import deque, defaultdict, Counter

citas = deque([
    ["Juan Sebastian", "Quiceno", "C.C", 1247812, "Dr. Dwyne Jhonson", "general"],
    ["Jk", "Smith", "C.C", 1017927075, "Dr. Karl Jhonson", "odontologica"],
    ["Juan Sebastian", "Quiceno", "C.C", 127819237, "Dr. Dwyne Jhonson", "pediatra"],
    ["Lex Luthor", "Garden", "C.C", 124123124, "Dr. Karl Jhonson", "odontologica"]
])
# print(citas);

# Caso de uso 1: Debe permitir crear y almacenar una nueva cita
# while True:
#     print("Ingresa el tipo de citas que necesitas 1.general 2.odontologica 3.pediatra 4.especilidad, 0.Para salir")
#     print("------------------------------------------------------------------------------------------")
#     opccion = int(input())  
#     if (opccion == 1):
#         opccion = "General"
#         nombre = input("Ingresa tu nombre \n")
#         apellido = input("Ingrese el apellido\n")
#         tipo_documento = input("tipo de documento: T.I O C.C")
#         Numero_documento = int(input(f"ingrese el numero de documento:"))
#         N_doctor = input("Ingrese el nombre del doctor")
#         citas.append([nombre,apellido,tipo_documento, Numero_documento,N_doctor,opccion])
    
#     elif (opccion == 2):
#         opccion = "odontologica"
#         nombre = input("Ingresa tu nombre \n")
#         apellido = input("Ingrese el apellido\n")
#         tipo_documento = input("tipo de documento: T.I O C.C")
#         Numero_documento = int(input(f"ingrese el numero de documento:"))
#         N_doctor = input("Ingrese el nombre del doctor")
#         citas.append([nombre,apellido,tipo_documento, Numero_documento,N_doctor,opccion])
    
        
#     elif (opccion == 3):
#         opccion = "pediatra"
#         nombre = input("Ingresa tu nombre \n")
#         apellido = input("Ingrese el apellido\n")
#         tipo_documento = input("tipo de documento: T.I O C.C")
#         Numero_documento = int(input(f"ingrese el numero de documento:"))
#         N_doctor = input("Ingrese el nombre del doctor")
#         citas.append([nombre,apellido,tipo_documento, Numero_documento,N_doctor,opccion])

        
#     elif( opccion == 4):
#         opccion = "especilidad"
#         nombre = input("Ingresa tu nombre \n")
#         apellido = input("Ingrese el apellido\n")
#         tipo_documento = input("tipo de documento: T.I O C.C")
#         Numero_documento = int(input(f"ingrese el numero de documento:"))
#         N_doctor = input("Ingrese el nombre del doctor")
#         citas.append([nombre,apellido,tipo_documento, Numero_documento,N_doctor,opccion])
    
#     elif (opccion == 0):
#         print("saliste del programa")
#         break
#     else:
#         print("error")
        
# print (citas)

# Caso de uso 2: Debe permitir ver los tipos de documento más comunes y los tipos de cita más comunes

# docComun = [];
# for cita in citas:
#     docComun.append(cita[2])
    
# print("Los tipos de citas más comunes son: ",Counter(docComun))
# print("........................................")

# Agrupar pacientes por tipo de cita y contar frecuencias
# AgruparPorTipo = defaultdict(list)
# tipoCita = []

# for cita in citas:
#     tipo = cita[5].lower()  # para evitar errores por mayúsculas
#     tipoCita.append(tipo)
#     AgruparPorTipo[tipo].append(cita[1])  # cita[1] = apellido

# # Caso de uso 2: Mostrar tipos de cita más comunes
# print("Tipos de citas más comunes:")
# for tipo, cantidad in Counter(tipoCita).most_common():
#     print(f"{tipo}: {cantidad}")

# # Caso de uso 3: Mostrar pacientes agrupados por tipo de cita
# print("Pacientes por tipo de cita:")
# for tipo, pacientes in AgruparPorTipo.items():
#     print(f"{tipo}: {pacientes}")
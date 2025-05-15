#se crea un archivo modulos.py 
#y se crean las funciones sumar multiplicar dividir

#nombre del paquete          importamos especificamente lo que necesitamos de el paquete

from my_paquet.operacion_texto import  suma, multiplicacion, divicion, frase
# import * hace que llama todo 

print(frase)
while True:
    print("por favor ingrese la opcion 1: suma o 2: multipliciacion 3: divicion o igresa 0 para salir")
    opccion = (input())
    if (opccion == "1"):
        print("ingresa la suma que quieras hacer")
        num1 = int(input("Ingresa el primer número: "))
        num2 = int(input("Ingresa el segundo número: "))
        print("La suma es:", suma(num1, num2))
    
    elif(opccion == "2"):
    
        num3 = int(input("Ingresa el primer número: "))
        num4 = int(input("Ingresa el segundo número: "))
        print("la multiplicacion es:",multiplicacion(num3,num4))
    elif (opccion == "3"):
        
        num5 = int (input("ingrese el primer numero"))
        num6 = int(input("Ingresa el segundo número: "))
        print("la multiplicacion es:",divicion(num5,num6))

        
    elif (opccion == "0"):
        print("saliste del programa")
        break
    else:
        print("error")
        break  
        
        
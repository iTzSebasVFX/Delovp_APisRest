# crear un programa que pida al usuario su nombre y edad y le diga si puede votar (mayor de 18)
print("porfavor ingrese su nombre");
nombre = input();
print("Porfavor ingrese su edad");
edad = int(input());

if (edad >= 18):
    print(f"el usuario: {nombre} tiene la edad: {edad}, suficiente para votar");
else:
    print(f"el usuario: {nombre} tiene la edad: {edad}, no es suficiente para votar");
    
# Cajero automatico
saldo = 300000;
print(f"señor usuario usted tiene de saldo: {saldo}");
print(f"desea retirar dinero de su saldo monetario??, 1 para si 0 para no");
respuesta = int(input());
while True:
    if (respuesta == 1):
        print("ingrese la cantidad que desea retirar");
        cantidad = int(input());
        total = saldo - cantidad;
        print(f"usted ha retirado exitosamente {cantidad}, su saldo ha quedado en {total}");
        if (total == 0):
            print("Usted ya no tiene mas saldo, muchas gracias");
            break;
        else:
            print("Desea seguir retirando dinero");
            resp1 = int(input())
            if (resp1 == 0):
                break;
    else:
        break;
        
# Crear programa que almacene y permita buscar frutas
Frutas: list = ["Banano", "Manzana"];
while True:
    print("ingrese la fruta que desea buscar");
    buscarFruit = input();
    if (Frutas.__contains__(buscarFruit)):
        print("Fruta encontrada exitosamente");
    else:
        print("Perdonde esta fruta no se encuentra, pero tenemos estas:");
        print(Frutas);
        print("desea ingresar la fruta " + buscarFruit + "? 1 pa si 0 pa no");
        resp = int(input());
        if (resp == 1):
            Frutas.append(buscarFruit);
            print("Fruta agregada correctamente");
            print(Frutas);
            print("desea buscar otra fruta?? 1 pa si 0 pa no");
            resp = int(input());
            if (resp == 0):
                break;

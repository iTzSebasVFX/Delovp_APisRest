""" Ejemplo de Modulo y Paquetes de Python """
import matplotlib.pyplot as plt

def EstadisticasPersonales():
    x = ["Salud", "Economia", "Fisico"];
    y = []
    count = 0;

    print("Ingrese su nombre");
    nombre = input();

    while True:
        if (count > 2):
            break;
        print(f"Ingrese dato numerico para {x[count]}");
        cantidad = int(input());
        count += 1;
        y.append(cantidad);
        
    print(y);

    plt.plot(x, y);
    plt.title(f"Estadisticas personales {nombre}");
    plt.xlabel("Campos");
    plt.ylabel("Cantidad");
    plt.show();

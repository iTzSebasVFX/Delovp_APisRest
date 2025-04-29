// See https://aka.ms/new-console-template for more information
using System.Collections.Concurrent;
using System.ComponentModel.DataAnnotations;

class Program
{
    public static void Main(string[] args)
    {
        Console.WriteLine("Gestor de Productos");
        Console.WriteLine("Bienvenido a su aplicacion de gestion de productos");
        GestorProducto gestorProducto = new GestorProducto();

        // Agregar productos
        Console.WriteLine("Ingrese el Id del producto:");
        int id = int.Parse(Console.ReadLine() ?? "0");
        Console.WriteLine("Ingrese el Nombre del producto");
        string nombre = Console.ReadLine() ?? string.Empty;
        Console.WriteLine("Ingrese la Descripción del producto");
        string descripcion = Console.ReadLine() ?? string.Empty;
        Console.WriteLine("Ingrese el precio del producto");
        decimal precio = decimal.Parse(Console.ReadLine() ?? "0.0m");
        Console.WriteLine("Ingrese la cantidad de prodcutos");
        int cantidad = int.Parse(Console.ReadLine() ?? "0");

        gestorProducto.AgregarProducto(new Producto { Id = id, Nombre = nombre, Descripcion = descripcion, Precio = precio, Cantidad = cantidad });

        // Mostrar Productos
        gestorProducto.MostrarProductos();

        // Actulizar Productos
        Console.WriteLine("Desea actualizar algun producto??");
        string respuesta = Console.ReadLine() ?? string.Empty;
        if (respuesta == "si")
        {
            Console.WriteLine("Ingrese el id del producto que desea actualizar");
            id = int.Parse(Console.ReadLine() ?? "0");

            gestorProducto.ActualizarProducto(id);
        }
        else
        {
            Console.WriteLine("No se actualizaron productos.");
        }

        // Eliminar Productos
        Console.WriteLine("Desea eliminar algun producto??");
        respuesta = Console.ReadLine() ?? string.Empty;
        if (respuesta == "si")
        {
            Console.WriteLine("Ingrese el id del producto que desea eliminar");
            id = int.Parse(Console.ReadLine() ?? "0");
            gestorProducto.EliminarProducto(id);
            Console.WriteLine("Producto eliminado correctamente.");
            gestorProducto.MostrarProductos();
        }
        else
        {
            Console.WriteLine("No se eliminaron productos.");
        }
    }
}

public class Producto
{
    [Key]
    public int Id { get; set; }
    public string Nombre { get; set; } = string.Empty;
    public string Descripcion { get; set; } = string.Empty;
    public decimal Precio { get; set; } = 0.0m;
    public int Cantidad { get; set; }
}

public class GestorProducto()
{
    private List<Producto> productos = new List<Producto>();

    public void MostrarProductos() 
    {
        foreach (var producto in productos) 
        {
            Console.WriteLine($"Id = {producto.Id}, Nombre = {producto.Nombre}, Descripción = {producto.Descripcion}, Precio = {producto.Precio}, Cantidad = {producto.Cantidad}");
        }
    }

    public void AgregarProducto(Producto producto)
    {
        productos.Add(producto);
    }

    public void ActualizarProducto(int id)
    {
        var producto = productos.FirstOrDefault(p => p.Id == id);

        if (producto != null)
        {
            Console.WriteLine("Ingrese el nuevo Id del producto:");
            producto.Id = int.Parse(Console.ReadLine() ?? "0");
            Console.WriteLine("Ingrese el nuevo nombre del producto:");
            producto.Nombre = Console.ReadLine() ?? string.Empty;
            Console.WriteLine("Ingrese la nueva descripcion");
            producto.Descripcion = Console.ReadLine() ?? string.Empty;
            Console.WriteLine("Actualice el precio");
            producto.Precio = decimal.Parse(Console.ReadLine() ?? "0.0m");
            Console.WriteLine("Ingrese la cantidad");
            producto.Cantidad = int.Parse(Console.ReadLine() ?? "0");
            Console.WriteLine("Producto actualizado correctamente.");
            MostrarProductos();
            return;
        }
        else 
        {
            Console.WriteLine("Producto no encontrado.");
        }
    }

    public void EliminarProducto(int id)
    {
        var producto = productos.FirstOrDefault(p => p.Id == id);
        if (producto != null)
        {
            productos.Remove(producto);
        }
        else
        {
            Console.WriteLine("Producto no encontrado.");
        }
    }
}
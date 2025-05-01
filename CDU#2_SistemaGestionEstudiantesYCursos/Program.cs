// See https://aka.ms/new-console-template for more information
using System;
using System.Data.SqlClient;
class Program
{
    public static void Main(string[] args)
    {
        //Registro de nuevos alumnos
        Console.WriteLine("Registro de nuevos alumnos");
        Console.WriteLine("Ingrese el nombre del alumno:");
        string nombre = Console.ReadLine() ?? string.Empty;
        Console.WriteLine("Ingrese el Correo Electronico del alumno");
        string correo = Console.ReadLine() ?? string.Empty;
        Console.WriteLine("Se le presentaran los cursos disponibles");

        string connectionString = "Server=ITZSEBASVFXPC\\SQLEXPRESS;Database=GestionEstYCur;Trusted_Connection=True;";

        using (SqlConnection conn = new SqlConnection(connectionString))
        {
            try
            {
                conn.Open();
                string query = "SELECT * FROM Cursos";

                using (SqlCommand cmd = new SqlCommand(query, conn))
                using (SqlDataReader reader = cmd.ExecuteReader())
                {
                    Console.WriteLine("Cursos disponibles:");
                    Console.WriteLine("Id_Curso  /  Nombre_Curso");
                    while (reader.Read())
                    {
                        Console.WriteLine("- " + reader["id"] + "/" + reader["nombre"]);
                    }
                }
                Console.WriteLine("Ingrese el Id del curso del curso al que se desea inscribir");
                int idCurso = Convert.ToInt32(Console.ReadLine());
                string query2 = $"INSERT INTO Estudiante (nombre, correoElectronico, cursoId) VALUES ('{nombre}', '{correo}', '{idCurso}');";
                using (SqlCommand cmd2 = new SqlCommand(query2, conn))
                {
                    int rowsAffected = cmd2.ExecuteNonQuery();
                    if (rowsAffected > 0)
                    {
                        Console.WriteLine("Alumno registrado exitosamente.");
                        string query3 = "SELECT * FROM Estudiante";

                        using (SqlCommand cmd = new SqlCommand(query3, conn))
                        using (SqlDataReader reader = cmd.ExecuteReader())
                        {
                            Console.WriteLine("Estudiantes Registrados:");
                            Console.WriteLine("Id_Estudiante  /  Nombre_Estudiante  /  Id_Curso");
                            while (reader.Read())
                            {
                                Console.WriteLine("- " + reader["id"] + "  /  " + reader["nombre"] + "  /  " + reader["cursoId"]);
                            }
                        }
                    }
                    else
                    {
                        Console.WriteLine("Error al registrar el alumno.");
                    }
                }
                conn.Close();
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error: " + ex.Message);
            }
        }
    }
}
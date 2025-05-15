from flask import Flask, request, render_template, redirect, url_for  # pip install flask
import mysql.connector  # pip install mysql-connector-python

# Instancia de la app Flask
app = Flask(__name__)

# Configuración de conexión a MySQL (ojo con las mayúsculas/minúsculas)
db_config = {
    'host': 'localhost',     # era 'Host', debe ser en minúscula
    'user': 'root',
    'password': '',
    'database': 'flask_db'
}

# Ruta principal
@app.route('/')
def index():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre FROM personas")  
    personas = cursor.fetchall()  
    cursor.close()
    conn.close()
    return render_template('index.html', personas=personas)

# Ruta para agregar personas
@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO personas (nombre) VALUES (%s)", (nombre,))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('agregar.html')

# Ejecutar la app
if __name__ == '__main__':
    app.run(debug=True)  # era debug.True, debe ser debug=True

from collections import defaultdict
from flask import Flask, render_template, request# es una función en Flask que se utiliza para renderizar plantillas HTML utilizando el motor de plantillas Jinja2. Permite generar contenido HTML dinámico al combinar contenido estático con datos proporcionados por la aplicación Flask. 
from modulos import casosUsoCita

app = Flask(__name__);


@app.route("/")
def inicio():
    return render_template("index.html");

@app.route("/crearCitas")
def crearCitas():
    tipoCita = ("general", "odontologica", "pediatra", "especialidad")
    return render_template("crearCitas.html", tipoCita=tipoCita);

@app.route("/registrarCita", methods=["GET","POST"])
def registrar():
    if request.method == "POST":
        nombre = request.form["nombre"];
        apellido = request.form["apellido"];
        tipoDoc = request.form["tipoDoc"];
        numDoc = int(request.form["numDoc"]);
        nomDoc = request.form["doctor"];
        opcion = request.form["opcion"];
        casosUsoCita.registrarCita(nombre, apellido, tipoDoc, numDoc, nomDoc, opcion)
        
        return render_template("mostrarCita.html", citas=casosUsoCita.mostrar());

@app.route("/mostrarCita")
def mostrarCita():
    citas = casosUsoCita.mostrar();
    return render_template("mostrarCita.html", citas=citas)

@app.route("/mostrarComunes")
def mostrarComunes():
    contador = casosUsoCita.docCommons();
    contador2 = casosUsoCita.citaCommons();
    lista_contador = list(contador.items())
    lista_contador = list(contador2.items())
    return render_template("mostrarComunes.html", contador=lista_contador, contador2=lista_contador);

@app.route("/pacPorCita")
def pacPorCita():
    lista = casosUsoCita.pacPorTipCita();
    return render_template("pacPorCita.html", lista=lista);
    

if __name__=="__main__":
    app.run(debug=True);
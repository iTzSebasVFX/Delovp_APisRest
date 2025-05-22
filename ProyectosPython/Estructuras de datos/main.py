from fastapi import FastAPI, HTTPException, Form, Request
from pydantic import BaseModel
from modulos.casosUsoCita import conn as c
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates


class pacientes(BaseModel):
    id: int 
    nombre: str 
    apellido: str
    tipoDoc: str
    numDoc: int
    nomDoc: str
    opcion: str
   
class tipodecitas(BaseModel):
    id: int
    nombre: str


app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def mostrarIndex(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/formulario/", response_class=HTMLResponse)
def mostrarForm(request: Request):
    return templates.TemplateResponse("formulario.html", {"request": request})

# Crud con apifast y html
# Insertar Citas
@app.post("/formulario/registrarCita", response_class=HTMLResponse)
def recibir_datos(
    request: Request,
    nombre: str = Form(...),
    apellido: str = Form(...),
    tipoDoc: str = Form(...),
    numDoc: int = Form(...),
    nomDoc: str = Form(...),
    opcion: str = Form(...)):
    print(nombre + apellido)
    conn = c()
    cursor = conn.cursor()
    sql = "INSERT INTO pacientes (nombre, apellido, tipoDoc, numDoc, nomDoc, opcion) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (nombre, apellido, tipoDoc, numDoc, nomDoc, opcion)
    cursor.execute(sql, values)
    conn.commit()
    if (cursor.rowcount == 0):
        raise HTTPException(status_code=404, detail="Paciente no encontrado") # Lanzamos una excepcion
    cursor.close()
    conn.close()
    return templates.TemplateResponse("mostrarCitas.html", {"request": request, "pacienteId": "Usuario Agregado Correctamente"})

# Consultar Citas
@app.get("/formulario/mostrarCitas/", response_class=HTMLResponse)
def obtenerCitas(request: Request):
    conn = c()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pacientes")
    consulta = cursor.fetchall()
    cursor.close()
    conn.close()
    return templates.TemplateResponse("mostrarCitas.html", {"request": request, "consulta": consulta})

# Actualizar Citas
@app.post("/actualizarCita/")
def editar_paciente(
    id: int = Form(...),
    nombre: str = Form(...),
    apellido: str = Form(...),
    tipoDoc: str = Form(...),
    numDoc: int = Form(...),
    nomDoc: str = Form(...),
    opcion: str = Form(...)):
    conn = c()
    cursor = conn.cursor()
    sql = ("UPDATE pacientes SET nombre= %s, apellido = %s, tipoDoc = %s, numDoc = %s, nomDoc = %s, opcion= %s WHERE id = %s")
    valores = (nombre, apellido, tipoDoc, numDoc, nomDoc, opcion, id)
    cursor.execute(sql, valores) # si el put no funciona gracias al c, toca colocar en conn = sql.connector.connect(**db_config)
    conn.commit()
    cursor.close()
    conn.close()
    return RedirectResponse(url="/formulario/mostrarCitas", status_code=303)

# Eliminar citas
@app.get("/eliminar/{id}")
def eliminar_cita(id: int):
    conn = c()
    cursor = conn.cursor()
    sql = ("DELETE FROM pacientes WHERE id = %s")
    cursor.execute(sql, (id,))
    conn.commit()
    if (cursor.rowcount == 0):
        raise HTTPException(status_code=404, detail="Paciente no encontrado") # Lanzamos una excepcion
    cursor.close()
    conn.close()
    return RedirectResponse(url="/formulario/mostrarCitas/", status_code=303)

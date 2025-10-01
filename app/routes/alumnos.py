from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.models.alumno_model import get_alumno, crear_alumno, get_grupos, inscribir_alumno, get_alumno_inscrito

alumnos_bp = Blueprint("alumnos", __name__)

# Redirigir a plantilla de registro
@alumnos_bp.route("/registro")
def registro():
    return render_template("registro.html")

# Recibir datos del formulario
@alumnos_bp.route("/registrarAlumno", methods=["POST"])
def registrar_alumno():
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    correo = request.form["correo"]

    registrado = get_alumno(nombre, apellido, correo)

    if registrado is None:
        result = crear_alumno(nombre, apellido, correo)
    else:
        result = registrado

    grupos = get_grupos()
    return render_template("grupos.html", consulta=result, grupos=grupos)

# Inscribir a alumno en un grupo mediante rutas
@alumnos_bp.route("/inscribir/<string:idAlumno>/<string:idGrupo>")
def inscribir(idAlumno, idGrupo):
    mensaje = inscribir_alumno(idAlumno, idGrupo)
    grupos = get_grupos()
    if mensaje:
        flash(mensaje)
    
        # Renderizamos el mismo template de selección de grupos
        return render_template("grupos.html", consulta=(idAlumno,), grupos=grupos)
    else:
        alumno = get_alumno_inscrito(idAlumno, idGrupo)[0]
        return render_template("registroCompleto.html", alumno=alumno)

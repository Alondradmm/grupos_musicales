from flask import Blueprint, render_template, flash
from app.models.grupo_model import cerrar_inscripciones, abrir_inscripciones

grupos_bp = Blueprint("grupos", __name__)

@grupos_bp.route("/abrirInscripcion")
def abrir_inscripcion():
    abrir_inscripciones()  # por ahora solo retorna True
    return render_template("index.html", inscripcion_activa=True)

@grupos_bp.route("/cerrarInscripcion")
def cerrar_inscripcion():
    mensajes = cerrar_inscripciones()
    for m in mensajes:
        flash(m)
    return render_template("index.html", inscripcion_activa=False)

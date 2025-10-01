from flask import Blueprint, render_template

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    # Ruta principal
    return render_template("index.html", inscripcion_activa=True)

@main_bp.route("/salir")
def salir():
    # Ruta para salir de los reportes
    return render_template("index.html", inscripcion_activa=False)
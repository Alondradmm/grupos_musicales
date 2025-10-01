from flask import Blueprint, render_template, flash, redirect, url_for
from app.models.reportes_model import get_alumnos, get_grupos, get_horarios

reportes_bp = Blueprint("reportes", __name__)

@reportes_bp.route("/reportes")
def reportes():
    alumnos = get_alumnos()
    return render_template('reportes.html', regisAlumnos=True, alumnos=alumnos)

@reportes_bp.route("/getGrupo")
def reportes_grupos():
    grupos, mensajes = get_grupos()
    for m in mensajes:
        flash(m)
    return render_template('reportes.html', regisGrupos=True, grupos=grupos)

@reportes_bp.route("/getHorario")
def reportes_horarios():
    horarios = get_horarios()
    return render_template('reportes.html', regisHorarios=True, horarios=horarios)

@reportes_bp.route('/getAlumnos')
def getAlumnos():
    return redirect(url_for('reportes.reportes'))
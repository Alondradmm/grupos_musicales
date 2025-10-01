from flask import current_app

def get_alumnos():
    mysql = current_app.mysql
    cursor = mysql.cursor()
    cursor.execute(
        'SELECT alumno.Apellido, alumno.Nombre, alumno.Correo, grupo.Nombre, grupo.Horario '
        'FROM alumno '
        'INNER JOIN inscripciones ON inscripciones.id_alumno = alumno.id_alumno '
        'INNER JOIN grupo ON grupo.id_grupo = inscripciones.id_grupo '
        'ORDER BY alumno.Apellido ASC'
    )
    result = cursor.fetchall()
    cursor.close()
    return result

def get_grupos():
    mysql = current_app.mysql
    cursor = mysql.cursor()
    cursor.execute(
        'SELECT Nombre, Horario, COUNT(inscripciones.id_grupo) '
        'FROM grupo '
        'INNER JOIN inscripciones ON grupo.id_grupo = inscripciones.id_grupo '
        'GROUP BY grupo.id_grupo'
    )
    result = cursor.fetchall()
    cursor.close()

    # Grupos cancelados
    cursor = mysql.cursor()
    cursor.execute(
        'SELECT grupo.id_grupo, Nombre FROM grupo '
        'WHERE grupo.id_grupo NOT IN (SELECT inscripciones.id_grupo FROM inscripciones)'
    )
    cancelados = cursor.fetchall()
    cursor.close()

    mensajes = [f"El grupo {g[1]} ha sido cancelado" for g in cancelados]
    return result, mensajes

def get_horarios():
    mysql = current_app.mysql
    cursor = mysql.cursor()
    cursor.execute(
        'SELECT Horario, COUNT(id_alumno) '
        'FROM grupo INNER JOIN inscripciones ON grupo.id_grupo = inscripciones.id_grupo '
        'GROUP BY Horario'
    )
    result = cursor.fetchall()
    cursor.close()
    return result

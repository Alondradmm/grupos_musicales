from flask import current_app
from datetime import date

# Validar si alumno existe, utilizando nombre, apellido y correo
def get_alumno(nombre, apellido, correo):
    mysql = current_app.mysql
    cursor = mysql.cursor()
    cursor.execute(
        "SELECT id_alumno FROM alumno WHERE Nombre=%s AND Apellido=%s AND Correo=%s",
        (nombre, apellido, correo),
    )
    result = cursor.fetchone()
    cursor.close()
    return result

# Creación de un nuevo alumno y devolver el ID
def crear_alumno(nombre, apellido, correo):
    mysql = current_app.mysql
    cursor = mysql.cursor()
    alumno_existente = get_alumno(nombre, apellido, correo)
    if alumno_existente is None:
        # Insertar alumno
        cursor.execute(
            "INSERT INTO alumno(Nombre, Apellido, Correo) VALUES (%s,%s,%s)",
            (nombre, apellido, correo),
        )
        mysql.commit()
        cursor.close()

        # Consulta el ID máximo (correspondiente al último alumno creado)
        cursor = mysql.cursor()
        cursor.execute("SELECT MAX(id_alumno) FROM alumno")
        result = cursor.fetchone()
        cursor.close()
        return result
    else:
        return alumno_existente

def get_grupos():
    mysql = current_app.mysql
    cursor = mysql.cursor()
    cursor.execute("SELECT * FROM grupo")
    result = cursor.fetchall()
    cursor.close()
    return result

def inscribir_alumno(idAlumno, idGrupo):
    mysql = current_app.mysql
    cursor = mysql.cursor()
    from datetime import date
    today = date.today()
    alumno_inscrito = get_alumno_inscrito(idAlumno, idGrupo)
    if len(alumno_inscrito) == 0:
        cursor.execute(
            "INSERT INTO inscripciones(id_alumno, id_grupo, FechaInscripcion) VALUES (%s,%s,%s)",
            (idAlumno, idGrupo, today),
        )
        mysql.commit()
        cursor.close()
        return None
    else:
        cursor.close()
        return "Ya estás registrado en ese curso"

def get_alumno_inscrito(idAlumno, idGrupo):
    mysql = current_app.mysql
    cursor = mysql.cursor()
    cursor.execute(
        """SELECT alumno.Apellido, alumno.Nombre, alumno.Correo, grupo.Nombre, grupo.Horario 
           FROM alumno 
           INNER JOIN inscripciones ON inscripciones.id_alumno = alumno.id_alumno 
           INNER JOIN grupo ON grupo.id_grupo = inscripciones.id_grupo 
           WHERE inscripciones.id_grupo=%s AND inscripciones.id_alumno=%s""",
        (idGrupo, idAlumno),
    )
    result = cursor.fetchall()
    cursor.close()
    return result

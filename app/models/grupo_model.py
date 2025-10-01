from flask import current_app

def cerrar_inscripciones():
    mysql = current_app.mysql
    cursor = mysql.cursor()
    
    # Buscar grupos que no alcanzaron CupoMinimo
    cursor.execute(
        'SELECT inscripciones.id_grupo, COUNT(*), grupo.CupoMinimo '
        'FROM inscripciones INNER JOIN grupo ON grupo.id_grupo = inscripciones.id_grupo '
        'GROUP BY id_grupo'
    )
    resultados = cursor.fetchall()
    cursor.close()

    # Eliminar inscripciones de grupos incompletos
    for i in resultados:
        if i[1] < i[2]:
            cursor = mysql.cursor()
            cursor.execute('DELETE FROM inscripciones WHERE id_grupo = %s', (i[0],))
            mysql.commit()
            cursor.close()

    # Buscar grupos sin inscripciones
    cursor = mysql.cursor()
    cursor.execute(
        'SELECT grupo.id_grupo, Nombre FROM grupo WHERE grupo.id_grupo NOT IN '
        '(SELECT inscripciones.id_grupo FROM inscripciones)'
    )
    grupos_cancelados = cursor.fetchall()
    cursor.close()

    return [f"El grupo {g[1]} ha sido cancelado" for g in grupos_cancelados]

def abrir_inscripciones():
    # Simplemente devolver True o manejar estado si fuera necesario
    return True

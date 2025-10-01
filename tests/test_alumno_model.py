from unittest.mock import MagicMock, patch
from app.models.alumno_model import crear_alumno, get_alumno, get_grupos, inscribir_alumno, get_alumno_inscrito

def test_crear_y_obtener_alumno(app):
    fake_alumno = (1, "Alondra", "Méndez", "dalon@gmail.com")
    fake_cursor = MagicMock()
    fake_cursor.fetchone.return_value = fake_alumno
    fake_mysql = MagicMock()
    fake_mysql.cursor.return_value = fake_cursor

    with app.app_context():
        with patch("flask.current_app.mysql", fake_mysql):
            nuevo = crear_alumno("Alondra", "Méndez", "dalon@gmail.com")
            assert nuevo == fake_alumno

            alumno = get_alumno("Alondra", "Méndez", "dalon@gmail.com")
            assert alumno == fake_alumno
            assert alumno[1] == "Alondra"

def test_inscribir_alumno(app):
    fake_alumno = (1, "Rodrigo", "González", "rodrigo@mail.com")
    fake_grupos = [(1, "Piano Vespertino", "Martes a Jueves de 5:00p.m. a 7:00p.m.", 10)]
    fake_inscripcion = [(fake_alumno[2], fake_alumno[1], fake_alumno[3], fake_grupos[0][1], fake_grupos[0][2])]

    fake_cursor = MagicMock()
    fake_cursor.fetchall.side_effect = [[], fake_inscripcion]  # primera llamada = no inscrito, segunda = inscrito
    fake_mysql = MagicMock()
    fake_mysql.cursor.return_value = fake_cursor

    with app.app_context():
        with patch("flask.current_app.mysql", fake_mysql), \
             patch("app.models.alumno_model.get_grupos", return_value=fake_grupos):

            inscribir_alumno(fake_alumno[0], fake_grupos[0][0])
            inscrito = get_alumno_inscrito(fake_alumno[0], fake_grupos[0][0])
            assert len(inscrito) > 0
            assert inscrito[0][0] == "González"

def test_inscripcion_duplicada(app):
    fake_alumno = (1, "Javier", "Pérez", "javi@gmail.com")
    fake_grupos = [(1, "Piano Vespertino", "Martes a Jueves de 5:00p.m. a 7:00p.m.", 10)]
    fake_cursor = MagicMock()
    # primera llamada vacía, segunda = inscrito, tercera = intenta duplicar
    fake_cursor.fetchall.side_effect = [[], [(fake_alumno[2], fake_alumno[1], fake_alumno[3], fake_grupos[0][1], fake_grupos[0][2])],
                                        [(fake_alumno[2], fake_alumno[1], fake_alumno[3], fake_grupos[0][1], fake_grupos[0][2])]]
    fake_mysql = MagicMock()
    fake_mysql.cursor.return_value = fake_cursor

    with app.app_context():
        with patch("flask.current_app.mysql", fake_mysql), \
             patch("app.models.alumno_model.get_grupos", return_value=fake_grupos):

            # Primera inscripción
            inscribir_alumno(fake_alumno[0], fake_grupos[0][0])
            # Duplicado
            inscribir_alumno(fake_alumno[0], fake_grupos[0][0])
            inscrito = get_alumno_inscrito(fake_alumno[0], fake_grupos[0][0])
            assert len(inscrito) == 1, "Error: el alumno se inscribió dos veces!"

from unittest.mock import MagicMock, patch
from app.models.alumno_model import crear_alumno

def test_registro_route(client):
    response = client.get("/registro")
    assert response.status_code == 200
    assert b"nombre" in response.data

def test_registrar_alumno_route(client):
    data = {"nombre": "Carlos", "apellido": "Medellín", "correo": "carlos@mail.com"}

    fake_alumno = (1, "Carlos", "Medellín", "carlos@mail.com")
    fake_grupos = [
        (1, "Piano Vespertino", "Martes a Jueves de 5:00p.m. a 7:00p.m.", 10)
    ]

    # Parchea las funciones como las importó la ruta
    with patch("app.routes.alumnos.get_alumno", return_value=None), \
         patch("app.routes.alumnos.crear_alumno", return_value=fake_alumno), \
         patch("app.routes.alumnos.get_grupos", return_value=fake_grupos):

        response = client.post("/registrarAlumno", data=data)

        assert response.status_code == 200
        assert b"Piano Vespertino" in response.data
        assert b"ID Alumno: 1" in response.data

def test_inscribir_route(client):
    # Alumno y grupo de prueba
    idAlumno = 1
    idGrupo = 1
    alumno_inscrito = [("Torres", "Joel", "jose_torres@gmail.com", "Piano Vespertino", "Martes a Jueves de 5:00p.m. a 7:00p.m.")]

    with patch("app.routes.alumnos.get_alumno_inscrito", return_value=[]), \
         patch("app.routes.alumnos.inscribir_alumno", return_value=None), \
         patch("app.routes.alumnos.get_alumno_inscrito", return_value=alumno_inscrito):

        response = client.get(f"/inscribir/{idAlumno}/{idGrupo}")

        assert response.status_code == 200
        # Verifica que el nombre del alumno aparece o mensaje de duplicado
        assert (b"Joel" in response.data) or ("Ya estás registrado en ese curso".encode() in response.data)

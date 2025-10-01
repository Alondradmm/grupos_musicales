def test_registro_route(client):
    """ Verifica que la ruta /registro devuelve status 200 y contiene el formulario."""
    response = client.get("/registro")
    assert response.status_code == 200
    assert b"nombre" in response.data  # busca input con name="nombre"

def test_registrar_alumno_route(client, app):
    """ Verifica que se puede registrar un alumno mediante POST y devuelve grupos. """
    data = {"nombre": "Carlos", "apellido": "Medellín", "correo": "carlos@mail.com"}
    response = client.post("/registrarAlumno", data=data)
    assert response.status_code == 200
    assert b"grupos" in response.data.lower()  # contenido de grupos.html

def test_inscribir_route(client, app):
    """ Verifica que un alumno se puede inscribir a un grupo usando la ruta /inscribir."""
    with app.app_context():
        # Crear alumno
        from app.models.alumno_model import crear_alumno, get_grupos
        alumno = crear_alumno("Joel", "Torres", "jose_torres@gmail.com")
        grupos = get_grupos()
        idGrupo = grupos[0][0]

    response = client.get(f"/inscribir/{alumno[0]}/{idGrupo}")
    assert response.status_code == 200
    assert (b"Joel" in response.data) or ("Ya estás registrado en ese curso".encode() in response.data)

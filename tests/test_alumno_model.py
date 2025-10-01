import pytest
from app.models.alumno_model import get_alumno, crear_alumno, get_grupos, inscribir_alumno, get_alumno_inscrito

def test_crear_y_obtener_alumno(app):
    """ Verifica que un alumno se puede crear y luego obtener correctamente. """
    with app.app_context():
        # Crear alumno
        nuevo = crear_alumno("Alondra", "Méndez", "dalon@gmail.com")
        assert nuevo is not None

        # Obtener alumno
        alumno = get_alumno("Alondra", "Méndez", "dalon@gmail.com")
        assert alumno is not None

def test_inscribir_alumno(app):
    """ Verifica que un alumno se puede inscribir a un grupo. """
    with app.app_context():
        # Crear alumno de prueba
        alumno = crear_alumno("Rodrigo", "González", "rodrigo@mail.com")

        # Tomar primer grupo de prueba
        grupos = get_grupos()
        assert len(grupos) > 0
        idGrupo = grupos[0][0]  # asumiendo que el primer campo es id_grupo

        # Inscribir alumno
        inscribir_alumno(alumno[0], idGrupo)

        # Verificar inscripción
        inscrito = get_alumno_inscrito(alumno[0], idGrupo)
        assert inscrito is not None
        assert inscrito[0][0] == "González"  # apellido

def test_inscripcion_duplicada(app):
    """ Test para verificar que un alumno no puede inscribirse dos veces en el mismo grupo. """
    with app.app_context():
        # Crear alumno de prueba
        alumno = crear_alumno("Javier", "Pérez", "javi@gmail.com")

        # Tomar primer grupo de prueba
        grupos = get_grupos()
        assert len(grupos) > 0
        idGrupo = grupos[0][0]

        # Primera inscripción
        inscribir_alumno(alumno[0], idGrupo)

        # Intento de inscripción duplicada
        inscribir_alumno(alumno[0], idGrupo)

        # Verificar alumno inscrito, buscando que solo haya 1 registro
        inscrito = get_alumno_inscrito(alumno[0], idGrupo)
        
        # En caso de no haber solo un registro, indica duplicado
        assert len(inscrito) == 1, "Error: el alumno se inscribió dos veces!"


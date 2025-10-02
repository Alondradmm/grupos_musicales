import pytest
from app import create_app
from unittest.mock import MagicMock

@pytest.fixture
def app():
    """
    Crea la app Flask en modo testing y la devuelve para usarla en los tests.
    La conexión a MySQL se reemplaza por un mock.
    """
    app = create_app(testing=True)

    # Mock global de MySQL
    app.mysql = MagicMock()
    cursor_mock = MagicMock()
    app.mysql.cursor.return_value = cursor_mock
    # fetchone y fetchall devolverán datos por test específico con side_effect
    cursor_mock.fetchone.return_value = None
    cursor_mock.fetchall.return_value = []

    yield app

@pytest.fixture
def client(app):
    """Devuelve un test client para simular requests HTTP."""
    return app.test_client()

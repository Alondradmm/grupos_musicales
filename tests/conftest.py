import pytest
from app import create_app

@pytest.fixture
def app():
    """
    Crea la app Flask en modo testing y la devuelve para usarla en los tests.
    """
    app = create_app(testing=True)
    yield app

@pytest.fixture
def client(app):
    """
    Devuelve un test client para simular requests HTTP.
    """
    return app.test_client()


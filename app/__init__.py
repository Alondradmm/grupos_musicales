from flask import Flask
import pymysql
import os
from unittest.mock import MagicMock

def create_app(testing=False):
    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY", "curso_musica")

    if testing:
        app.mysql = MagicMock()
    else:
        # Configuración MySQL
        # Modificación para leer variables de entorno
        host = os.getenv("MYSQL_HOST", "localhost")
        user = os.getenv("MYSQL_USER", "root")
        db_port = int(os.getenv("DB_PORT", 3306)) # Puerto del contenedor
        password = os.getenv("MYSQL_PASSWORD", "")
        db = os.getenv("MYSQL_DB", "gruposmusicales")

        # Conexión MySQL
        app.mysql = pymysql.connect(
            host=host,
            user=user,
            port=db_port,
            password=password,
            db=db
        )

    # Importar y registrar blueprints
    from .routes.main import main_bp
    from .routes.alumnos import alumnos_bp
    from .routes.grupos import grupos_bp
    from .routes.reportes import reportes_bp


    app.register_blueprint(alumnos_bp)
    app.register_blueprint(grupos_bp)
    app.register_blueprint(reportes_bp)
    app.register_blueprint(main_bp)

    return app

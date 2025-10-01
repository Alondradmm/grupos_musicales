from flask import Flask
import pymysql

def create_app(testing=False):
    app = Flask(__name__)
    app.secret_key = "curso_musica"

    # Configuración MySQL
    app.config['TESTING'] = testing
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'gruposmusicales_test' if testing else 'gruposmusicales'

    # Conexión MySQL
    app.mysql = pymysql.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        db=app.config['MYSQL_DB']
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

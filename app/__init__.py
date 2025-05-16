from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inicialización de la base de datos
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/libros.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Registro de rutas
    from .routes import main
    app.register_blueprint(main)

    return app

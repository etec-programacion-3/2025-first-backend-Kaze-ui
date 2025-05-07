from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Inicializar Flask
app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///biblioteca.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Evita warnings

# Inicializar SQLAlchemy y Flask-Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)  # <--- ¡Clave para los comandos de migración!

# Importar modelos (¡ESENCIAL para que Flask-Migrate los detecte!)
from models.libro import Libro  # Asegúrate de que esta importación esté después de `db`

if __name__ == '__main__':
    app.run(debug=True)
from datetime import datetime
from .. import db

class Libro(db.Model):
    __tablename__ = 'libros'
    
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    autor = db.Column(db.String(255), nullable=False)
    isbn = db.Column(db.String(13), unique=True, nullable=False)
    categoria = db.Column(db.String(100))
    estado = db.Column(db.String(50), default='disponible')
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
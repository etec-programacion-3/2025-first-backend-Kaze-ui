from app import create_app, db
from app.models import Libro

app = create_app()

with app.app_context():
    db.create_all()

    # Datos de ejemplo
    if not Libro.query.first():
        libro1 = Libro(titulo="Cien años de soledad", autor="Gabriel García Márquez", anio_publicacion=1967, isbn="1234567890123", categoria="Novela", estado="disponible")
        libro2 = Libro(titulo="Don Quijote de la Mancha", autor="Miguel de Cervantes", anio_publicacion=1605, isbn="9876543210987", categoria="Clásico", estado="disponible")
        db.session.add_all([libro1, libro2])
        db.session.commit()

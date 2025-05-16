import unittest
from app import create_app, db
from app.models import Libro

class TestRoutes(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_crear_libro(self):
        response = self.client.post('/libros', json={
            'titulo': 'El Principito',
            'autor': 'Antoine de Saint-Exupéry',
            'anio_publicacion': 1943,
            'isbn': '1234567890123',
            'categoria': 'Ficción'
        })
        self.assertEqual(response.status_code, 201)

    def test_obtener_libros(self):
        response = self.client.get('/libros')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

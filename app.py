from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///libros.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Libro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100), nullable=False)
    anho = db.Column(db.Integer, nullable=False)
    isbn = db.Column(db.String(13), unique=True, nullable=False)

@app.route('/libros', methods=['GET'])
def obtener_libros():
    libros = Libro.query.all()
    return jsonify([
        {
            'id': libro.id,
            'titulo': libro.titulo,
            'autor': libro.autor,
            'anho': libro.anho,
            'isbn': libro.isbn
        } for libro in libros
    ])

@app.route('/libros', methods=['POST'])
def crear_libro():
    datos = request.get_json()
    nuevo_libro = Libro(
        titulo=datos['titulo'],
        autor=datos['autor'],
        anho=datos['anho'],
        isbn=datos['isbn']
    )
    db.session.add(nuevo_libro)
    db.session.commit()
    return jsonify({'mensaje': 'Libro creado exitosamente'}), 201

@app.route('/libros/<int:id>', methods=['GET'])
def obtener_libro(id):
    libro = Libro.query.get_or_404(id)
    return jsonify({
        'id': libro.id,
        'titulo': libro.titulo,
        'autor': libro.autor,
        'anho': libro.anho,
        'isbn': libro.isbn
    })

@app.route('/libros/<int:id>', methods=['PUT'])
def modificar_libro(id):
    libro = Libro.query.get_or_404(id)
    datos = request.get_json()
    libro.titulo = datos.get('titulo', libro.titulo)
    libro.autor = datos.get('autor', libro.autor)
    libro.anho = datos.get('anho', libro.anho)
    libro.isbn = datos.get('isbn', libro.isbn)
    db.session.commit()
    return jsonify({'mensaje': 'Libro actualizado exitosamente'})

@app.route('/libros/<int:id>', methods=['DELETE'])
def eliminar_libro(id):
    libro = Libro.query.get_or_404(id)
    db.session.delete(libro)
    db.session.commit()
    return jsonify({'mensaje': 'Libro eliminado exitosamente'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

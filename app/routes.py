from flask import Blueprint, request, jsonify
from .models import Libro
from . import db
from .schemas import LibroSchema

main = Blueprint('main', __name__)

libro_schema = LibroSchema()
libros_schema = LibroSchema(many=True)

@main.route('/libros', methods=['GET'])
def obtener_libros():
    libros = Libro.query.all()
    return jsonify([{
        'id': libro.id,
        'titulo': libro.titulo,
        'autor': libro.autor,
        'anio_publicacion': libro.anio_publicacion
    } for libro in libros])

@main.route('/libros', methods=['POST'])
def crear_libro():
    datos = request.get_json()
    errores = libro_schema.validate(datos)
    if errores:
        return jsonify(errores), 400

    nuevo_libro = Libro(
        titulo=datos['titulo'],
        autor=datos['autor'],
        anio_publicacion=datos['anio_publicacion'],
        isbn=datos['isbn'],
        categoria=datos['categoria'],
        estado=datos.get('estado', 'disponible')
    )
    db.session.add(nuevo_libro)
    db.session.commit()
    return jsonify({'mensaje': 'Libro creado exitosamente'}), 201

@main.route('/libros/<int:id>', methods=['PUT'])
def actualizar_libro(id):
    datos = request.get_json()
    libro = Libro.query.get_or_404(id)
    libro.titulo = datos['titulo']
    libro.autor = datos['autor']
    libro.anio_publicacion = datos['anio_publicacion']
    db.session.commit()
    return jsonify({'mensaje': 'Libro actualizado exitosamente'})

@main.route('/libros/<int:id>', methods=['DELETE'])
def eliminar_libro(id):
    libro = Libro.query.get_or_404(id)
    db.session.delete(libro)
    db.session.commit()
    return jsonify({'mensaje': 'Libro eliminado exitosamente'})

@main.route('/libros/buscar', methods=['GET'])
def buscar_libros():
    titulo = request.args.get('titulo')
    categoria = request.args.get('categoria')
    orden = request.args.get('orden', 'titulo')
    pagina = int(request.args.get('pagina', 1))
    tamano = int(request.args.get('tamano', 10))

    query = Libro.query

    if titulo:
        query = query.filter(Libro.titulo.ilike(f"%{titulo}%"))
    if categoria:
        query = query.filter(Libro.categoria == categoria)

    query = query.order_by(getattr(Libro, orden).asc())
    libros = query.paginate(page=pagina, per_page=tamano, error_out=False).items

    return jsonify([{
        'id': libro.id,
        'titulo': libro.titulo,
        'autor': libro.autor,
        'anio_publicacion': libro.anio_publicacion,
        'isbn': libro.isbn,
        'categoria': libro.categoria,
        'estado': libro.estado,
        'fecha_creacion': libro.fecha_creacion
    } for libro in libros])

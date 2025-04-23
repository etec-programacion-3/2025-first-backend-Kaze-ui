from flask import Blueprint, request, jsonify
from app.models.libro import Libro
from app.schemas.libro import LibroSchema
from app.extensions import db

libros_bp = Blueprint('libros', __name__, url_prefix='/api/libros')
libro_schema = LibroSchema()
libros_schema = LibroSchema(many=True)

@libros_bp.route('/', methods=['POST'])
def crear_libro():
    data = request.get_json()
    errors = libro_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    
    libro = Libro(**data)
    db.session.add(libro)
    db.session.commit()
    
    return libro_schema.jsonify(libro), 201

@libros_bp.route('/', methods=['GET'])
def listar_libros():
    libros = Libro.query.all()
    return jsonify(libros_schema.dump(libros))

@libros_bp.route('/<int:id>', methods=['GET'])
def obtener_libro(id):
    libro = Libro.query.get_or_404(id)
    return libro_schema.jsonify(libro)

@libros_bp.route('/<int:id>', methods=['PUT'])
def actualizar_libro(id):
    libro = Libro.query.get_or_404(id)
    data = request.get_json()
    errors = libro_schema.validate(data, partial=True)
    if errors:
        return jsonify(errors), 400
    
    for key, value in data.items():
        setattr(libro, key, value)
    
    db.session.commit()
    return libro_schema.jsonify(libro)

@libros_bp.route('/<int:id>', methods=['DELETE'])
def eliminar_libro(id):
    libro = Libro.query.get_or_404(id)
    db.session.delete(libro)
    db.session.commit()
    return jsonify({'message': 'Libro eliminado'}), 200

@libros_bp.route('/buscar', methods=['GET'])
def buscar_libros():
    titulo = request.args.get('titulo')
    autor = request.args.get('autor')
    categoria = request.args.get('categoria')
    
    query = Libro.query
    
    if titulo:
        query = query.filter(Libro.titulo.ilike(f'%{titulo}%'))
    if autor:
        query = query.filter(Libro.autor.ilike(f'%{autor}%'))
    if categoria:
        query = query.filter(Libro.categoria.ilike(f'%{categoria}%'))
    
    libros = query.all()
    return jsonify(libros_schema.dump(libros))
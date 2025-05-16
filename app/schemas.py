from marshmallow import Schema, fields, validate

class LibroSchema(Schema):
    id = fields.Int(dump_only=True)
    titulo = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    autor = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    anio_publicacion = fields.Int(required=True)
    isbn = fields.Str(required=True, validate=validate.Length(equal=13))
    categoria = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    estado = fields.Str(validate=validate.OneOf(["disponible", "prestado"]))
    fecha_creacion = fields.DateTime(dump_only=True)

from marshmallow import Schema, fields, validate

class LibroSchema(Schema):
    id = fields.Int(dump_only=True)
    titulo = fields.Str(required=True, validate=validate.Length(max=255))
    autor = fields.Str(required=True, validate=validate.Length(max=255))
    isbn = fields.Str(required=True, validate=validate.Length(min=10, max=13))
    categoria = fields.Str(validate=validate.Length(max=100))
    estado = fields.Str(dump_only=True)
    fecha_creacion = fields.DateTime(dump_only=True)
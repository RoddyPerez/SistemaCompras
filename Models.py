# models.py
from app import db


class Departamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    estado = db.Column(db.Boolean, default=True)

class UnidadMedida(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(255), nullable=False)
    estado = db.Column(db.Boolean, default=True)

class Proveedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cedula_rnc = db.Column(db.String(50), nullable=False)
    nombre_comercial = db.Column(db.String(255), nullable=False)
    estado = db.Column(db.Boolean, default=True)

class Articulo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(255), nullable=False)
    marca = db.Column(db.String(255))
    unidad_medida_id = db.Column(db.Integer, db.ForeignKey('unidad_medida.id'))
    existencia = db.Column(db.Integer, default=0)
    estado = db.Column(db.Boolean, default=True)
    unidad_medida = db.relationship('UnidadMedida')

class OrdenCompra(db.Model):
    numero_orden = db.Column(db.Integer, primary_key=True)
    fecha_orden = db.Column(db.Date, nullable=False)
    estado = db.Column(db.Boolean, default=True)
    articulo_id = db.Column(db.Integer, db.ForeignKey('articulo.id'))
    cantidad = db.Column(db.Integer, nullable=False)
    unidad_medida_id = db.Column(db.Integer, db.ForeignKey('unidad_medida.id'))
    costo_unitario = db.Column(db.Numeric(10, 2), nullable=False)
    articulo = db.relationship('Articulo')
    unidad_medida = db.relationship('UnidadMedida')

class AsientoContable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(255), nullable=False)
    tipo_inventario_id = db.Column(db.Integer)
    cuenta_contable = db.Column(db.String(255), nullable=False)
    tipo_movimiento = db.Column(db.String(2), nullable=False)
    fecha_asiento = db.Column(db.Date, nullable=False)
    monto = db.Column(db.Numeric(10, 2), nullable=False)
    estado = db.Column(db.Boolean, default=True)
    
from app import app

with app.app_context():
    db.create_all()

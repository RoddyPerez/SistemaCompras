from flask import render_template, request, redirect, url_for
from app import app, db
from datetime import datetime
from Models import Departamento, UnidadMedida, Proveedor, Articulo, OrdenCompra, AsientoContable

# -------------------------- PÁGINA PRINCIPAL --------------------------
@app.route('/')
def index():
    return render_template('index.html')

# -------------------------- DEPARTAMENTOS --------------------------
@app.route('/departamentos')
def listar_departamentos():
    departamentos = Departamento.query.all()
    return render_template('departamentos.html', departamentos=departamentos)

@app.route('/departamentos/agregar', methods=['GET', 'POST'])
def agregar_departamento():
    if request.method == 'POST':
        nombre = request.form['nombre']
        nuevo_departamento = Departamento(nombre=nombre)
        db.session.add(nuevo_departamento)
        db.session.commit()
        return redirect(url_for('listar_departamentos'))
    return render_template('agregar_departamento.html')

@app.route('/departamentos/editar/<int:id>', methods=['GET', 'POST'])
def editar_departamento(id):
    departamento = Departamento.query.get_or_404(id)
    if request.method == 'POST':
        departamento.nombre = request.form['nombre']
        db.session.commit()
        return redirect(url_for('listar_departamentos'))
    return render_template('editar_departamento.html', departamento=departamento)

@app.route('/departamentos/eliminar/<int:id>', methods=['POST'])
def eliminar_departamento(id):
    departamento = Departamento.query.get_or_404(id)
    db.session.delete(departamento)
    db.session.commit()
    return redirect(url_for('listar_departamentos'))

# -------------------------- UNIDADES DE MEDIDA --------------------------
@app.route('/unidades_medida')
def listar_unidades_medida():
    unidades = UnidadMedida.query.all()
    return render_template('unidades_medida.html', unidades=unidades)

@app.route('/unidades_medida/agregar', methods=['GET', 'POST'])
def agregar_unidad_medida():
    if request.method == 'POST':
        descripcion = request.form['descripcion']
        nueva_unidad = UnidadMedida(descripcion=descripcion)
        db.session.add(nueva_unidad)
        db.session.commit()
        return redirect(url_for('listar_unidades_medida'))
    return render_template('agregar_unidad_medida.html')

@app.route('/unidades_medida/editar/<int:id>', methods=['GET', 'POST'])
def editar_unidad_medida(id):
    unidad = UnidadMedida.query.get_or_404(id)
    if request.method == 'POST':
        unidad.descripcion = request.form['descripcion']
        db.session.commit()
        return redirect(url_for('listar_unidades_medida'))
    return render_template('editar_unidad_medida.html', unidad=unidad)

@app.route('/unidades_medida/eliminar/<int:id>', methods=['POST'])
def eliminar_unidad_medida(id):
    unidad = UnidadMedida.query.get_or_404(id)
    db.session.delete(unidad)
    db.session.commit()
    return redirect(url_for('listar_unidades_medida'))

# -------------------------- PROVEEDORES --------------------------
@app.route('/proveedores')
def listar_proveedores():
    proveedores = Proveedor.query.all()
    return render_template('proveedores.html', proveedores=proveedores)

@app.route('/proveedores/agregar', methods=['GET', 'POST'])
def agregar_proveedor():
    if request.method == 'POST':
        cedula_rnc = request.form['cedula_rnc']
        nombre_comercial = request.form['nombre_comercial']
        nuevo_proveedor = Proveedor(cedula_rnc=cedula_rnc, nombre_comercial=nombre_comercial)
        db.session.add(nuevo_proveedor)
        db.session.commit()
        return redirect(url_for('listar_proveedores'))
    return render_template('agregar_proveedor.html')

@app.route('/proveedores/editar/<int:id>', methods=['GET', 'POST'])
def editar_proveedor(id):
    proveedor = Proveedor.query.get_or_404(id)
    if request.method == 'POST':
        proveedor.cedula_rnc = request.form['cedula_rnc']
        proveedor.nombre_comercial = request.form['nombre_comercial']
        db.session.commit()
        return redirect(url_for('listar_proveedores'))
    return render_template('editar_proveedor.html', proveedor=proveedor)

@app.route('/proveedores/eliminar/<int:id>', methods=['POST'])
def eliminar_proveedor(id):
    proveedor = Proveedor.query.get_or_404(id)
    db.session.delete(proveedor)
    db.session.commit()
    return redirect(url_for('listar_proveedores'))

# -------------------------- ARTÍCULOS --------------------------
@app.route('/articulos')
def listar_articulos():
    articulos = Articulo.query.all()
    return render_template('articulos.html', articulos=articulos)

@app.route('/articulos/agregar', methods=['GET', 'POST'])
def agregar_articulo():
    if request.method == 'POST':
        descripcion = request.form['descripcion']
        marca = request.form['marca']
        unidad_medida_id = request.form['unidad_medida_id']
        existencia = request.form['existencia']
        nuevo_articulo = Articulo(descripcion=descripcion, marca=marca, unidad_medida_id=unidad_medida_id, existencia=existencia)
        db.session.add(nuevo_articulo)
        db.session.commit()
        return redirect(url_for('listar_articulos'))
    return render_template('agregar_articulo.html')

@app.route('/articulos/editar/<int:id>', methods=['GET', 'POST'])
def editar_articulo(id):
    articulo = Articulo.query.get_or_404(id)
    if request.method == 'POST':
        articulo.descripcion = request.form['descripcion']
        articulo.marca = request.form['marca']
        articulo.unidad_medida_id = request.form['unidad_medida_id']
        articulo.existencia = request.form['existencia']
        db.session.commit()
        return redirect(url_for('listar_articulos'))
    return render_template('editar_articulo.html', articulo=articulo)

@app.route('/articulos/eliminar/<int:id>', methods=['POST'])
def eliminar_articulo(id):
    articulo = Articulo.query.get_or_404(id)
    db.session.delete(articulo)
    db.session.commit()
    return redirect(url_for('listar_articulos'))

# -------------------------- ÓRDENES DE COMPRA --------------------------
@app.route('/ordenes_compra')
def listar_ordenes_compra():
    ordenes = OrdenCompra.query.all()
    return render_template('ordenes_compra.html', ordenes=ordenes)

@app.route('/ordenes_compra/agregar', methods=['GET', 'POST'])
def agregar_orden_compra():
    articulos = Articulo.query.all()
    unidades = UnidadMedida.query.all()

    if request.method == 'POST':
        fecha_orden = request.form.get('fecha_orden')

        # Si no se recibe la fecha, asignar la actual
        if not fecha_orden:
            fecha_orden = datetime.today().strftime('%Y-%m-%d')

        articulo_id = request.form['articulo_id']
        cantidad = request.form['cantidad']
        unidad_medida_id = request.form['unidad_medida_id']
        costo_unitario = request.form['costo_unitario']

        nueva_orden = OrdenCompra(
            fecha_orden=fecha_orden,
            estado=1,  # Estado por defecto activo
            articulo_id=articulo_id,
            cantidad=cantidad,
            unidad_medida_id=unidad_medida_id,
            costo_unitario=costo_unitario
        )
        db.session.add(nueva_orden)
        db.session.commit()
        return redirect(url_for('listar_ordenes_compra'))

    return render_template('agregar_ordenes_compra.html', articulos=articulos, unidades=unidades)

# -------------------------- ASIENTOS CONTABLES --------------------------
@app.route('/asientos_contables')
def listar_asientos_contables():
    asientos = AsientoContable.query.all()
    return render_template('asiento_contable.html', asientos=asientos)

@app.route('/asientos_contables/agregar', methods=['GET', 'POST'])
def agregar_asiento_contable():
    if request.method == 'POST':
        descripcion = request.form['descripcion']
        cuenta_contable = request.form['cuenta_contable']
        tipo_movimiento = request.form['tipo_movimiento']
        fecha_asiento = request.form['fecha_asiento']
        monto = request.form['monto']
        nuevo_asiento = AsientoContable(descripcion=descripcion, cuenta_contable=cuenta_contable, tipo_movimiento=tipo_movimiento, fecha_asiento=fecha_asiento, monto=monto)
        db.session.add(nuevo_asiento)
        db.session.commit()
        return redirect(url_for('listar_asientos_contables'))
    return render_template('agregar_asiento_contable.html')




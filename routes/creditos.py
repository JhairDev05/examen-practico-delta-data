from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.creditos import Creditos
from utils.db import db

creditos_bp = Blueprint('creditos', __name__)

from collections import defaultdict

@creditos_bp.route("/")
def index():
    page = request.args.get("page", 1, type=int)
    per_page = 5  

    # Consulta paginada para la tabla
    creditos_paginated = Creditos.query.paginate(page=page, per_page=per_page, error_out=False)

    # Total de créditos otorgados
    total_creditos = db.session.query(db.func.sum(Creditos.monto)).scalar() or 0  

    # Obtener todos los créditos
    todos_los_creditos = Creditos.query.all()

    # Créditos por cliente
    creditos_por_cliente = defaultdict(float)
    for credito in todos_los_creditos:
        creditos_por_cliente[credito.cliente] += credito.monto

    labels_clientes = list(creditos_por_cliente.keys())
    data_clientes = list(creditos_por_cliente.values())

    # Créditos por rango de monto
    rangos = {
        "0-5000": 0,
        "5001-10000": 0,
        "10001-15000": 0,
        "20001+": 0
    }

    for credito in todos_los_creditos:
        if credito.monto <= 5000:
            rangos["0-5000"] += credito.monto
        elif credito.monto <= 10000:
            rangos["5001-10000"] += credito.monto
        elif credito.monto <= 15000:
            rangos["10001-15000"] += credito.monto
        else:
            rangos["20001+"] += credito.monto

    labels_rangos = list(rangos.keys())
    data_rangos = list(rangos.values())

    return render_template(
        "index.html",
        creditos=creditos_paginated,
        total_creditos=total_creditos,
        labels_clientes=labels_clientes,
        data_clientes=data_clientes,
        labels_rangos=labels_rangos,
        data_rangos=data_rangos
    )



@creditos_bp.route('/new', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        try:
            cliente = request.form.get('cliente', '').strip()
            monto = request.form.get('monto', '')
            tasa_interes = request.form.get('tasa_interes', '')
            plazo = request.form.get('plazo', '')
            fecha_otorgamiento = request.form.get('fecha_otorgamiento', '')

            monto = float(monto)
            tasa_interes = float(tasa_interes)
            plazo = int(plazo)

            if monto <= 0 or tasa_interes <= 0 or plazo <= 0:
                flash('Monto, tasa de interés y/o plazo deben ser mayores a 0.', 'danger')
                return render_template('create.html')

            if not cliente.strip():
                flash('El nombre del cliente es obligatorio y no puede estar vacío', 'danger')
                return render_template('create.html')

            if not cliente or not monto or not tasa_interes or not plazo or not fecha_otorgamiento:
                flash('Todos los campos son obligatorios', 'danger')
            
            monto = float(monto)
            tasa_interes = float(tasa_interes)
            plazo = int(plazo)

            nuevo_credito = Creditos(cliente, monto, tasa_interes, plazo, fecha_otorgamiento)
            db.session.add(nuevo_credito)
            db.session.commit()

            flash('Crédito agregado correctamente', 'success')
            return redirect(url_for('creditos.index'))

        except ValueError:
            flash('Error en los datos ingresados. Asegúrate de que los valores sean correctos.', 'danger')

    return render_template('create.html')  


@creditos_bp.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    creditos = Creditos.query.get_or_404(id)

    if request.method == 'POST':
        try:
            creditos.cliente = request.form['cliente']
            creditos.monto = float(request.form['monto'])
            creditos.tasa_interes = float(request.form['tasa_interes'])
            creditos.plazo = int(request.form['plazo'])
            creditos.fecha_otorgamiento = request.form['fecha_otorgamiento']

            creditos.monto = float(request.form['monto'])
            creditos.tasa_interes = float(request.form['tasa_interes'])
            creditos.plazo = int(request.form['plazo'])

            if creditos.monto <= 0 or creditos.tasa_interes <= 0 or creditos.plazo <= 0:
                flash('Monto, tasa de interés y/o plazo deben ser mayores a 0.', 'danger')
                return render_template('update.html', creditos=creditos)

            if not creditos.cliente or not creditos.monto or not creditos.tasa_interes or not creditos.plazo or not creditos.fecha_otorgamiento:
                flash('Todos los campos son obligatorios', 'danger')
                return render_template('update.html', creditos=creditos)

            db.session.commit()
            flash('Crédito actualizado correctamente', 'success')
            return redirect(url_for('creditos.index'))
        except ValueError:
            flash('Todos los campos son obligatorios.', 'danger')
            return render_template('update.html', creditos=creditos)

    return render_template('update.html', creditos=creditos)

@creditos_bp.route('/delete/<int:id>', methods=['POST', 'GET'])
def delete(id):
    credito = Creditos.query.get_or_404(id)
    
    db.session.delete(credito)
    db.session.commit()
    
    flash('Crédito eliminado correctamente', 'success')
    return redirect(url_for('creditos.index'))
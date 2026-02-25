from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Alumno(db.Model):
    __tablename__ = 'alumnos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    dni = db.Column(db.String(20))
    direccion = db.Column(db.String(200))
    telefono = db.Column(db.String(20))
    fecha_nacimiento = db.Column(db.Date)
    tel_emergencia = db.Column(db.String(20))
    nombre_emergencia = db.Column(db.String(100))
    relacion_emergencia = db.Column(db.String(50))
    activo = db.Column(db.String(20), default='ACTIVO')

    actividades = db.relationship('AlumnoActividad', backref='alumno', lazy=True)
    pagos = db.relationship('Pago', backref='alumno', lazy=True)


class Actividad(db.Model):
    __tablename__ = 'actividades'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    cuota_mensual = db.Column(db.Float, nullable=False)
    activa = db.Column(db.String(10), default='SI')

    alumnos = db.relationship('AlumnoActividad', backref='actividad', lazy=True)


class AlumnoActividad(db.Model):
    __tablename__ = 'alumno_actividades'

    id = db.Column(db.Integer, primary_key=True)
    alumno_id = db.Column(db.Integer, db.ForeignKey('alumnos.id'), nullable=False)
    actividad_id = db.Column(db.Integer, db.ForeignKey('actividades.id'), nullable=False)


class Pago(db.Model):
    __tablename__ = 'pagos'

    id = db.Column(db.Integer, primary_key=True)
    alumno_id = db.Column(db.Integer, db.ForeignKey('alumnos.id'), nullable=False)
    mes = db.Column(db.Integer, nullable=False)
    anio = db.Column(db.Integer, nullable=False)
    monto_total = db.Column(db.Float, nullable=False)
    monto_pagado = db.Column(db.Float, nullable=False)
    fecha_pago = db.Column(db.Date)
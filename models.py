from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    rol = db.Column(db.String(20), default="admin")  
    sucursal_id = db.Column(db.Integer, db.ForeignKey('sucursal.id'))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Sucursal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    usuarios = db.relationship('Usuario', backref='sucursal', lazy=True)
    empleados = db.relationship('Empleado', backref='sucursal', lazy=True)

class Empleado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    huella_id = db.Column(db.Integer, unique=True, nullable=False)  
    sucursal_id = db.Column(db.Integer, db.ForeignKey('sucursal.id'))
    asistencias = db.relationship('Asistencia', backref='empleado', lazy=True)

class Asistencia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    empleado_id = db.Column(db.Integer, db.ForeignKey('empleado.id'))
    fecha = db.Column(db.Date, server_default=db.func.current_date())
    hora_entrada = db.Column(db.Time)
    hora_salida = db.Column(db.Time)



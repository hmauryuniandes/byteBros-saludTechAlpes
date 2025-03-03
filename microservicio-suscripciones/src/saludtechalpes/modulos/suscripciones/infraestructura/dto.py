"""DTOs para la capa de infrastructura del dominio de suscripciones

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio del suscripciones

"""

"""DTOs para la capa de infrastructura del dominio de clientes

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de clientes

"""

from saludtechalpes.config.db import db
from sqlalchemy import ForeignKey
import uuid

Base = db.declarative_base()

class Cliente(db.Model):
    __tablename__ = "clientes"
    id = db.Column(db.String, primary_key=True)
    codigo = db.Column(db.String)
    nombres = db.Column(db.String, nullable=False)
    apellidos = db.Column(db.String, nullable=False)
    usuario = db.Column(db.String, nullable=False)
    numero_rut = db.Column(db.String, nullable=True)
    numero_cedula = db.Column(db.String, nullable=True)
    email_address = db.Column(db.String, nullable=True)
    email_domain = db.Column(db.String, nullable=True)

class Plan(db.Model):
    __tablename__ = "planes"
    id = db.Column(db.String, primary_key=True)
    codigo = db.Column(db.String, nullable=False)
    nombre = db.Column(db.String, nullable=False)


class Suscripcion(db.Model):
    __tablename__ = "suscripciones"
    id = db.Column(db.String, primary_key=True)
    cliente_id = db.Column(db.String, ForeignKey("clientes.id"))
    cliente: Cliente = db.relationship("Cliente", backref=db.backref("clientes", uselist=False))
    plan_id = db.Column(db.String, ForeignKey("planes.id"))
    plan: Plan =  db.relationship("Plan", backref=db.backref("planes", uselist=False))
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)
    estado = db.Column(db.String)
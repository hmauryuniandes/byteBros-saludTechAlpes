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
    codigo = db.Column(db.String, primary_key=True, nullable=False)
    nombres = db.Column(db.String, nullable=False)
    apellidos = db.Column(db.String, nullable=False)
    usuario = db.Column(db.String, nullable=False)
    numero_rut = db.Column(db.Integer, nullable=True)
    numero_cedula = db.Column(db.Integer, nullable=True)
    email_address = db.Column(db.String, nullable=True)
    email_domain = db.Column(db.String, nullable=True)

class Plan(db.Model):
    __tablename__ = "planes"
    codigo = db.Column(db.String, primary_key=True, nullable=False)
    nombre = db.Column(db.String, nullable=False)


class Suscripcion(db.Model):
    __tablename__ = "suscripciones"
    id = db.Column(db.String, primary_key=True, default=uuid.uuid4())
    cliente_id = db.Column(db.String, ForeignKey("clientes.codigo"))
    client: Cliente = db.relationship("Cliente", backref=db.backref("clientes", uselist=False))
    plan_id = db.Column(db.String, ForeignKey("planes.codigo"))
    plan: Plan =  db.relationship("Plan", backref=db.backref("planes", uselist=False))

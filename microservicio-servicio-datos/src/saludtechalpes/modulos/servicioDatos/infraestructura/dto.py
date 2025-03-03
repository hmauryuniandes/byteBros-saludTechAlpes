"""DTOs para la capa de infrastructura del dominio de servicio de datos
En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio del servicio de datos

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
    nombres = db.Column(db.String)
    apellidos = db.Column(db.String)
    usuario = db.Column(db.String, nullable=False)

class Plan(db.Model):
    __tablename__ = "planes"
    id = db.Column(db.String, primary_key=True)
    codigo = db.Column(db.String, nullable=False)
    nombre = db.Column(db.String, nullable=False)


class Suscripcion(db.Model):
    __tablename__ = "suscripciones"
    id = db.Column(db.String, primary_key=True)
    codigo = db.Column(db.String, nullable=False)
    cliente_id = db.Column(db.String, ForeignKey("clientes.id"))
    cliente: Cliente = db.relationship("Cliente", backref=db.backref("clientes", uselist=False))
    plan_id = db.Column(db.String, ForeignKey("planes.id"))
    plan: Plan =  db.relationship("Plan", backref=db.backref("planes", uselist=False))

class Experto(db.Model):
    __tablename__ = "experto"
    id = db.Column(db.String, primary_key=True)
    codigo = db.Column(db.String)
    nombres = db.Column(db.String, nullable=False)
    apellidos = db.Column(db.String, nullable=False)
    usuario = db.Column(db.String, nullable=False)
    numero_cedula = db.Column(db.String, nullable=True)
    email_address = db.Column(db.String, nullable=True)
    email_domain = db.Column(db.String, nullable=True)

class TipoNube(db.Model):
    __tablename__ = "tiponube"
    id = db.Column(db.String, primary_key=True)
    codigo = db.Column(db.String, nullable=False)
    nombre = db.Column(db.String, nullable=False)

class Nube(db.Model):
    __tablename__ = "nube"
    id = db.Column(db.String, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    tiponube_id = db.Column(db.String, ForeignKey("tiponube.id"))
    tiponube: TipoNube = db.relationship("TipoNube", backref=db.backref("tiponube", uselist=False))

class Imagen(db.Model):
    __tablename__ = "imagen"
    id = db.Column(db.String, primary_key=True)
    codigo = db.Column(db.String, nullable=False)
    nombre = db.Column(db.String, nullable=False)

class DataSet(db.Model):
    __tablename__ = "dataset"
    id = db.Column(db.String, primary_key=True)
    codigo = db.Column(db.String, nullable=False)
    nombre = db.Column(db.String, nullable=False)

class ServicioDatos(db.Model):
    __tablename__ = "serviciodatos"
    id = db.Column(db.String, primary_key=True)
    suscripcion_id = db.Column(db.String, ForeignKey("suscripciones.id"))
    suscripcion: Suscripcion = db.relationship("Suscripcion", backref=db.backref("suscripciones", uselist=False))
    experto_id = db.Column(db.String, ForeignKey("experto.id"))
    experto: Experto = db.relationship("Experto", backref=db.backref("experto", uselist=False))
    nube_id = db.Column(db.String, ForeignKey("nube.id"))
    nube: Nube=  db.relationship("Nube", backref=db.backref("nube", uselist=False))
    dataset_id = db.Column(db.String, ForeignKey("dataset.id"))
    dataset: DataSet=  db.relationship("DataSet", backref=db.backref("dataset", uselist=False))


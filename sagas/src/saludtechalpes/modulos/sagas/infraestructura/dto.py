from saludtechalpes.config.db import db

Base = db.declarative_base()

class SagaLog(db.Model):
    __tablename__ = "saga_logs"
    id = db.Column(db.String, primary_key=True)
    index = db.Column(db.Integer)
    id_correlacion = db.Column(db.String)
    descripcion = db.Column(db.String)
    evento = db.Column(db.String)
    evento_error = db.Column(db.String)
    comando = db.Column(db.String)
    comando_compensacion = db.Column(db.String)
    input = db.Column(db.String)
    output = db.Column(db.String)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    exitosa = db.Column(db.Boolean)

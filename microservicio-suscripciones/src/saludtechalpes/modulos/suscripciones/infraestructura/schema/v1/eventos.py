from pulsar.schema import *
from saludtechalpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class SuscripcionCreadaPayload(Record):
    codigo_cliente = String()
    codigo_plan = String()
    id_suscripcion = String()

class EventoSuscripcionCreada(EventoIntegracion):
    data = SuscripcionCreadaPayload()
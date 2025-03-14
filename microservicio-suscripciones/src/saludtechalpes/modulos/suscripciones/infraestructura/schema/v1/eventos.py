from pulsar.schema import *
from saludtechalpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class SuscripcionCreadaPayload(Record):
    codigo_cliente = String()
    codigo_plan = String()
    id_suscripcion = String()

class EventoSuscripcionCreada(EventoIntegracion):
    data = SuscripcionCreadaPayload()

class SuscripcionFallidaPayload(Record):
    id_suscripcion = String()

class EventoSuscripcionFallida(EventoIntegracion):
    data = SuscripcionFallidaPayload()

class SuscripcionEliminadaPayload(Record):
    id_suscripcion = String()

class EventoSuscripcionEliminada(EventoIntegracion):
    data = SuscripcionEliminadaPayload()
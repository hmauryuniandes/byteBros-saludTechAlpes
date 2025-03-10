from pulsar.schema import *
from saludtechalpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class InfraestructuraCreadaPayload(Record):
    id_serviciodatos = String()
    id_suscripcion = string()

class EventoInfraestructuraCreada(EventoIntegracion):
    data = InfraestructuraCreadaPayload()

class InfraestructuraNoCreadaPayload(Record):
    id_suscripcion = String()

class EventoInfraestructuraNoCreada(EventoIntegracion):
    data = InfraestructuraNoCreadaPayload()
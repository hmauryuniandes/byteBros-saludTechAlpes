from pulsar.schema import *
from saludtechalpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class ServicioDatosCreadaPayload(Record):
    id_serviciodatos = String()

class EventoServicioDatosCreada(EventoIntegracion):
    data = ServicioDatosCreadaPayload()
from pulsar.schema import *
from saludtechalpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

# Suscripciones
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

# Servicios de datos
class InfraestructuraCreadaPayload(Record):
    id_serviciodatos = String()
    id_suscripcion = String()

class EventoInfraestructuraCreada(EventoIntegracion):
    data = InfraestructuraCreadaPayload()

class InfraestructuraNoCreadaPayload(Record):
    id_suscripcion = String()

class EventoInfraestructuraNoCreada(EventoIntegracion):
    data = InfraestructuraNoCreadaPayload()

class InfraestructuraEliminadaPayload(Record):
    id_serviciodatos = String()
    id_suscripcion = String()

class EventoInfraestructuraEliminada(EventoIntegracion):
    data = InfraestructuraEliminadaPayload()    
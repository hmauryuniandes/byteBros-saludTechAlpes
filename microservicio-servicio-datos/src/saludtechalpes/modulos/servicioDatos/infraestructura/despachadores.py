import pulsar
from pulsar.schema import *

from saludtechalpes.modulos.servicioDatos.infraestructura.schema.v1.eventos import EventoInfraestructuraCreada, InfraestructuraCreadaPayload, EventoInfraestructuraNoCreada, InfraestructuraNoCreadaPayload, EventoInfraestructuraEliminada, InfraestructuraEliminadaPayload
from saludtechalpes.modulos.servicioDatos.infraestructura.schema.v1.comandos import ComandoCrearInfraestructura, ComandoCompensacionCrearInfraestructuraPayload
from saludtechalpes.seedwork.infraestructura import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=schema)
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        if type(evento).__name__ == "InfraestructuraCreada":
            payload = InfraestructuraCreadaPayload(
                id_serviciodatos = str(evento.id_serviciodatos),
                id_suscripcion=str(evento.id_suscripcion)
            )
            evento_integracion = EventoInfraestructuraCreada(data=payload)
            self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoInfraestructuraCreada))
        
        if type(evento).__name__ == "InfraestruraNoCreada":
            payload = InfraestructuraNoCreadaPayload(
                id_suscripcion=str(evento.id_suscripcion)
            )
            evento_integracion = EventoInfraestructuraNoCreada(data=payload)
            self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoInfraestructuraNoCreada))

        if type(evento).__name__ == "InfraestructuraEliminada":
            payload = InfraestructuraEliminadaPayload(
                id_suscripcion=str(evento.id_suscripcion)
            )
            evento_integracion = EventoInfraestructuraEliminada(data=payload)
            self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoInfraestructuraEliminada))


    def publicar_comando(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        payload = ComandoCompensacionCrearInfraestructuraPayload(
            id_usuario=str(comando.id_usuario)
            # agregar itinerarios
        )
        comando_integracion = ComandoCrearInfraestructura(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearInfraestructura))
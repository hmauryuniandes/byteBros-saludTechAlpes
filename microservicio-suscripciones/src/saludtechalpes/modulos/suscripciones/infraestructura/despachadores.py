import pulsar
from pulsar.schema import *

from saludtechalpes.modulos.suscripciones.infraestructura.schema.v1.eventos import EventoSuscripcionCreada, EventoSuscripcionEliminada, EventoSuscripcionFallida, SuscripcionCreadaPayload, SuscripcionEliminadaPayload, SuscripcionFallidaPayload
from saludtechalpes.modulos.suscripciones.infraestructura.schema.v1.comandos import ComandoCrearSuscripcion, ComandoCrearSuscripcionPayload
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
        if type(evento).__name__ == "SuscripcionCreada":
            payload = SuscripcionCreadaPayload(
                codigo_cliente=str(evento.codigo_cliente), 
                codigo_plan=str(evento.codigo_plan), 
                id_suscripcion=str(evento.id_suscripcion)
            )
            evento_integracion = EventoSuscripcionCreada(data=payload)
            self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoSuscripcionCreada))
        
        if type(evento).__name__ == "SuscripcionFallida":
            payload = SuscripcionFallidaPayload(
                id_suscripcion=str(evento.id_suscripcion)
            )
            evento_integracion = EventoSuscripcionFallida(data=payload)
            self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoSuscripcionFallida))

        if type(evento).__name__ == "SuscripcionEliminada":
            payload = SuscripcionEliminadaPayload(
                id_suscripcion=str(evento.id_suscripcion)
            )
            evento_integracion = EventoSuscripcionEliminada(data=payload)
            self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoSuscripcionFallida))


    def publicar_comando(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        payload = ComandoCrearSuscripcionPayload(
            id_usuario=str(comando.id_usuario)
            # agregar itinerarios
        )
        comando_integracion = ComandoCrearSuscripcion(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearSuscripcion))

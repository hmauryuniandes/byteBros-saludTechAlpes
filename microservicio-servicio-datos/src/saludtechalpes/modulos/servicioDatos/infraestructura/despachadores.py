import pulsar
from pulsar.schema import *

from saludtechalpes.modulos.servicioDatos.infraestructura.schema.v1.eventos import EventoServicioDatosCreada, ServicioDatosCreadaPayload
from saludtechalpes.modulos.servicioDatos.infraestructura.schema.v1.comandos import ComandoCrearServicioDatos, ComandoCrearServicioDatosPayload
from saludtechalpes.seedwork.infraestructura import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        print(f'########### enviando mensaje -> {topico}') 
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoServicioDatosCreada))
        publicador.send(mensaje)
        print(f'########### mensaje enviado -> {topico}') 
        cliente.close()

    def publicar_evento(self, evento, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del evento
        print(f'########### enviando evento -> {topico}') 
        payload = ServicioDatosCreadaPayload(
            id_serviciodatos=str(evento.id_serviciodatos)
        )
        evento_integracion = EventoServicioDatosCreada(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoServicioDatosCreada))
        print(f'########### evento enviado -> {topico}') 


    def publicar_comando(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        payload = ComandoCrearServicioDatosPayload(
            id_usuario=str(comando.id_usuario)
            # agregar itinerarios
        )
        comando_integracion = ComandoCrearServicioDatos(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearServicioDatos))

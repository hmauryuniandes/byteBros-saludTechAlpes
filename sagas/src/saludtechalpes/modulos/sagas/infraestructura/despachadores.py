import uuid
import pulsar
from pulsar.schema import *

from saludtechalpes.modulos.sagas.infraestructura.schema.v1.eventos import EventoSuscripcionCreada, EventoSuscripcionEliminada, EventoSuscripcionFallida, SuscripcionCreadaPayload, SuscripcionEliminadaPayload, SuscripcionFallidaPayload
from saludtechalpes.seedwork.infraestructura import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def publicar_mensaje(self, mensaje, topico, schema):
        json_schema = utils.consultar_schema_registry(schema)  
        avro_schema = utils.obtener_schema_avro_de_diccionario(json_schema)

        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=avro_schema)
        publicador.send(mensaje)
        cliente.close()

    
    # Comandos: 

    def publicar_comando(self, comando, topico):
        comando = dict(
            id = str(uuid.uuid4()),
            time=utils.time_millis(),
            specversion = "v1",
            type = str(type(comando).__name__),
            ingestion=utils.time_millis(),
            datacontenttype="AVRO",
            service_name = "BFF Web",
            data = comando.data.__dict__
        )
        print(f'Enviando Comando {str(type(comando).__name__)}')
        self.publicar_mensaje(comando, topico, f"public/default/{topico}")


          
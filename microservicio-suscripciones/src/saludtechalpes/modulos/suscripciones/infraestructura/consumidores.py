import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback

from saludtechalpes.modulos.suscripciones.aplicacion.comandos.crear_suscripcion import CrearSuscripcion
from saludtechalpes.modulos.suscripciones.infraestructura.schema.v1.eventos import EventoSuscripcionCreada
from saludtechalpes.modulos.suscripciones.infraestructura.schema.v1.comandos import ComandoCrearSuscripcion
from saludtechalpes.seedwork.infraestructura import utils
from saludtechalpes.seedwork.aplicacion.comandos import ejecutar_commando
from saludtechalpes.modulos.suscripciones.aplicacion.mapeadores import MapeadorSuscripcionDTOJson

def suscribirse_a_eventos():
    cliente = None
    try:
        print(f'########## suscribirse_a_eventos')

        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-suscripcion', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='saludtechalpes-sub-eventos', schema=AvroSchema(EventoSuscripcionCreada))
        
        print(f'########## Esperando eventos')

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido: {mensaje.value().data}')
            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-suscripcion', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='saludtechalpes-sub-comandos', schema=AvroSchema(ComandoCrearSuscripcion))

        while True:
            mensaje = consumidor.receive()
            valor = mensaje.value()

            print(f'Comando recibido: {mensaje.value()}')

            try:
                with app.app_context():
                    suscripcion_dict = valor

                    map_suscripcion = MapeadorSuscripcionDTOJson()
                    suscripcion_dto = map_suscripcion.externo_a_dto(suscripcion_dict)

                    comando = CrearSuscripcion(suscripcion_dto.cliente, suscripcion_dto.plan, suscripcion_dto.id, suscripcion_dto.facturas)
                    ejecutar_commando(comando)
            except:
                logging.error('ERROR: Procesando comando!')
                traceback.print_exc()

            consumidor.acknowledge(mensaje)         
            
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()
import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback

from saludtechalpes.modulos.sagas.aplicacion.comandos.iniciar_suscripcion import IniciarSuscripcion
from saludtechalpes.modulos.sagas.infraestructura.schema.v1.eventos import EventoSuscripcionCreada, EventoSuscripcionFallida
from saludtechalpes.modulos.sagas.infraestructura.schema.v1.comandos import ComandoCrearSuscripcion
from saludtechalpes.seedwork.infraestructura import utils
from saludtechalpes.seedwork.aplicacion.comandos import ejecutar_commando

def suscribirse_a_evento_suscription_creada():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-suscripcion-creada', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='saludtechalpes-sub-eventos', schema=AvroSchema(EventoSuscripcionCreada))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido - EventoSuscripcionCreada: {mensaje.value().data}')
            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos-suscripcion-creada!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_evento_suscription_fallida():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-suscripcion-fallida', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='saludtechalpes-sub-eventos', schema=AvroSchema(EventoSuscripcionFallida))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido - EventoSuscripcionFallida: {mensaje.value().data}')
            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos-suscripcion-creada!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-iniciar-suscripcion', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='saludtechalpes-sub-comandos', schema=AvroSchema(ComandoCrearSuscripcion))

        while True:
            mensaje = consumidor.receive()
            valor = mensaje.value()

            print(f'Comando recibido: {valor.data.__dict__}')

            try:
                with app.app_context():
                    suscripcion_dict = valor.data.__dict__
                    comando = IniciarSuscripcion(suscripcion_dict)
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
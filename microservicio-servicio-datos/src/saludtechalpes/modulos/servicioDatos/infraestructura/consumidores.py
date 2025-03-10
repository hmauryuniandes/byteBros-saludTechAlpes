import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback

from saludtechalpes.modulos.servicioDatos.aplicacion.comandos.compensacion_crear_infraestructura import CompensacionCrearInfraestructura
from saludtechalpes.modulos.servicioDatos.aplicacion.comandos.crear_infraestructura import CrearInfraestrctura
from saludtechalpes.modulos.servicioDatos.infraestructura.schema.v1.eventos import EventoInfraestructuraCreada, EventoInfraestructuraNoCreada
from saludtechalpes.modulos.servicioDatos.infraestructura.schema.v1.comandos import ComandoCrearInfraestructura, ComandoCompensacionCrearInfraestructura
from saludtechalpes.seedwork.infraestructura import utils
from saludtechalpes.seedwork.aplicacion.comandos import ejecutar_commando
from saludtechalpes.modulos.servicioDatos.aplicacion.mapeadores import MapeadorServicioDatosDTOJson

def suscribirse_a_evento_infraestructura_creada():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-infraestructura-creada', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='saludtechalpes-sub-eventos', schema=AvroSchema(EventoInfraestructuraCreada))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido - EventoInfraestructuraCreada: {mensaje.value().data}')
            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos-infraestructura-creada!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_evento_infraestructura_no_creada():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-infraestructura-no-creada', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='saludtechalpes-sub-eventos', schema=AvroSchema(EventoInfraestructuraNoCreada))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido - EventoInfraestructuraNoCreada: {mensaje.value().data}')
            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos-infraestructura-no-creada!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-crear-infraestructura', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='saludtechalpes-sub-comandos', schema=AvroSchema(ComandoCrearInfraestructura))

        while True:
            mensaje = consumidor.receive()
            valor = mensaje.value()

            print(f'Comando recibido: {valor.data.__dict__}')
            try:
                with app.app_context():
                    serviciodatos_dict = valor.data.__dict__
                    map_serviciodatos = MapeadorServicioDatosDTOJson()
                    serviciodatos_dto = map_serviciodatos.externo_a_dto(serviciodatos_dict)
                    
                    comando = CrearInfraestrctura(suscripcion=serviciodatos_dto.suscripcion, id=serviciodatos_dto.id)
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

def suscribirse_a_compensacion_comandos(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-compensacion-crear-infraestructura', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='saludtechalpes-sub-comandos', schema=AvroSchema(ComandoCompensacionCrearInfraestructura))

        while True:
            mensaje = consumidor.receive()
            valor = mensaje.value()

            print(f'Comando recibido: {valor.data.__dict__}')

            try:
                with app.app_context():
                    serviciodatos_dict = valor.data.__dict__

                    comando = CompensacionCrearInfraestructura(id=serviciodatos_dict.get('id_serviciodatos'),id_suscripcio=serviciodatos_dict.get('id_suscripcion'))
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
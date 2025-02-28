from pydispatch import dispatcher

from .handlers import HandlerSuscripcionIntegracion

from saludtechalpes.modulos.suscripciones.dominio.eventos import SuscripcionCreada

print(f'########### dispatcher -> {SuscripcionCreada.__name__}Integracion') 
dispatcher.connect(HandlerSuscripcionIntegracion.handle_suscripcion_creada, signal=f'{SuscripcionCreada.__name__}Integracion')
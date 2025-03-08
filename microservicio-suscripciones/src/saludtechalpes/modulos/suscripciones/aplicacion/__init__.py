from pydispatch import dispatcher

from .handlers import HandlerSuscripcionIntegracion

from saludtechalpes.modulos.suscripciones.dominio.eventos import SuscripcionCreada, SuscripcionFallida, SuscripcionEliminada

dispatcher.connect(HandlerSuscripcionIntegracion.handle_suscripcion_creada, signal=f'{SuscripcionCreada.__name__}Dominio')
dispatcher.connect(HandlerSuscripcionIntegracion.handle_suscripcion_fallida, signal=f'{SuscripcionFallida.__name__}Dominio')
dispatcher.connect(HandlerSuscripcionIntegracion.handle_suscripcion_eliminada, signal=f'{SuscripcionEliminada.__name__}Dominio')
dispatcher.connect(HandlerSuscripcionIntegracion.handle_suscripcion_creada, signal=f'{SuscripcionCreada.__name__}Integracion')

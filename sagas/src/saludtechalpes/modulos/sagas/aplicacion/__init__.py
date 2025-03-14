from pydispatch import dispatcher

from .handlers import HandlerSuscripcionComandos

from saludtechalpes.modulos.sagas.infraestructura.schema.v1.comandos import ComandoCompensacionCrearInfraestructura, ComandoCompensacionCrearSuscripcion, ComandoCrearInfraestructura, ComandoCrearSuscripcion

dispatcher.connect(HandlerSuscripcionComandos.handle_crear_suscripcion, signal=f'{ComandoCrearSuscripcion.__name__}')
dispatcher.connect(HandlerSuscripcionComandos.handle_compensacion_crear_suscripcion, signal=f'{ComandoCompensacionCrearSuscripcion.__name__}')

dispatcher.connect(HandlerSuscripcionComandos.handle_crear_infraestructura, signal=f'{ComandoCrearInfraestructura.__name__}')
dispatcher.connect(HandlerSuscripcionComandos.handle_compensacion_crear_infraestructura, signal=f'{ComandoCompensacionCrearInfraestructura.__name__}')
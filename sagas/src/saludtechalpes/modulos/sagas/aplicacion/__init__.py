from pydispatch import dispatcher

from .handlers import HandlerSuscripcionComandos

from saludtechalpes.modulos.sagas.infraestructura.schema.v1.comandos import ComandoCrearSuscripcion

dispatcher.connect(HandlerSuscripcionComandos.handle_crear_suscripcion, signal=f'{ComandoCrearSuscripcion.__name__}')
from pydispatch import dispatcher

from .handlers import HandlerServicioDatosIntegracion 

from saludtechalpes.modulos.servicioDatos.dominio.eventos import ServicioDatosCreada

dispatcher.connect(HandlerServicioDatosIntegracion.handle_servicio_datos_creada, signal=f'{ServicioDatosCreada.__name__}Integracion')
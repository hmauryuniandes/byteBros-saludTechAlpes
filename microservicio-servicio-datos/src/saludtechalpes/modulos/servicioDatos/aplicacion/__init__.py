from pydispatch import dispatcher

from .handlers import HandlerServicioDatosIntegracion 

from saludtechalpes.modulos.servicioDatos.dominio.eventos import ServicioDatosCreada

print(f'########### dispatcher -> {ServicioDatosCreada.__name__}Integracion') 
dispatcher.connect(HandlerServicioDatosIntegracion.handle_servicio_datos_creada, signal=f'{ServicioDatosCreada.__name__}Integracion')
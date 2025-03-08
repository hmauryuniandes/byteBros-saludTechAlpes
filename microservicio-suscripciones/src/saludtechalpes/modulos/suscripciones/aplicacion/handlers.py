from saludtechalpes.seedwork.aplicacion.handlers import Handler
from saludtechalpes.modulos.suscripciones.infraestructura.despachadores import Despachador

class HandlerSuscripcionIntegracion(Handler):

    @staticmethod
    def handle_suscripcion_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-suscripcion-creada')
    
    @staticmethod
    def handle_suscripcion_fallida(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-suscripcion-fallida')

    @staticmethod
    def handle_suscripcion_eliminada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-suscripcion-eliminada')
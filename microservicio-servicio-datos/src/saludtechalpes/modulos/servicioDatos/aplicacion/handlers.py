from saludtechalpes.seedwork.aplicacion.handlers import Handler
from saludtechalpes.modulos.servicioDatos.infraestructura.despachadores import Despachador

class HandlerServicioDatosIntegracion(Handler):

    @staticmethod
    def handle_servicio_datos_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-servicio-datos')

    @staticmethod
    def handle_infraestructura_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-infraestructura-creada')

    @staticmethod
    def handle_infraestructura_no_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-infraestructura-no-creada')

    @staticmethod
    def handle_infraestructura_eliminada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-infraestructura-eliminada')
    
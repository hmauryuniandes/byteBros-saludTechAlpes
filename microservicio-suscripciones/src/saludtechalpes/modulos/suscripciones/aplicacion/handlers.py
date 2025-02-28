from saludtechalpes.seedwork.aplicacion.handlers import Handler
from saludtechalpes.modulos.suscripciones.infraestructura.despachadores import Despachador

class HandlerSuscripcionIntegracion(Handler):

    @staticmethod
    def handle_suscripcion_creada(evento):
        print(f'########### handle_suscripcion_creada -> {evento}') 
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-suscripcion')
    
from saludtechalpes.seedwork.aplicacion.handlers import Handler
from saludtechalpes.modulos.suscripciones.infraestructura.despachadores import Despachador

class HandlerSuscripcionComandos(Handler):

    @staticmethod
    def handle_crear_suscripcion(comando):
        despachador = Despachador()
        despachador.publicar_comando(comando, 'comandos-crear-suscripcion')
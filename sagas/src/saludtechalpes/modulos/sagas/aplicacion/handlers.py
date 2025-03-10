from saludtechalpes.seedwork.aplicacion.handlers import Handler
from saludtechalpes.modulos.sagas.infraestructura.despachadores import Despachador

class HandlerSuscripcionComandos(Handler):

    @staticmethod
    def handle_crear_suscripcion(comando):
        despachador = Despachador()
        despachador.publicar_comando(comando, 'comandos-crear-suscripcion')

    @staticmethod
    def handle_compensacion_crear_suscripcion(comando):
        despachador = Despachador()
        despachador.publicar_comando(comando, 'comandos-compensacion-crear-suscripcion')
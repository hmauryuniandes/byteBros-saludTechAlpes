from saludtechalpes.seedwork.aplicacion.comandos import Comando
from dataclasses import dataclass
from saludtechalpes.seedwork.aplicacion.comandos import ejecutar_commando as comando

from saludtechalpes.modulos.sagas.aplicacion.coordinadores.saga_suscripciones import CoordinadorSuscripciones

@dataclass
class IniciarSuscripcion(Comando):
    data: dict

class IniciarSuscripcionHandler():
    
    def handle(self, comando: IniciarSuscripcion):
        # try: 
            saga = CoordinadorSuscripciones(comando.data.get('id_suscripcion'))
            saga.iniciar(comando)
        # except:
        #     print('Error comando IniciarSuscripcion')

@comando.register(IniciarSuscripcion)
def ejecutar_comando_crear_suscripcion(comando: IniciarSuscripcion):
    handler = IniciarSuscripcionHandler()
    handler.handle(comando)
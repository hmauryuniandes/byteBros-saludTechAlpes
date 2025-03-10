from saludtechalpes.seedwork.aplicacion.comandos import Comando
from dataclasses import dataclass
from saludtechalpes.seedwork.aplicacion.comandos import ejecutar_commando as comando

from saludtechalpes.modulos.sagas.aplicacion.coordinadores.saga_suscripciones import CoordinadorSuscripciones

@dataclass
class IniciarSuscripcion(Comando):
    cliente_codigo: str
    cliente_nombres: str
    cliente_apellidos: str
    cliente_usuario: str
    cliente_rut: str
    cliente_cedula: str
    cliente_email: str
    plan_codigo: str
    plan_nombre: str
    id_suscripcion: str

class IniciarSuscripcionHandler():
    
    def handle(self, comando: IniciarSuscripcion):
        # try: 
            saga = CoordinadorSuscripciones(comando.id_suscripcion)
            saga.iniciar(comando)
        # except:
        #     print('Error comando IniciarSuscripcion')

@comando.register(IniciarSuscripcion)
def ejecutar_comando_crear_suscripcion(comando: IniciarSuscripcion):
    handler = IniciarSuscripcionHandler()
    handler.handle(comando)
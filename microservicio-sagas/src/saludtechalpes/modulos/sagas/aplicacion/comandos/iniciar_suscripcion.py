from saludtechalpes.seedwork.aplicacion.comandos import Comando
from dataclasses import dataclass
from saludtechalpes.seedwork.aplicacion.comandos import ejecutar_commando as comando

from saludtechalpes.modulos.sagas.aplicacion.coordinadores.saga_suscripciones import CoordinadorSuscripciones
from saludtechalpes.modulos.sagas.infraestructura.schema.v1.comandos import ComandoCrearSuscripcion, ComandoCrearSuscripcionPayload
from saludtechalpes.modulos.sagas.infraestructura.despachadores import Despachador
from pydispatch import dispatcher
@dataclass
class IniciarSuscripcion(Comando):
    data: dict

class IniciarSuscripcionHandler():
    
    def handle(self, comando: IniciarSuscripcion):
        try: 
            saga = CoordinadorSuscripciones()
            saga.inicializar_pasos()
            saga.iniciar()

            # TODO: mover este comando a la saga
            payload = ComandoCrearSuscripcionPayload(
                cliente_codigo = comando.get('cliente_codigo'),
                cliente_nombres = comando.get('cliente_nombres'),
                cliente_apellidos = comando.get('cliente_apellidos'),
                cliente_usuario = comando.get('cliente_usuario'),
                cliente_rut = comando.get('cliente_rut'),
                cliente_cedula = comando.get('cliente_cedula'),
                cliente_email = comando.get('cliente_email'),
                plan_codigo = comando.get('plan_codigo'),
                plan_nombre = comando.get('plan_nombre')
            )
            comando = ComandoCrearSuscripcion(data=payload)
            despachador = Despachador()
            despachador.publicar_comando(comando, 'eventos-suscripcion-creada')
        except:
            print('Error comando IniciarSuscripcion')

@comando.register(IniciarSuscripcion)
def ejecutar_comando_crear_suscripcion(comando: IniciarSuscripcion):
    handler = IniciarSuscripcionHandler()
    handler.handle(comando)
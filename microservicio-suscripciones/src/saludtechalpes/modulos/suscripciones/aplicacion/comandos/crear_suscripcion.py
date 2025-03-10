from saludtechalpes.seedwork.aplicacion.comandos import Comando
from saludtechalpes.modulos.suscripciones.aplicacion.dto import SuscripcionDTO, ClienteDTO, PlanDTO, FacturaDTO
from .base import CrearSuscripcionBaseHandler
from dataclasses import dataclass
from saludtechalpes.seedwork.aplicacion.comandos import ejecutar_commando as comando

from saludtechalpes.modulos.suscripciones.dominio.entidades import Suscripcion
from saludtechalpes.modulos.suscripciones.dominio.eventos import SuscripcionFallida
from saludtechalpes.modulos.suscripciones.aplicacion.mapeadores import MapeadorSuscripcion
from saludtechalpes.modulos.suscripciones.infraestructura.repositorios import RepositorioSuscripciones
from pydispatch import dispatcher
import random

@dataclass
class CrearSuscripcion(Comando):
    cliente: ClienteDTO
    plan: PlanDTO
    facturas: list[FacturaDTO]
    id: str

class CrearSuscripcionHandler(CrearSuscripcionBaseHandler):
    
    def handle(self, comando: CrearSuscripcion):
        try: 
            # Introducción de una falla aleatoria
            estado = ['normal', 'error']
            if random.choice(estado) is 'error':
                raise 'Error generado aleatoriamente'

            suscripcion_dto = SuscripcionDTO(
                    cliente=comando.cliente
                ,   plan=comando.plan
                ,   id=comando.id
                ,   facturas=comando.facturas)

            suscripcion: Suscripcion = self.fabrica_suscripciones.crear_objeto(suscripcion_dto, MapeadorSuscripcion())
            suscripcion.crear_suscripcion(suscripcion)

            repositorio = self.fabrica_repositorio.crear_objeto(RepositorioSuscripciones.__class__)

            repositorio.agregar(suscripcion)

            for evento in suscripcion.eventos:
                # dispatcher.send(signal=f'{type(evento).__name__}Dominio', evento=evento)
                dispatcher.send(signal=f'{type(evento).__name__}Integracion', evento=evento)

        except:
            eventoFallido = SuscripcionFallida(id_suscripcion=str(comando.id))
            # dispatcher.send(signal=f'{type(eventoFallido).__name__}Dominio', evento=eventoFallido)
            dispatcher.send(signal=f'{type(eventoFallido).__name__}Integracion', evento=eventoFallido)


@comando.register(CrearSuscripcion)
def ejecutar_comando_crear_suscripcion(comando: CrearSuscripcion):
    handler = CrearSuscripcionHandler()
    handler.handle(comando)
    
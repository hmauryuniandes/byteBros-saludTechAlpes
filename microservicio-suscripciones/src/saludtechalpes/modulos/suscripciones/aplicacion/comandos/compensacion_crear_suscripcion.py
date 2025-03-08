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
class CompensacionCrearSuscripcion(Comando):
    id: str

class CompensacionCrearSuscripcionHandler(CrearSuscripcionBaseHandler):
    
    def handle(self, comando: CompensacionCrearSuscripcion):
        try: 
            suscripcion = Suscripcion(id=comando.id)
            suscripcion.eliminar_suscripcion()

            repositorio = self.fabrica_repositorio.crear_objeto(RepositorioSuscripciones.__class__)
            repositorio.eliminar(suscripcion.id)

            for evento in suscripcion.eventos:
                dispatcher.send(signal=f'{type(evento).__name__}Dominio', evento=evento)
        except:
            print('Error procesando comando CompensacionCrearSuscripcion')

@comando.register(CompensacionCrearSuscripcion)
def ejecutar_comando_crear_suscripcion(comando: CompensacionCrearSuscripcion):
    handler = CompensacionCrearSuscripcionHandler()
    handler.handle(comando)
    
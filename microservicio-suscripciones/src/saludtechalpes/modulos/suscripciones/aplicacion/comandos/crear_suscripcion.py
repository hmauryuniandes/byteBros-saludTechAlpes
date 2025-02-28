from saludtechalpes.seedwork.aplicacion.comandos import Comando
from saludtechalpes.modulos.suscripciones.aplicacion.dto import SuscripcionDTO, ClienteDTO, PlanDTO, FacturaDTO
from .base import CrearSuscripcionBaseHandler
from dataclasses import dataclass, field
from saludtechalpes.seedwork.aplicacion.comandos import ejecutar_commando as comando

from saludtechalpes.modulos.suscripciones.dominio.entidades import Suscripcion
from saludtechalpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from saludtechalpes.modulos.suscripciones.aplicacion.mapeadores import MapeadorSuscripcion
from saludtechalpes.modulos.suscripciones.infraestructura.repositorios import RepositorioSuscripciones

@dataclass
class CrearSuscripcion(Comando):
    cliente: ClienteDTO
    plan: PlanDTO
    facturas: list[FacturaDTO]
    id: str

class CrearSuscripcionHandler(CrearSuscripcionBaseHandler):
    
    def handle(self, comando: CrearSuscripcion):
        suscripcion_dto = SuscripcionDTO(
                cliente=comando.cliente
            ,   plan=comando.plan
            ,   id=comando.id
            ,   facturas=comando.facturas)

        suscripcion: Suscripcion = self.fabrica_suscripciones.crear_objeto(suscripcion_dto, MapeadorSuscripcion())
        suscripcion.crear_suscripcion(suscripcion)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioSuscripciones.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, suscripcion)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(CrearSuscripcion)
def ejecutar_comando_crear_suscripcion(comando: CrearSuscripcion):
    handler = CrearSuscripcionHandler()
    handler.handle(comando)
    
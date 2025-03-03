from saludtechalpes.seedwork.aplicacion.comandos import Comando
from saludtechalpes.modulos.servicioDatos.aplicacion.dto import SuscripcionDTO, ExpertoDTO, NubeDTO, DataSetDTO, ServicioDatosDTO
from .base import CrearServicioDatosBaseHandler
from dataclasses import dataclass, field
from saludtechalpes.seedwork.aplicacion.comandos import ejecutar_commando as comando

from saludtechalpes.modulos.servicioDatos.dominio.entidades import ServicioDatos
from saludtechalpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from saludtechalpes.modulos.servicioDatos.aplicacion.mapeadores import MapeadorServicioDatos
from saludtechalpes.modulos.servicioDatos.infraestructura.repositorios import RepositorioServicioDatos

@dataclass
class CrearServicioDatos(Comando):
    suscripcion: SuscripcionDTO
    experto: ExpertoDTO
    nube: NubeDTO
    dataset: DataSetDTO
    id: str

class CrearServicioDatosHandler(CrearServicioDatosBaseHandler):
    
    def handle(self, comando: CrearServicioDatos):
        serviciodatos_dto = ServicioDatosDTO(
                suscripcion=comando.suscripcion
            ,   experto=comando.experto
            ,   nube=comando.nube
            ,   dataset=comando.dataset
            ,   id=comando.id)

        serviciodatos: ServicioDatos = self.fabrica_serviciodatos.crear_objeto(serviciodatos_dto, MapeadorServicioDatos())
        serviciodatos.crear_servicio_datos(serviciodatos)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioServicioDatos.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, serviciodatos)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(CrearServicioDatos)
def ejecutar_comando_crear_servicio_datos(comando: CrearServicioDatos):
    handler = CrearServicioDatosHandler()
    handler.handle(comando)
    
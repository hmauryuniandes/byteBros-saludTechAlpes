from saludtechalpes.seedwork.aplicacion.comandos import Comando
from saludtechalpes.modulos.servicioDatos.aplicacion.dto import SuscripcionDTO, ExpertoDTO, NubeDTO, DataSetDTO, ServicioDatosDTO
from .base import CrearServicioDatosBaseHandler
from dataclasses import dataclass, field
from saludtechalpes.seedwork.aplicacion.comandos import ejecutar_commando as comando

from saludtechalpes.modulos.servicioDatos.dominio.entidades import ServicioDatos
from saludtechalpes.modulos.servicioDatos.dominio.eventos import InfraestrucraNoCreada
from saludtechalpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from saludtechalpes.modulos.servicioDatos.aplicacion.mapeadores import MapeadorServicioDatos
from saludtechalpes.modulos.servicioDatos.infraestructura.repositorios import RepositorioServicioDatos
from pydispatch import dispatcher

@dataclass
class CrearInfraestrctura(Comando):
    suscripcion: SuscripcionDTO
    experto: ExpertoDTO
    nube: NubeDTO
    dataset: DataSetDTO
    id: str

class CrearInfraestrcturaHandler(CrearServicioDatosBaseHandler):
    
    def handle(self, comando: CrearInfraestrctura):
        try:
            serviciodatos_dto = ServicioDatosDTO(
                    suscripcion=comando.suscripcion
                ,   experto=comando.experto
                ,   nube=comando.nube
                ,   dataset=comando.dataset
                ,   id=comando.id)

            serviciodatos: ServicioDatos = self.fabrica_serviciodatos.crear_objeto(serviciodatos_dto, MapeadorServicioDatos())
            serviciodatos.crear_infraestructura(serviciodatos)

            repositorio = self.fabrica_repositorio.crear_objeto(RepositorioServicioDatos.__class__)
            repositorio.agregar(serviciodatos)
            for evento in serviciodatos.eventos:
                #dispatcher.send(signal=f'{type(evento).__name__}Dominio', evento=evento)
                dispatcher.send(signal=f'{type(evento).__name__}Integracion', evento=evento)
        except:
            eventoFallido = InfraestrucraNoCreada(id_suscripcion=str(comando.id))
            #dispatcher.send(signal=f'{type(eventoFallido).__name__}Dominio', evento=eventoFallido)
            dispatcher.send(signal=f'{type(eventoFallido).__name__}Integracion', evento=eventoFallido)


@comando.register(CrearInfraestrctura)
def ejecutar_comando_crear_servicio_datos(comando: CrearInfraestrctura):
    handler = CrearInfraestrcturaHandler()
    handler.handle(comando)
    
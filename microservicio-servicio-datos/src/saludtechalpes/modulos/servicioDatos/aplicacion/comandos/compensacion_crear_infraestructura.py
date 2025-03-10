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

class CompensacionCrearInfraestructura(Comando):
    id: str
    id_suscripcion: str

class CompensacionCrearInfraestructuraHandler(CrearServicioDatosBaseHandler):
    
    def handle(self, comando: CompensacionCrearInfraestructura):
        try: 
            suscripcion = ServicioDatos(id=comando.id)
            suscripcion.eliminar_infraestructura()

            repositorio = self.fabrica_repositorio.crear_objeto(RepositorioServicioDatos.__class__)
            repositorio.eliminar(suscripcion.id)

            for evento in suscripcion.eventos:
                # dispatcher.send(signal=f'{type(evento).__name__}Dominio', evento=evento)
                dispatcher.send(signal=f'{type(evento).__name__}Integracion', evento=evento)
        except:
            print('Error procesando comando CompensacionCrearSuscripcion')

@comando.register(CompensacionCrearInfraestructura)
def ejecutar_comando_crear_suscripcion(comando: CompensacionCrearInfraestructura):
    handler = CompensacionCrearInfraestructuraHandler()
    handler.handle(comando)
    
from saludtechalpes.seedwork.aplicacion.servicios import Servicio
from saludtechalpes.modulos.suscripciones.dominio.entidades import Suscripcion
from saludtechalpes.modulos.suscripciones.dominio.fabricas import FabricaSuscripciones
from saludtechalpes.modulos.suscripciones.infraestructura.fabricas import FabricaRepositorio
from saludtechalpes.modulos.suscripciones.infraestructura.repositorios import RepositorioSuscripciones
from .mapeadores import MapeadorSuscripcion

from .dto import SuscripcionDTO

class ServicioSuscripcion(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_suscripciones: FabricaSuscripciones = FabricaSuscripciones()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_suscripciones(self):
        return self._fabrica_suscripciones

    def crear_suscripcion(self, suscripcion_dto: SuscripcionDTO) -> SuscripcionDTO:
        suscripcion: Suscripcion = self._fabrica_suscripciones.crear_objeto(suscripcion_dto, MapeadorSuscripcion())

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioSuscripciones.__class__)
        repositorio.agregar(suscripcion)

        return self._fabrica_suscripciones.crear_objeto(suscripcion, MapeadorSuscripcion())

    def obtener_suscripcion_por_id(self, id) -> SuscripcionDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioSuscripciones.__class__)
        return repositorio.obtener_por_id(id).__dict__


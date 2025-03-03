from saludtechalpes.seedwork.aplicacion.servicios import Servicio
from saludtechalpes.modulos.servicioDatos.dominio.entidades import ServicioDatos
from saludtechalpes.modulos.servicioDatos.dominio.fabricas import FabricaServiciosDatos
from saludtechalpes.modulos.servicioDatos.infraestructura.fabricas import FabricaRepositorio
from saludtechalpes.modulos.servicioDatos.infraestructura.repositorios import RepositorioServicioDatos
from .mapeadores import MapeadorServicioDatos

from .dto import ServicioDatosDTO

class ServicioServicioDatos(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_servicio_datos: FabricaServiciosDatos = FabricaServiciosDatos()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_servicio_datos(self):
        return self._fabrica_servicio_datos

    def crear_servicio_datos(self, serviciodatos_dto: ServicioDatosDTO) -> ServicioDatosDTO:
        serviciodatos: ServicioDatos = self._fabrica_servicio_datos.crear_objeto(serviciodatos_dto, MapeadorServicioDatos())

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioServicioDatos.__class__)
        repositorio.agregar(serviciodatos)

        return self._fabrica_suscripciones.crear_objeto(serviciodatos, MapeadorServicioDatos())

    def obtener_servicio_datos_por_id(self, id) -> ServicioDatosDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioServicioDatos.__class__)
        return repositorio.obtener_por_id(id).__dict__


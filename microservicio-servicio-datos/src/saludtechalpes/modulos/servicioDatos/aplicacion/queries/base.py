from saludtechalpes.seedwork.aplicacion.queries import QueryHandler
from saludtechalpes.modulos.servicioDatos.infraestructura.fabricas import FabricaRepositorio
from saludtechalpes.modulos.servicioDatos.dominio.fabricas import FabricaServiciosDatos

class ServicioDatosQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_servicio_datos: FabricaServiciosDatos = FabricaServiciosDatos()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_servicio_datos(self):
        return self._fabrica_servicio_datos  
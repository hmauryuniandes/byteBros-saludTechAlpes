from saludtechalpes.seedwork.aplicacion.comandos import ComandoHandler
from saludtechalpes.modulos.servicioDatos.infraestructura.fabricas import FabricaRepositorio
from saludtechalpes.modulos.servicioDatos.dominio.fabricas import FabricaServiciosDatos

class CrearServicioDatosBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_serviciodatos: FabricaServiciosDatos = FabricaServiciosDatos()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_serviciodatos(self):
        return self._fabrica_serviciodatos
    
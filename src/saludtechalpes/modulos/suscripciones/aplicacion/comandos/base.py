from saludtechalpes.seedwork.aplicacion.comandos import ComandoHandler
from saludtechalpes.modulos.suscripciones.infraestructura.fabricas import FabricaRepositorio
from saludtechalpes.modulos.suscripciones.dominio.fabricas import FabricaSuscripciones

class CrearSuscripcionBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_suscripciones: FabricaSuscripciones = FabricaSuscripciones()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_suscripciones(self):
        return self._fabrica_suscripciones    
    
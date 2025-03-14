""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de suscripciones

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de suscripciones

"""

from dataclasses import dataclass, field
from saludtechalpes.seedwork.dominio.fabricas import Fabrica
from saludtechalpes.seedwork.dominio.repositorios import Repositorio
from saludtechalpes.modulos.sagas.dominio.repositorios import RepositorioSagas
from .repositorios import RepositorioSagasPostgresSQL
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioSagas.__class__:
            return RepositorioSagasPostgresSQL()
        else:
            raise ExcepcionFabrica()
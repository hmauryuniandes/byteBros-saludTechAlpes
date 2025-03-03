""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de servicio de datos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de servicio de datos

"""

from dataclasses import dataclass, field
from saludtechalpes.seedwork.dominio.fabricas import Fabrica
from saludtechalpes.seedwork.dominio.repositorios import Repositorio
from saludtechalpes.modulos.servicioDatos.dominio.repositorios import RepositorioServicioDatos
from .repositorios import RepositorioServiciosDatosPostgresSQL
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioServicioDatos.__class__:
            return RepositorioServiciosDatosPostgresSQL()
        else:
            raise ExcepcionFabrica()
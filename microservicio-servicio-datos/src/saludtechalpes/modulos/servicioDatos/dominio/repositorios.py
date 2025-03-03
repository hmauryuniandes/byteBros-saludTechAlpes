""" Interfaces para los repositorios del dominio de Servicio de datos

En este archivo usted encontrará las diferentes interfaces para repositorios
del dominio de servicio de datos

"""

from abc import ABC
from saludtechalpes.seedwork.dominio.repositorios import Repositorio


class RepositorioServicioDatos(Repositorio, ABC):
    ...

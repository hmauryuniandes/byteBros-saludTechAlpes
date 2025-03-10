""" Interfaces para los repositorios del dominio de suscripcion

En este archivo usted encontrará las diferentes interfaces para repositorios
del dominio de saga

"""

from abc import ABC
from saludtechalpes.seedwork.dominio.repositorios import Repositorio


class RepositorioSagas(Repositorio, ABC):
    ...

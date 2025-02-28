""" Interfaces para los repositorios del dominio de suscripcion

En este archivo usted encontrará las diferentes interfaces para repositorios
del dominio de suscripcion

"""

from abc import ABC
from saludtechalpes.seedwork.dominio.repositorios import Repositorio


class RepositorioSuscripciones(Repositorio, ABC):
    ...

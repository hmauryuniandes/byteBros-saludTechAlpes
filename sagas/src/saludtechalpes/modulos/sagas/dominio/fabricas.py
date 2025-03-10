""" Fábricas para la creación de objetos del dominio de Saga

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de Saga

"""

from .entidades import SagaLog
from .excepciones import TipoObjetoNoExisteEnDominioSagasExcepcion
from saludtechalpes.seedwork.dominio.repositorios import Mapeador, Repositorio
from saludtechalpes.seedwork.dominio.fabricas import Fabrica
from saludtechalpes.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass


@dataclass
class _FabricaSaga(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            Saga: SagaLog = mapeador.dto_a_entidad(obj)
            return Saga

@dataclass
class FabricaSagas(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == SagaLog.__class__:
            fabrica_Saga = _FabricaSaga()
            return fabrica_Saga.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioSagasExcepcion()


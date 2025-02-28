""" Fábricas para la creación de objetos del dominio de suscripcion

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de suscripcion

"""

from .entidades import Suscripcion, Cliente
from .reglas import AlmenosUnaPlan
from .excepciones import TipoObjetoNoExisteEnDominioSuscripcionesExcepcion
from saludtechalpes.seedwork.dominio.repositorios import Mapeador, Repositorio
from saludtechalpes.seedwork.dominio.fabricas import Fabrica
from saludtechalpes.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass


@dataclass
class _FabricaSuscripcion(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            suscripcion: Suscripcion = mapeador.dto_a_entidad(obj)
            self.validar_regla(AlmenosUnaPlan(suscripcion.plan))
            return suscripcion

@dataclass
class FabricaSuscripciones(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Suscripcion.__class__:
            fabrica_suscripcion = _FabricaSuscripcion()
            return fabrica_suscripcion.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioSuscripcionesExcepcion()


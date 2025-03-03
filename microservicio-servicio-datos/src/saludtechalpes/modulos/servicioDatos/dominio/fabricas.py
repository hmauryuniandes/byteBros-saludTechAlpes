""" Fábricas para la creación de objetos del dominio de servicio de datos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de servicio de datos

"""

from .entidades import ServicioDatos, Cliente
from .reglas import AlmenosUnaPlan
from .excepciones import TipoObjetoNoExisteEnDominioServicioDatosExcepcion
from saludtechalpes.seedwork.dominio.repositorios import Mapeador, Repositorio
from saludtechalpes.seedwork.dominio.fabricas import Fabrica
from saludtechalpes.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass


@dataclass
class _FabricaServicioDatos(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            servicioDatos: ServicioDatos = mapeador.dto_a_entidad(obj)
            
            return servicioDatos

@dataclass
class FabricaServiciosDatos(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == ServicioDatos.__class__:
            fabrica_servicio_datos = _FabricaServicioDatos()
            return fabrica_servicio_datos.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioServicioDatosExcepcion()


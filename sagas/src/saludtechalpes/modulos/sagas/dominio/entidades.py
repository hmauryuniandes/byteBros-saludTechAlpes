"""Entidades del dominio de sagas

En este archivo usted encontrará las entidades del dominio de suscripcion

"""

from saludtechalpes.seedwork.dominio.entidades import AgregacionRaiz, Entidad
from dataclasses import dataclass, field

@dataclass
class SagaLog(AgregacionRaiz):
    id_correlacion: str = field(default_factory=str)
    index: int = field(default_factory=int)
    descripcion: str = field(default_factory=str)
    evento: str = field(default_factory=str)
    evento_error: str = field(default_factory=str)
    comando: str = field(default_factory=str)
    comando_compensacion: str = field(default_factory=str)
    input: str = field(default_factory=str)
    output: str = field(default_factory=str)
    exitosa: bool = field(default_factory=bool)



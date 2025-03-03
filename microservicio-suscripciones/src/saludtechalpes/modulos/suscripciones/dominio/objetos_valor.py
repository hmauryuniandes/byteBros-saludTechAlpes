"""Objetos valor del dominio de suscripcion

En este archivo usted encontrará los objetos valor del dominio de suscripcion

"""

from datetime import datetime
from saludtechalpes.seedwork.dominio.objetos_valor import ObjetoValor
from dataclasses import dataclass

@dataclass(frozen=True)
class Codigo(ObjetoValor):
    valor: str

@dataclass(frozen=True)
class Nombre(ObjetoValor):
    nombres: str
    apellidos: str

@dataclass(frozen=True)
class Usuario(ObjetoValor):
    nombre: str

@dataclass(frozen=True)
class Email(ObjetoValor):
    address: str
    dominio: str

@dataclass(frozen=True)
class Cedula(ObjetoValor):
    numero: str

@dataclass(frozen=True)
class Rut(ObjetoValor):
    numero: str

@dataclass(frozen=True)
class MedioPago(ObjetoValor):
    nombre: str
    numero: int

@dataclass(frozen=True)
class NombrePlan(ObjetoValor):
    nombre: str

@dataclass(frozen=True)
class ValorMoneda(ObjetoValor):
    moneda: str
    valor: float

@dataclass(frozen=True)
class Fecha(ObjetoValor):
    valor: datetime

@dataclass(frozen=True)
class Estado(ObjetoValor):
    valor: str



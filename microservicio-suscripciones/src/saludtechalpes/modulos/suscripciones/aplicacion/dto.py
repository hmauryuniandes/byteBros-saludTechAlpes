from dataclasses import dataclass, field
from saludtechalpes.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class ClienteDTO(DTO):
    codigo: str
    nombre: dict
    usuario: str
    rut: dict
    cedula: dict
    email: str

@dataclass(frozen=True)
class PlanDTO(DTO):
    codigo: str
    nombre: str

@dataclass(frozen=True)
class PagoDTO(DTO):
    valor: dict
    medio_pago: dict

@dataclass(frozen=True)
class FacturaDTO(DTO):
    valor_total: dict
    fecha_creacion: str
    pagos: list[PagoDTO]


@dataclass(frozen=True)
class SuscripcionDTO(DTO):
    cliente: ClienteDTO = field(default_factory=ClienteDTO)
    plan: PlanDTO = field(default_factory=PlanDTO)
    facturas: list[FacturaDTO] = field(default_factory=list[FacturaDTO])
    id: str = field(default_factory=str)
    estado: str

from dataclasses import dataclass, field
from saludtechalpes.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class ClienteDTO(DTO):
    codigo: str
    nombre: dict
    usuario: str

@dataclass(frozen=True)
class PlanDTO(DTO):
    codigo: str
    nombre: str

@dataclass(frozen=True)
class SuscripcionDTO(DTO):
    codigo: str
    cliente: ClienteDTO
    plan: PlanDTO

@dataclass(frozen=True)
class ExpertoDTO(DTO):
    codigo: str
    nombre: dict
    usuario: str
    cedula: dict
    email: str

@dataclass(frozen=True)
class TipoNubeDTO(DTO):
    codigo: str
    nombre: dict

@dataclass(frozen=True)
class NubeDTO(DTO):
    codigo: str
    nombre: dict

@dataclass(frozen=True)
class ImagenDTO(DTO):
    codigo: str
    nombre: dict

@dataclass(frozen=True)
class DataSetDTO(DTO):
    codigo: str
    nombre: dict


@dataclass(frozen=True)
class ServicioDatosDTO(DTO):
    suscripcion: SuscripcionDTO = field(default_factory=SuscripcionDTO)
    experto: ExpertoDTO = field(default_factory=ExpertoDTO)
    nube: NubeDTO = field(default_factory=NubeDTO)
    dataset: DataSetDTO = field(default_factory=DataSetDTO)
    id: str = field(default_factory=str)
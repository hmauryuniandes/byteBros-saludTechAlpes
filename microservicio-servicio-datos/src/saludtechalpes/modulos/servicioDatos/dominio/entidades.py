"""Entidades del dominio de servicio de datos

En este archivo usted encontrará las entidades del dominio de servicio de datos

"""

from saludtechalpes.modulos.servicioDatos.dominio.eventos import ServicioDatosCreada
from saludtechalpes.seedwork.dominio.entidades import AgregacionRaiz, Entidad
from dataclasses import dataclass, field
from .objetos_valor import Codigo, Fecha, Nombre, Email, Cedula, NombrePlan, Usuario, TipoNube, NombreNube, NombreImagen, NombreDataset, NombreTipoNube

@dataclass
class Cliente(Entidad):
    codigo: Codigo = field(default_factory=Codigo)
    nombre: Nombre = field(default_factory=Nombre)
    usuario: Usuario = field(default_factory=Usuario)

@dataclass
class Plan(Entidad):
    codigo: Codigo = field(default_factory=Codigo)
    nombre: NombrePlan = field(default_factory=NombrePlan)

@dataclass
class Suscripcion(Entidad):
    codigo: Codigo = field(default_factory=Codigo)
    cliente: Cliente = field(default_factory=Cliente)
    plan: Plan = field(default_factory=Plan)
    
@dataclass
class Experto(Entidad):
    codigo: Codigo = field(default_factory=Codigo)
    nombre: Nombre = field(default_factory=Nombre)
    usuario: Usuario = field(default_factory=Usuario)
    cedula: Cedula = field(default_factory=Cedula)
    email: Email = field(default_factory=Email)

@dataclass
class TipoNube(Entidad):
    codigo: Codigo = field(default_factory=Codigo)
    nombre: Nombre = field(default_factory=NombreTipoNube)

@dataclass
class Nube(Entidad):
    codigo: Codigo = field(default_factory=Codigo)
    nombre: Nombre = field(default_factory=NombreNube)

@dataclass
class Imagen(Entidad):
    codigo: Codigo = field(default_factory=Codigo)
    nombre: Nombre = field(default_factory=NombreImagen)

@dataclass
class DataSet(Entidad):
    codigo: Codigo = field(default_factory=Codigo)
    nombre: Nombre = field(default_factory=NombreDataset)

@dataclass
class ServicioDatos(AgregacionRaiz):
    suscripcion: Suscripcion = field(default_factory=Suscripcion)
    experto: Experto = field(default_factory=Experto)
    nube: Nube = field(default_factory=Nube)
    dataset: DataSet = field(default_factory=DataSet)

    def crear_servicio_datos(self, servicioDatos):
        self.suscripcion = servicioDatos.suscripcion
        self.experto = servicioDatos.experto
        self.nube = servicioDatos.nube
        self.dataset = servicioDatos.dataset

        self.agregar_evento(ServicioDatosCreada(codigo_suscripcion=self.suscripcion.codigo, codigo_experto=self.experto.codigo, codigo_nube=self.nube.codigo, codigo_data_set=self.dataset.codigo, id_serviciodatos=self.id))

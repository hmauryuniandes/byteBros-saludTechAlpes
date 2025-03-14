"""Entidades del dominio de suscripcion

En este archivo usted encontrará las entidades del dominio de suscripcion

"""

from saludtechalpes.modulos.suscripciones.dominio.eventos import SuscripcionCreada, SuscripcionEliminada
from saludtechalpes.seedwork.dominio.entidades import AgregacionRaiz, Entidad
from dataclasses import dataclass, field
from .objetos_valor import Codigo, Estado, Fecha, Nombre, Email, Cedula, NombrePlan, Rut, MedioPago, Usuario, ValorMoneda

@dataclass
class Cliente(Entidad):
    codigo: Codigo = field(default_factory=Codigo)
    nombre: Nombre = field(default_factory=Nombre)
    usuario: Usuario = field(default_factory=Usuario)
    rut: Rut = field(default_factory=Rut)
    cedula: Cedula = field(default_factory=Cedula)
    email: Email = field(default_factory=Email)

@dataclass
class Plan(Entidad):
    codigo: Codigo = field(default_factory=Codigo)
    nombre: NombrePlan = field(default_factory=NombrePlan)

@dataclass
class Pago(Entidad):
    valor: ValorMoneda = field(default_factory=ValorMoneda)
    medio_pago: MedioPago = field(default_factory=MedioPago)

@dataclass
class Factura(Entidad):
    valor_total: ValorMoneda = field(default_factory=ValorMoneda)
    fecha_creacion: Fecha = field(default_factory=Fecha)
    pagos: list[Pago] = field(default_factory=list[Pago])

@dataclass
class Suscripcion(AgregacionRaiz):
    cliente: Cliente = field(default_factory=Cliente)
    plan: Plan = field(default_factory=Plan)
    facturas: list[Factura] = field(default_factory=list[Factura])
    estado: Estado = field(default_factory=str)

    def crear_suscripcion(self, suscripcion):
        self.cliente = suscripcion.cliente
        self.plan = suscripcion.plan
        self.facturas = suscripcion.plan
        self.estado = 'Activo'

        self.agregar_evento(SuscripcionCreada(codigo_plan=self.plan.codigo.valor, codigo_cliente=self.cliente.codigo.valor, id_suscripcion=self.id))

    def eliminar_suscripcion(self):
        self.agregar_evento(SuscripcionEliminada(id_suscripcion=self.id))



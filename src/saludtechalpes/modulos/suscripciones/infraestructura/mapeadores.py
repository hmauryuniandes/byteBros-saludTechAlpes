""" Mapeadores para la capa de infrastructura del dominio de suscripcion

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from saludtechalpes.modulos.suscripciones.aplicacion.dto import PlanDTO
from saludtechalpes.modulos.suscripciones.dominio.objetos_valor import Cedula, Codigo, Email, Nombre, NombrePlan, Rut, Usuario
from saludtechalpes.seedwork.dominio.repositorios import Mapeador
from saludtechalpes.modulos.suscripciones.dominio.entidades import Cliente, Plan, Suscripcion
from .dto import Suscripcion as SuscripcionDTO
from .dto import Cliente as ClienteDTO
from .dto import Plan as PlanDTO

class MapeadorSuscripcion(Mapeador):

    def _procesar_cliente_dto(self, cliente_dto: ClienteDTO) -> Cliente:
        cliente = Cliente(id = cliente_dto.id)
        cliente.codigo = Codigo(valor=cliente_dto.codigo)
        cliente.nombre = Nombre(nombres=cliente_dto.nombres, apellidos=cliente_dto.apellidos)
        cliente.usuario = Usuario(nombre=cliente_dto.usuario)
        cliente.rut = Rut(numero=cliente_dto.numero_rut)
        cliente.cedula = Cedula(numero=cliente_dto.numero_cedula)
        cliente.email = Email(address=cliente_dto.email_address, dominio=cliente_dto.email_domain)

        return cliente

    def _procesar_cliente(self, cliente: Cliente) -> ClienteDTO:
       
        cliente_dto = ClienteDTO()
        cliente_dto.codigo = cliente.codigo.valor
        cliente_dto.nombres = cliente.nombre.nombres
        cliente_dto.apellidos = cliente.nombre.apellidos
        cliente_dto.usuario = cliente.usuario.nombre
        cliente_dto.numero_rut = cliente.rut.numero
        cliente_dto.numero_cedula = cliente.cedula.numero
        cliente_dto.email_address = cliente.email.address
        cliente_dto.email_domain = cliente.email.dominio
        cliente_dto.id = str(cliente.id)

        return cliente_dto
    
    def _procesar_plan_dto(self, plan_dto: PlanDTO) -> Plan:
        plan = Plan(id = plan_dto.id)
        plan.codigo = Codigo(valor=plan_dto.codigo)
        plan.nombre = NombrePlan(nombre=plan_dto.nombre)

        return plan

    def _procesar_plan(self, plan: Plan) -> PlanDTO:
        plan_dto = PlanDTO()
        plan_dto.codigo = plan.codigo.valor
        plan_dto.nombre = plan.nombre.nombre
        plan_dto.id = str(plan.id)

        return plan_dto

    def obtener_tipo(self) -> type:
        return Suscripcion.__class__

    def entidad_a_dto(self, entidad: Suscripcion) -> SuscripcionDTO:
        suscripcion_dto = SuscripcionDTO()
        suscripcion_dto.fecha_creacion = entidad.fecha_creacion
        suscripcion_dto.fecha_actualizacion = entidad.fecha_actualizacion
        suscripcion_dto.cliente = self._procesar_cliente(entidad.cliente)
        # suscripcion_dto.cliente_id = entidad.client.id
        suscripcion_dto.plan = self._procesar_plan(entidad.plan)
        # suscripcion_dto.plan_id = entidad.plan.id
        suscripcion_dto.fecha_actualizacion = entidad.fecha_actualizacion
        suscripcion_dto.fecha_actualizacion = entidad.fecha_actualizacion
        suscripcion_dto.id = str(entidad.id)

        return suscripcion_dto

    def dto_a_entidad(self, dto: SuscripcionDTO) -> Suscripcion:
        suscripcion = Suscripcion(id = dto.id)
        suscripcion.cliente = self._procesar_cliente_dto(dto.cliente)
        suscripcion.plan = self._procesar_plan_dto(dto.plan)
        suscripcion.fecha_creacion = dto.fecha_creacion
        suscripcion.fecha_actualizacion = dto.fecha_actualizacion

        return suscripcion
""" Mapeadores para la capa de infrastructura del dominio de servicio de datos

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from saludtechalpes.modulos.servicioDatos.aplicacion.dto import PlanDTO
from saludtechalpes.modulos.servicioDatos.dominio.objetos_valor import Cedula, Codigo, Email, Nombre, NombrePlan, Rut, Usuario
from saludtechalpes.seedwork.dominio.repositorios import Mapeador
from saludtechalpes.modulos.servicioDatos.dominio.entidades import Cliente, Plan, Suscripcion, ServicioDatos, Experto
from .dto import Suscripcion as SuscripcionDTO
from .dto import Cliente as ClienteDTO
from .dto import Plan as PlanDTO
from .dto import Experto as ExpertoDTO
from .dto import Nube as NubeDTO
from .dto import TipoNube as TipoNubeDTO
from .dto import Imagen as ImagenDTO
from .dto import DataSet as DataSetDTO
from .dto import ServicioDatos as ServicioDatosDTO

class MapeadorServicioDatos(Mapeador):

    def _procesar_cliente_dto(self, cliente_dto: ClienteDTO) -> Cliente:
        cliente = Cliente(id = cliente_dto.id)
        cliente.codigo = Codigo(valor=cliente_dto.codigo)
        cliente.nombre = Nombre(nombres=cliente_dto.nombres, apellidos=cliente_dto.apellidos)
        cliente.usuario = Usuario(nombre=cliente_dto.usuario)

        return cliente

    def _procesar_cliente(self, cliente: Cliente) -> ClienteDTO:
       
        cliente_dto = ClienteDTO()
        cliente_dto.codigo = cliente.codigo.valor
        cliente_dto.nombres = cliente.nombre.nombres
        cliente_dto.apellidos = cliente.nombre.apellidos
        cliente_dto.usuario = cliente.usuario.nombre
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
    
    def _procesar_suscripcion_dto(self, suscripcion_dto: SuscripcionDTO) -> Suscripcion:
        Suscripcion = SuscripcionDTO(id = suscripcion_dto.id)
        Suscripcion.codigo = Codigo(valor=suscripcion_dto.codigo)
        Suscripcion.cliente_id = Codigo(valor=suscripcion_dto.cliente_id)
        Suscripcion.cliente = self._procesar_cliente_dto(suscripcion_dto.cliente)
        Suscripcion.plan_id = Codigo(valor=suscripcion_dto.plan_id)
        Suscripcion.plan = self._procesar_plan_dto(suscripcion_dto.plan)

        return Suscripcion
    
    def _procesar_suscripcion(self, suscripcion: Suscripcion) -> SuscripcionDTO:
        suscripcion_dto = SuscripcionDTO()
        suscripcion_dto.codigo = suscripcion.codigo.valor
        # suscripcion_dto.cliente = self._procesar_cliente(suscripcion.cliente)
        suscripcion_dto.cliente_id = suscripcion.cliente.id
        # suscripcion_dto.plan = self._procesar_plan(suscripcion.plan)
        suscripcion_dto.plan_id = suscripcion.plan.id

        suscripcion_dto.id = str(suscripcion.id)

        return suscripcion_dto
    
    def _procesar_experto_dto(self, experto_dto: ExpertoDTO) -> Experto:
        experto = Experto(id = experto_dto.id)
        experto.codigo = Codigo(valor=experto_dto.codigo)
        experto.nombre = Nombre(nombres=experto_dto.nombres, apellidos=experto_dto.apellidos)
        experto.usuario = Usuario(nombre=experto_dto.usuario)
        experto.cedula = Cedula(nombre=experto_dto.numero_cedula)
        experto.email = Email(dominio=experto_dto.email_address, address=experto_dto.email_address)

        return experto

    def _procesar_experto(self, experto: Experto) -> ExpertoDTO:
       
        experto_dto = ExpertoDTO()
        experto_dto.codigo = experto.codigo.valor
        experto_dto.nombres = experto.nombre.nombres
        experto_dto.apellidos = experto.nombre.apellidos
        experto_dto.usuario = experto.usuario.nombre
        experto_dto.numero_cedula = experto.cedula
        experto_dto.email_address = experto.email.address
        experto_dto.email_domain = experto.email.dominio
        experto_dto.id = str(experto.id)

        return experto_dto

    def obtener_tipo(self) -> type:
        return ServicioDatos.__class__

    def entidad_a_dto(self, entidad: ServicioDatos) -> ServicioDatosDTO:
        serviciodatos_dto = ServicioDatosDTO()
        serviciodatos_dto.suscripcion = self._procesar_suscripcion(entidad.suscripcion)
        serviciodatos_dto.id = str(entidad.id)

        return serviciodatos_dto

    def dto_a_entidad(self, dto: ServicioDatosDTO) -> ServicioDatos:
        serviciodatos = ServicioDatos(id = dto.id)
        serviciodatos.suscripcion = self._procesar_suscripcion_dto(dto.suscripcion)

        return serviciodatos
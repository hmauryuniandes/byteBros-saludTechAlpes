from saludtechalpes.seedwork.aplicacion.dto import Mapeador as AppMap
from saludtechalpes.seedwork.dominio.repositorios import Mapeador as RepMap
from saludtechalpes.modulos.suscripciones.dominio.entidades import Factura, Plan, Suscripcion, Cliente
from saludtechalpes.modulos.suscripciones.dominio.objetos_valor import Codigo, Email, Nombre, MedioPago, NombrePlan, Rut, Usuario
from .dto import ClienteDTO, FacturaDTO, PagoDTO, PlanDTO, SuscripcionDTO

from datetime import datetime

class MapeadorSuscripcionDTOJson(AppMap):
    def _procesar_cliente(self, cliente: dict) -> ClienteDTO:
        codigo = cliente.get('codigo')
        nombre = cliente.get('nombre')
        usuario = cliente.get('usuario')
        rut = cliente.get('rut')
        cedula = cliente.get('cedula')
        email = cliente.get('email')

        return ClienteDTO(codigo, nombre, usuario, rut, cedula, email)
    
    def _procesar_plan(self, factura: dict) -> PlanDTO:
        codigo = factura.get('codigo')
        nombre = factura.get('nombre')

        return PlanDTO(codigo, nombre)
    
    def _procesar_pago(self, factura: dict) -> PagoDTO:
        valor = factura.get('valor')
        medio_pago = factura.get('medio_pago')

        return PagoDTO(valor, medio_pago)
    
    def _procesar_factura(self, factura: dict) -> FacturaDTO:
        factura_dto = FacturaDTO()
        factura_dto.valor_total = factura.get('codigo')
        factura_dto.fecha_creacion = factura.get('nombre')
        factura_dto.pagos = factura.get('usuario')

        factura_dto.pagos = list()
        for pago in factura.get('pagos', list()):
            factura_dto.pagos.append(self._procesar_pago(pago))

        return factura_dto
    
    def externo_a_dto(self, externo: dict) -> SuscripcionDTO:
        cliente = self._procesar_cliente(externo.get('cliente'))
        plan = self._procesar_plan(externo.get('plan'))


        # TODO
        # suscripcion_dto.facturas = list()
        # for factura in externo.get('facturas', list()):
        #     suscripcion_dto.facturas.append(self._procesar_factura(factura))

        return SuscripcionDTO(cliente=cliente, plan=plan)

    def dto_a_externo(self, dto: SuscripcionDTO) -> dict:
        return dto.__dict__

class MapeadorSuscripcion(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def _procesar_cliente(self, cliente: ClienteDTO) -> Cliente:
        codigo = Codigo(cliente.codigo)
        nombre = Nombre(cliente.nombre.get('nombres'), cliente.nombre.get('apellidos'))
        usuario = Usuario(cliente.usuario)
        rut = Rut(cliente.rut.get('numero'))
        cedula = Rut(cliente.cedula.get('numero'))
        email_address = cliente.email.split("@")[0]
        email_domain = cliente.email.split("@")[1]
        email = Email(email_address, email_domain)

        return Cliente(codigo=codigo, nombre=nombre, usuario=usuario, rut=rut, cedula=cedula, email=email)
    
    def _procesar_plan(self, plan: PlanDTO) -> Plan:
        codigo = Codigo(valor=plan.codigo)
        nombre = NombrePlan(nombre=plan.nombre)

        return Plan(codigo=codigo, nombre=nombre)

    def obtener_tipo(self) -> type:
        return Suscripcion.__class__


    def entidad_a_dto(self, entidad: Suscripcion) -> SuscripcionDTO:
        
        cliente = ClienteDTO(
            entidad.cliente.codigo.valor, \
            entidad.cliente.nombre.__dict__, \
            entidad.cliente.usuario.nombre, \
            entidad.cliente.rut.__dict__, \
            entidad.cliente.cedula.__dict__, \
            entidad.cliente.email.__dict__, \
        )
        plan = PlanDTO(
            entidad.plan.codigo.valor, \
            entidad.plan.nombre.nombre, \
        )
        facturas = list()
        _id = str(entidad.id)
        estado = str(entidad.estado)

        return SuscripcionDTO(cliente=cliente, plan=plan, facturas=facturas, id=_id, estado=estado)

    def dto_a_entidad(self, dto: SuscripcionDTO) -> Suscripcion:
        cliente = self._procesar_cliente(dto.cliente)
        plan = self._procesar_plan(dto.plan)
       

        #TODO
        # suscripcion.facturas = list()

        return Suscripcion(cliente=cliente, plan=plan, estado=dto.estado)




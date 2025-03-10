from saludtechalpes.seedwork.aplicacion.dto import Mapeador as AppMap
from saludtechalpes.seedwork.dominio.repositorios import Mapeador as RepMap
from saludtechalpes.modulos.servicioDatos.dominio.entidades import Plan, Suscripcion, Cliente, Experto, DataSet, ServicioDatos, Nube, TipoNube
from saludtechalpes.modulos.servicioDatos.dominio.objetos_valor import Codigo, Email, Nombre, NombrePlan, Cedula, Usuario, NombreNube, NombreImagen, NombreDataset, NombreTipoNube
from .dto import ClienteDTO, PlanDTO, SuscripcionDTO, ExpertoDTO, TipoNubeDTO, NubeDTO, ImagenDTO, DataSetDTO, ServicioDatosDTO

from datetime import datetime

class MapeadorServicioDatosDTOJson(AppMap):
    def _procesar_cliente(self, cliente: dict) -> ClienteDTO:
        codigo = cliente.get('codigo')
        nombre = cliente.get('nombre')
        usuario = cliente.get('usuario')

        return ClienteDTO(codigo, nombre, usuario)
    
    def _procesar_plan(self, plan: dict) -> PlanDTO:
        codigo = plan.get('codigo')
        nombre = plan.get('nombre')

        return PlanDTO(codigo, nombre)
    
    def _procesar_suscripcion(self, suscripcion: dict) -> SuscripcionDTO:
        id_suscripcion = suscripcion.get('id_suscripcion')
        plan = suscripcion.get('id_plan')
        cliente = suscripcion.get('id_cliente')
        return SuscripcionDTO(suscripcion=id_suscripcion, plan=plan, cliente=cliente)
    
    def _procesar_experto(self, experto: dict) -> ExpertoDTO:
        codigo = experto.get('codigo')
        nombre = experto.get('nombre')
        usuario = experto.get('usuario')
        cedula = experto.get('cedula')
        email = experto.get('email')

        return ExpertoDTO(codigo, nombre, usuario, cedula, email)
    
    def _procesar_nube(self, nube: dict) -> NubeDTO:
        codigo = nube.get('codigo')
        nombre = nube.get('nombre')

        return NubeDTO(codigo, nombre)

    def _procesar_dataset(self, dataset: dict) -> DataSetDTO:
        codigo = dataset.get('codigo')
        nombre = dataset.get('nombre')

        return DataSetDTO(codigo, nombre)
    
    def externo_a_dto(self, externo: dict) -> ServicioDatosDTO:
        suscripcion = self._procesar_suscripcion(externo)
        return ServicioDatosDTO(suscripcion=suscripcion)

    def dto_a_externo(self, dto: ServicioDatosDTO) -> dict:
        return dto.__dict__

class MapeadorServicioDatos(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def _procesar_cliente(self, cliente: ClienteDTO) -> Cliente:
        codigo = Codigo(cliente.codigo)
        nombre = Nombre(cliente.nombre.get('nombres'), cliente.nombre.get('apellidos'))
        usuario = Usuario(cliente.usuario)

        return Cliente(codigo=codigo, nombre=nombre, usuario=usuario)
    
    def _procesar_plan(self, plan: PlanDTO) -> Plan:
        codigo = Codigo(plan.codigo)
        nombre = NombrePlan(plan.nombre)

        return Plan(codigo=codigo, nombre=nombre)
    
    def _procesar_suscripcion(self, suscripcion: SuscripcionDTO) -> Suscripcion:
        codigo = Codigo(valor=suscripcion.suscripcion)
        cliente = Cliente(
            codigo=Codigo(valor=suscripcion.cliente), 
            nombre="",
            usuario=""
        )
        plan = Plan(
            codigo = Codigo(valor=suscripcion.plan),
            nombre = NombrePlan(nombre=suscripcion.plan)
        )
        return Suscripcion(codigo=codigo, cliente=cliente, plan=plan)
    
    def _procesar_experto(self, experto: ExpertoDTO) -> Experto:
        codigo = Codigo(experto.codigo)
        nombre = Nombre(experto.nombre.get('nombres'), experto.nombre.get('apellidos'))
        usuario = Usuario(experto.usuario)
        cedula = Cedula(experto.cedula.get('numero'))
        email_address = experto.email.split("@")[0]
        email_domain = experto.email.split("@")[1]
        email = Email(email_address, email_domain)

        return Experto(codigo=codigo, nombre=nombre, usuario=usuario, cedula=cedula, email=email)
    
    def _procesar_nube(self, nube: NubeDTO) -> Nube:
        codigo = Codigo(nube.codigo)
        nombre = NombreNube(nube.nombre)
        
        return Nube(codigo=codigo, nombre=nombre)
    
    def _procesar_dataset(self, dataset: DataSetDTO) -> DataSet:
        codigo = Codigo(dataset.codigo)
        nombre = NombreDataset(dataset.nombre)

        return DataSet(codigo=codigo, nombre=nombre)

    def obtener_tipo(self) -> type:
        return ServicioDatos.__class__


    def entidad_a_dto(self, entidad: ServicioDatos) -> ServicioDatosDTO:
        
        suscripcion = SuscripcionDTO(
            entidad.suscripcion.codigo.valor, \
            entidad.suscripcion.cliente.codigo, \
            entidad.suscripcion.cliente.nombre.nombres, \
            entidad.suscripcion.cliente.nombre.apellidos, \
            entidad.suscripcion.cliente.usuario, \
            entidad.suscripcion.plan.codigo, \
            entidad.suscripcion.plan.nombre, \
        )

        experto = ExpertoDTO(
            entidad.experto.codigo.valor, \
            entidad.experto.nombre.__dict__, \
            entidad.experto.usuario.nombre, \
            entidad.experto.cedula.__dict__, \
            entidad.experto.email.__dict__, \
        )

        nube = NubeDTO(
            entidad.nube.codigo.valor, \
            entidad.nube.nombre.__dict__, \
        )

        dataset = DataSetDTO(
            entidad.dataset.codigo, \
            entidad.dataset.nombre.__dict__, \
        )
        
        _id = str(entidad.id)

        return ServicioDatosDTO(suscripcion, experto, nube, dataset, _id)

    def dto_a_entidad(self, dto: ServicioDatosDTO) -> ServicioDatos:
        suscripcion = self._procesar_suscripcion(dto.suscripcion)
        return ServicioDatos(suscripcion=suscripcion)




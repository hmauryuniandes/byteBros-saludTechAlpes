""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de servicio de datos

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de servicio de datos

"""

from saludtechalpes.config.db import db
from saludtechalpes.modulos.servicioDatos.dominio.repositorios import RepositorioServicioDatos
from saludtechalpes.modulos.servicioDatos.dominio.entidades import ServicioDatos
from saludtechalpes.modulos.servicioDatos.dominio.fabricas import FabricaServiciosDatos
from .dto import ServicioDatos as ServicioDatosDTO



from .mapeadores import MapeadorServicioDatos
from uuid import UUID

class RepositorioServiciosDatosPostgresSQL(RepositorioServicioDatos):

    def __init__(self):
        self._fabrica_servicios_datos: FabricaServiciosDatos = FabricaServiciosDatos()

    @property
    def fabrica_servicio_datos(self):
        return self._fabrica_servicios_datos

    def obtener_por_id(self, id: UUID) -> ServicioDatos:
        serviciodatos_dto = db.session.query(ServicioDatosDTO).filter_by(id=str(id)).first()
        return self.fabrica_servicio_datos.crear_objeto(serviciodatos_dto, MapeadorServicioDatos())

    def obtener_todos(self) -> list[ServicioDatos]:
        # TODO
        raise NotImplementedError

    def agregar(self, servicioDatos: ServicioDatos):
        serviciodatos_dto = self.fabrica_servicio_datos.crear_objeto(servicioDatos, MapeadorServicioDatos())
        
        # cliente = db.session.query(ClienteDTO).filter_by(codigo=str(suscripcion_dto.cliente.codigo)).first()
        
        # if cliente is not None: 
        #     suscripcion_dto.cliente_id = cliente.id
        #     suscripcion_dto.cliente.id = cliente.id
        
        # plan = db.session.query(PlanDTO).filter_by(codigo=str(suscripcion_dto.plan.codigo)).first()
        
        # if plan is not None: 
        #     suscripcion_dto.plan_id = plan.id
        #     suscripcion_dto.plan.id = plan.id
            
        db.session.add(serviciodatos_dto)
        db.session.commit()

    def actualizar(self, servicioDatos: ServicioDatos):
        # TODO
        raise NotImplementedError

    def eliminar(self, servicioDatos_id: UUID):
        serviciodatos_dto = db.session.get(str(servicioDatos_id))
        db.session.delete(serviciodatos_dto)
        db.session.commit()
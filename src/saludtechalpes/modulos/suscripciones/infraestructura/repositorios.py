""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de suscripciones

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de suscripciones

"""

from saludtechalpes.config.db import db
from saludtechalpes.modulos.suscripciones.dominio.repositorios import RepositorioSuscripciones
from saludtechalpes.modulos.suscripciones.dominio.entidades import Suscripcion
from saludtechalpes.modulos.suscripciones.dominio.fabricas import FabricaSuscripciones
from .dto import Suscripcion as SuscripcionDTO
from .mapeadores import MapeadorSuscripcion
from uuid import UUID

class RepositorioSuscripcionesPostgresSQL(RepositorioSuscripciones):

    def __init__(self):
        self._fabrica_suscripciones: FabricaSuscripciones = FabricaSuscripciones()

    @property
    def fabrica_suscripciones(self):
        return self._fabrica_suscripciones

    def obtener_por_id(self, id: UUID) -> Suscripcion:
        suscripcion_dto = db.session.query(SuscripcionDTO).filter_by(id=str(id)).one()
        return self.fabrica_suscripciones.crear_objeto(suscripcion_dto, MapeadorSuscripcion())

    def obtener_todos(self) -> list[Suscripcion]:
        # TODO
        raise NotImplementedError

    def agregar(self, suscripcion: Suscripcion):
        suscripcion_dto = self.fabrica_suscripciones.crear_objeto(suscripcion, MapeadorSuscripcion())
        db.session.add(suscripcion_dto)
        db.session.commit()

    def actualizar(self, suscripcion: Suscripcion):
        # TODO
        raise NotImplementedError

    def eliminar(self, suscripcion_id: UUID):
        # TODO
        raise NotImplementedError
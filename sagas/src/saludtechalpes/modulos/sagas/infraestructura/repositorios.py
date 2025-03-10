""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de Sagas

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de Sagas

"""

import uuid
from saludtechalpes.config.db import db
from saludtechalpes.modulos.sagas.dominio.repositorios import RepositorioSagas
from saludtechalpes.modulos.sagas.dominio.entidades import SagaLog
from saludtechalpes.modulos.sagas.dominio.fabricas import FabricaSagas
from .dto import SagaLog as SagaLogDTO
from .mapeadores import MapeadorSaga

class RepositorioSagasPostgresSQL(RepositorioSagas):

    def __init__(self):
        self._fabrica_Sagas: FabricaSagas = FabricaSagas()

    @property
    def fabrica_Sagas(self):
        return self._fabrica_Sagas

    def obtener_por_id(self, id: uuid.UUID) -> SagaLog:
        # TODO
        raise NotImplementedError

    def obtener_todos(self) -> list[SagaLog]:
        # TODO
        raise NotImplementedError

    def agregar(self, saga: SagaLog):
        saga_dto: SagaLogDTO = self.fabrica_Sagas.crear_objeto(saga, MapeadorSaga())
        db.session.add(saga_dto)
        db.session.commit()

    def actualizar(self, saga: SagaLog):
        # TODO
        raise NotImplementedError

    def eliminar(self, Saga_id: uuid.UUID):
        # TODO
        raise NotImplementedError
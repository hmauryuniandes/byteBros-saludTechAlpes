""" Mapeadores para la capa de infrastructura del dominio de Saga

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

import uuid
from saludtechalpes.seedwork.dominio.repositorios import Mapeador
from saludtechalpes.modulos.sagas.dominio.entidades import SagaLog
from .dto import SagaLog as SagaDTO
class MapeadorSaga(Mapeador):

    def obtener_tipo(self) -> type:
        return SagaLog.__class__

    def entidad_a_dto(self, entidad: SagaLog) -> SagaDTO:
        saga_dto = SagaDTO()
        saga_dto.id = entidad.id
        saga_dto.index = entidad.index
        saga_dto.id_correlacion = entidad.id_correlacion
        saga_dto.descripcion = entidad.descripcion
        saga_dto.evento = entidad.evento
        saga_dto.evento_error = entidad.evento_error
        saga_dto.comando = entidad.comando
        saga_dto.comando_compensacion = entidad.comando_compensacion
        saga_dto.input = entidad.input
        saga_dto.output = entidad.output
        saga_dto.fecha_creacion = entidad.fecha_creacion
        saga_dto.exitosa = entidad.exitosa


        return saga_dto

    def dto_a_entidad(self, dto: SagaDTO) -> SagaLog:
        sagaLog = SagaLog(id = dto.id)
        sagaLog.index = dto.index
        sagaLog.id_correlacion = dto.id_correlacion
        sagaLog.descripcion = dto.descripcion
        sagaLog.evento = dto.evento
        sagaLog.evento_error = dto.evento_error
        sagaLog.comando = dto.comando
        sagaLog.comando_compensacion = dto.comando_compensacion
        sagaLog.input = dto.input
        sagaLog.output = dto.output
        sagaLog.fecha_creacion = dto.fecha_creacion
        sagaLog.exitosa = dto.exitosa

        return sagaLog
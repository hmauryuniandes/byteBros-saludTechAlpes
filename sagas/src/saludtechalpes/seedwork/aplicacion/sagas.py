from abc import ABC, abstractmethod
from saludtechalpes.modulos.sagas.dominio.fabricas import FabricaSagas
from saludtechalpes.modulos.sagas.infraestructura.fabricas import FabricaRepositorio
from saludtechalpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
from saludtechalpes.seedwork.aplicacion.comandos import Comando
from dataclasses import dataclass
import uuid
import datetime
from pydispatch import dispatcher

class CoordinadorSaga(ABC):
    id_correlacion: uuid.UUID

    @abstractmethod
    def persistir_en_saga_log(self, mensaje, inicio):
        ...

    @abstractmethod
    def construir_comando(self, evento: EventoIntegracion, tipo_comando: type) -> Comando:
        ...

    def publicar_comando(self, evento: EventoIntegracion, tipo_comando: type):
        comando = self.construir_comando(evento, tipo_comando)
        dispatcher.send(signal=f'{type(comando).__name__}', comando=comando)

    @abstractmethod
    def inicializar_pasos(self):
        ...
    
    @abstractmethod
    def procesar_evento(self, evento: EventoIntegracion):
        ...

    @abstractmethod
    def iniciar(evento):
        ...
    
    @abstractmethod
    def terminar():
        ...

class Paso():
    index: int
    id_correlacion: uuid.UUID
    fecha_evento: datetime.datetime

@dataclass
class Inicio(Paso):
    index: int = 0

@dataclass
class Fin(Paso):
    def __init__(self, index: int):
        self.index = index

@dataclass
class Transaccion(Paso):
    comando: Comando
    evento: EventoIntegracion
    error: EventoIntegracion
    compensacion: Comando
    exitosa: bool

    def __init__(self, index: int, comando: Comando, evento: EventoIntegracion, error: EventoIntegracion, compensacion: Comando):
        self.index = index
        self.comando = comando
        self.evento = evento
        self.error = error
        self.compensacion = compensacion


class CoordinadorOrquestacion(CoordinadorSaga, ABC):
    pasos: list[Paso]
    index: int

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_suscripciones: FabricaSagas = FabricaSagas()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_suscripciones(self):
        return self._fabrica_suscripciones 
    
    def obtener_paso_dado_un_evento(self, evento: EventoIntegracion):
        for i, paso in enumerate(self.pasos):
            if not isinstance(paso, Transaccion):
                continue

            if isinstance(evento, paso.evento) or isinstance(evento, paso.error):
                return paso, i
        raise Exception("Evento no hace parte de la transacción")
                
    def es_ultima_transaccion(self, index):
        return len(self.pasos) - 2 == index
    
    def es_primera_transaccion(self, index):
        return index == 1

    def procesar_evento(self, evento: EventoIntegracion):
        paso, index = self.obtener_paso_dado_un_evento(evento)

        paso.exitosa = isinstance(evento, paso.evento)
        if paso.exitosa:
            self.persistir_en_saga_log(paso, "Fin Existoso")
        else: 
            self.persistir_en_saga_log(paso, "Fin Fallido")

        if self.es_ultima_transaccion(index) and not isinstance(evento, paso.error):
            self.terminar()
        elif isinstance(evento, paso.error):
            if self.es_primera_transaccion(index):
                self.terminar()
            else:
                paso_anterior = self.pasos[index-1]
                self.persistir_en_saga_log(paso_anterior, "Compensacion")
                self.publicar_comando(evento, paso_anterior.compensacion)
                self.terminar()
        elif isinstance(evento, paso.evento):
            paso_siguiente = self.pasos[index+1]
            self.persistir_en_saga_log(paso_siguiente, "Inicio")
            self.publicar_comando(evento, paso_siguiente.comando)



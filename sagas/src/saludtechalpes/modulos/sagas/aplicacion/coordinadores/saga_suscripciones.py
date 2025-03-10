from saludtechalpes.seedwork.aplicacion.comandos import Comando
from saludtechalpes.modulos.sagas.dominio.entidades import SagaLog
from saludtechalpes.modulos.sagas.dominio.repositorios import RepositorioSagas
from saludtechalpes.modulos.sagas.infraestructura.schema.v1.comandos import ComandoCompensacionCrearSuscripcion, ComandoCompensacionCrearSuscripcionPayload, ComandoCrearSuscripcion, ComandoCrearSuscripcionPayload
from saludtechalpes.modulos.sagas.infraestructura.schema.v1.eventos import EventoSuscripcionCreada, EventoSuscripcionFallida
from saludtechalpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
from saludtechalpes.seedwork.aplicacion.sagas import CoordinadorOrquestacion, Transaccion, Inicio, Fin
from pydispatch import dispatcher

class CoordinadorSuscripciones(CoordinadorOrquestacion):

    def __init__(self, id_correlacion):
        super().__init__()
        self.id_correlacion = id_correlacion
        self.inicializar_pasos()

    def inicializar_pasos(self):
        self.pasos = [
            Inicio(index=0),
            Transaccion(index=1, comando=ComandoCrearSuscripcion, evento=EventoSuscripcionCreada, error=EventoSuscripcionFallida, compensacion=ComandoCompensacionCrearSuscripcion),
            # Transaccion(index=2, comando=ComandoCrearInfraestructura, evento=EventoInfraestructuraCreada, error=EventoInfraestructuraFallida, compensacion=ComandoCompensacionCrearInfraestructura),
            Fin(index=2)
        ]

    def iniciar(self, evento):
        paso = self.pasos[0]
        pasoSiguiente = self.pasos[1]
        self.persistir_en_saga_log(paso, 'Inicio')
        self.persistir_en_saga_log(pasoSiguiente, 'Inicio')
        self.publicar_comando(evento, pasoSiguiente.comando)
    
    def terminar(self):
        self.persistir_en_saga_log(self.pasos[-1], 'Fin')
        # publicar evento de notificacion con el resultado de la transaccion

    def persistir_en_saga_log(self, paso, estado):
        print(f'####### SAGA LOG ##### ID: {self.id_correlacion} - PASO: {paso.index}')

        sagaLog = SagaLog()
        sagaLog.id_correlacion = self.id_correlacion
        
        if sagaLog.index == 0 or sagaLog.index == len(self.pasos):
            sagaLog.descripcion = f'{estado} Saga'

        if isinstance(paso, Transaccion):
            sagaLog.index = paso.index
            sagaLog.comando=str(paso.comando.__class__)
            sagaLog.comando_compensacion=str(paso.compensacion.__class__)
            sagaLog.evento=str(paso.evento.__class__)
            sagaLog.evento_error=str(paso.error.__class__)
            sagaLog.exitosa=False
            sagaLog.descripcion = f'{estado} T{paso.index}'
            #TODO
            sagaLog.input = ''
            sagaLog.output = ''

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioSagas.__class__)
        repositorio.agregar(sagaLog)

    def construir_comando(self, evento: EventoIntegracion, tipo_comando: type) -> Comando:
        if  tipo_comando.__class__ is ComandoCrearSuscripcion.__class__:
            payload = ComandoCrearSuscripcionPayload(
                id_suscripcion = evento.data.get('id_suscripcion'),
                cliente_codigo = evento.data.get('cliente_codigo'),
                cliente_nombres = evento.data.get('cliente_nombres'),
                cliente_apellidos = evento.data.get('cliente_apellidos'),
                cliente_usuario = evento.data.get('cliente_usuario'),
                cliente_rut = evento.data.get('cliente_rut'),
                cliente_cedula = evento.data.get('cliente_cedula'),
                cliente_email = evento.data.get('cliente_email'),
                plan_codigo = evento.data.get('plan_codigo'),
                plan_nombre = evento.data.get('plan_nombre')
            )
            return ComandoCrearSuscripcion(data=payload)
        
        if  tipo_comando.__class__ is ComandoCompensacionCrearSuscripcion.__class__:
            payload = ComandoCompensacionCrearSuscripcionPayload(
                id = evento.data.get('id_suscripcion')
            )
            return ComandoCompensacionCrearSuscripcion(data=payload)
        
        raise NotImplementedError("Comando no implementado en la saga")
    
def oir_mensaje(mensaje):
    if isinstance(mensaje, EventoIntegracion):
        coordinador = CoordinadorSuscripciones(mensaje.data.id_suscripcion)
        coordinador.procesar_evento(mensaje)
    else:
        raise NotImplementedError("El mensaje no es evento de Dominio")

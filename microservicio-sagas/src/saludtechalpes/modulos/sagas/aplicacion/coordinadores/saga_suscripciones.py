from saludtechalpes.seedwork.aplicacion.sagas import CoordinadorOrquestacion, Transaccion, Inicio, Fin
from saludtechalpes.seedwork.aplicacion.comandos import Comando
from saludtechalpes.seedwork.dominio.eventos import EventoDominio

from saludtechalpes.modulos.sagas.aplicacion.comandos.crear_suscripcion import CrearSuscripcion
# from saludtechalpes.modulos.suscripciones.aplicacion.comandos.compensacion_crear_suscripcion import CompensacionCrearSuscripcion
# from saludtechalpes.modulos.suscripciones.dominio.eventos import SuscripcionCreada, SuscripcionFallida


class CoordinadorSuscripciones(CoordinadorOrquestacion):

    def inicializar_pasos(self):
        self.pasos = [
            Inicio(index=0),
            #Transaccion(index=1, comando=CrearSuscripcion, evento=SuscripcionCreada, error=SuscripcionFallida, compensacion=CompensacionCrearSuscripcion),
            Fin(index=5)
        ]

    def iniciar(self):
        self.persistir_en_saga_log(self.pasos[0])
    
    def terminar(self):
        self.persistir_en_saga_log(self.pasos[-1])
        # publicar evento de notificacion con el resultado de la transaccion

    def persistir_en_saga_log(self, mensaje):
        # TODO Persistir estado en DB
        # Probablemente usted podría usar un repositorio para ello
        ...

    def construir_comando(self, evento: EventoDominio, tipo_comando: type):
        # TODO 
        ...
        
# TODO Agregue un Listener/Handler para que se puedan redireccionar eventos de dominio
def oir_mensaje(mensaje):
    if isinstance(mensaje, EventoDominio):
        coordinador = CoordinadorSuscripciones()
        coordinador.procesar_evento(mensaje)
    else:
        raise NotImplementedError("El mensaje no es evento de Dominio")

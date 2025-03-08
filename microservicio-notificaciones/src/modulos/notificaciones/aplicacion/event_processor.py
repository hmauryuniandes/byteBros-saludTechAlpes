from src.modulos.notificaciones.aplicacion.notificacion import enviar_notificacion
from src.modulos.notificaciones.infraestructura.event_store import EventStore

class EventProcessor:
    def __init__(self, event_store: EventStore):
        self.event_store = event_store
    
    def procesar_evento(self, event):
        # Persistir el evento
        self.event_store.save_event({"evento": event})
        
       # Solo enviar notificación si el evento es de tipo "ProcesoFinalizado"
        if event == "ProcesoFinalizado":
            enviar_notificacion("La transacción ha sido finalizada exitosamente.")

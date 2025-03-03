from infraestructura.pulsar_client import PulsarClient
from aplicacion.event_processor import EventProcessor

class Consumidor:
    def __init__(self, pulsar_client, topic, subscription_name, event_store):
        self.consumer = pulsar_client.create_consumer(topic, subscription_name)
        self.event_processor = EventProcessor(event_store)
    
    def recibir_mensajes(self):
        while True:
            msg = self.consumer.receive()
            try:
                print(f"Recibido mensaje: '{msg.data()}'")
                # Procesar el mensaje (evento)
                event = msg.data().decode('utf-8')
                self.event_processor.procesar_evento(event)
                self.consumer.acknowledge(msg)
            except Exception as e:
                print(f"Error procesando mensaje: {e}")
                self.consumer.negative_acknowledge(msg)

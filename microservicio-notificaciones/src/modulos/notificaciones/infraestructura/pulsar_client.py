import atexit
import logging
import pulsar

class PulsarClient:
    def __init__(self, service_url='pulsar://broker:6650'):
        try:
            self.client = pulsar.Client(service_url)
            logging.info(f"Conexión establecida a Pulsar en {service_url}")
        except Exception as e:
            logging.error(f"Error al conectar a Pulsar: {e}")
            raise e
    
    def create_consumer(self, topic, subscription_name):
        try:
            consumer = self.client.subscribe(topic, subscription_name)
            logging.info(f"Consumidor creado para el tópico: {topic} con suscripción: {subscription_name}")
            return consumer
        except Exception as e:
            logging.error(f"Error al crear consumidor: {e}")
            raise e
    
    def close(self):
        try:
            self.client.close()
            logging.info("Cliente de Pulsar cerrado correctamente.")
        except Exception as e:
            logging.error(f"Error al cerrar cliente de Pulsar: {e}")

# Registrar cierre adecuado de la conexión cuando la aplicación termine
atexit.register(lambda: PulsarClient.close(PulsarClient()))

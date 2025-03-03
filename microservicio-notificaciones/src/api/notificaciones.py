from flask import Flask, jsonify
from src.modulos.notificaciones.infraestructura.pulsar_client import PulsarClient
from src.modulos.notificaciones.infraestructura.event_store import EventStore
from src.modulos.notificaciones.aplicacion.consumidor import Consumidor
import threading

app = Flask(__name__)

# Configuración de Pulsar
pulsar_client = PulsarClient('pulsar://broker:6650')
topic = 'suscripciones-topic'  # Tópico de eventos
subscription_name = 'notificaciones-sub'  # Nombre de la suscripción

# Event Store (Persistencia de eventos)
event_store = EventStore()

# Crear consumidor
consumidor = Consumidor(pulsar_client, topic, subscription_name, event_store)

def iniciar_consumidor():
    consumidor.recibir_mensajes()

# Iniciar el consumidor en un hilo separado para no bloquear el servidor Flask
thread = threading.Thread(target=iniciar_consumidor)
thread.start()

@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Microservicio de notificaciones en ejecución"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, )

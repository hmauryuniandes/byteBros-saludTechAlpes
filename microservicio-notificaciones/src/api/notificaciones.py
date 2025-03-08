from flask import Flask, jsonify, request
from src.modulos.notificaciones.infraestructura.pulsar_client import PulsarClient
from src.modulos.notificaciones.infraestructura.event_store import EventStore
from src.modulos.notificaciones.aplicacion.consumidor import Consumidor
from src.modulos.notificaciones.aplicacion.notificacion import enviar_notificacion  

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

@app.route('/test-notification', methods=['POST'])
def test_notification():
    """Simula la llegada de un evento para enviar una notificación"""
    try:
        # Intentamos obtener el cuerpo JSON
        data = request.json
        if not data:
            return jsonify({"error": "No se proporcionó un cuerpo JSON válido."}), 400

        event = data.get("event", "")
        if not event:
            return jsonify({"error": "No se proporcionó un evento."}), 400
        
        # Simula el evento de notificación
        enviar_notificacion(event)  # Llama a la función para enviar la notificación
        
        return jsonify({"message": f"Notificación para el evento '{event}' enviada exitosamente."}), 200

    except Exception as e:
        # Loggear el error completo para depuración
        app.logger.error(f"Error en test_notification: {e}")
        return jsonify({"error": f"Hubo un error procesando la solicitud: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, )

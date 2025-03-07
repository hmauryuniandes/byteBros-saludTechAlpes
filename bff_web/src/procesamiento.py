from datetime import datetime
import json
import uuid
import pulsar
from flask import Blueprint, request, jsonify

# Definir Blueprint para el procesamiento
bp = Blueprint('procesamiento', __name__, url_prefix='/procesamiento')

# Configuración de Apache Pulsar
PULSAR_BROKER_URL = 'pulsar://broker:6650'  # Asegúrate de que esta URL sea correcta
TOPIC_ANONIMIZACION = 'anonimizacion'

def publicar_mensaje(mensaje, topico):
    """
    Publica un mensaje en Apache Pulsar en el tópico indicado.
    """
    cliente = pulsar.Client(PULSAR_BROKER_URL)
    publicador = cliente.create_producer(topico)

    try:
        mensaje_json = json.dumps(mensaje).encode('utf-8')
        publicador.send(mensaje_json)
        print(f"✅ Mensaje enviado a {topico}: {mensaje}")
    except Exception as e:
        print(f"❌ Error enviando mensaje: {e}")
    finally:
        cliente.close()

@bp.route('/procesar-imagen', methods=['POST'])
def procesar_imagen():
    """
    Recibe una solicitud HTTP con datos de imagen y la publica en Pulsar.
    """
    try:
        datos = request.json
        if not datos or 'id_imagen' not in datos:
            return jsonify({"error": "El JSON debe contener un campo 'id_imagen'"}), 400

        # 🔥 Enviar todos los datos en el mensaje
        mensaje = {
            "id_imagen": datos["id_imagen"],
            "modalidad": datos.get("modalidad", "Desconocida"),
            "patologia": datos.get("patologia", "Desconocido"),
            "region_anatomica": datos.get("region_anatomica", "No especificada"),
            "formato_imagen": datos.get("formato_imagen", "Desconocido"),
            "fuente_de_datos": datos.get("fuente_de_datos", "***ANONIMIZADO***"),
            "antecedentes": datos.get("antecedentes", "***ANONIMIZADO***"),
            "id_paciente": datos.get("id_paciente", str(uuid.uuid4())),
            "fecha_ingesta": datos.get("fecha_ingesta", datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
            "timestamp": uuid.uuid4().hex  # Agregar un identificador único
        }

        # Publicar en el tópico de anonimización
        publicar_mensaje(mensaje, TOPIC_ANONIMIZACION)

        return jsonify({"status": "Mensaje enviado"}), 202
    except Exception as e:
        return jsonify({"error": str(e)}), 500


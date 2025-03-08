import json
from pulsar import Client
from src.saludtechalpes.modulos.anonimizacion.dominio.eventos import EventoAnonimizacion, EventoConsultaAnonimizacion


class DespachadorEventosPulsar:
    def __init__(self):
        self.cliente = Client('pulsar://broker:6650')
        self.productor_anonimizacion = self.cliente.create_producer('anonimizacion')
        self.productor_consulta = self.cliente.create_producer('consulta_anonimizacion')

    def despachar(self, evento):
        if isinstance(evento, dict):  # Si ya es un diccionario, está bien
            evento_serializado = json.dumps(evento).encode("utf-8")
        elif hasattr(evento, "serializar"):  # Si tiene serialización, úsala
            evento_serializado = evento.serializar()
        else:
            print("⚠️ Evento desconocido, no se enviará a Pulsar")
            return

        print(f"📩 Enviando evento serializado: {evento_serializado}")
        self.pulsar_producer.send(evento_serializado)

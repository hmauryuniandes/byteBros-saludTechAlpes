from pulsar import Client
from src.saludtechalpes.modulos.anonimizacion.dominio.eventos import EventoAnonimizacion, EventoConsultaAnonimizacion


class DespachadorEventosPulsar:
    def __init__(self):
        self.cliente = Client('pulsar://broker:6650')
        self.productor_anonimizacion = self.cliente.create_producer('anonimizacion')
        self.productor_consulta = self.cliente.create_producer('consulta_anonimizacion')

    def despachar(self, evento):
        if isinstance(evento, EventoAnonimizacion):
            print(f"📩 Enviando evento de anonimización a Pulsar: {evento.id_datos}")
            self.productor_anonimizacion.send(evento.id_datos.encode('utf-8'))
            print("✅ Mensaje enviado correctamente a Pulsar")


        elif isinstance(evento, EventoConsultaAnonimizacion):
            print(f"🔍 Enviando evento de consulta a Pulsar: {evento.id_datos}")
            self.productor_consulta.send(evento.id_datos.encode('utf-8'))

        else:
            print("⚠️ Evento desconocido, no se enviará a Pulsar")

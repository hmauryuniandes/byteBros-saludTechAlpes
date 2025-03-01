from pulsar import Client

class DespachadorEventosPulsar:
    def __init__(self):
        self.cliente = Client('pulsar://localhost:6650')
        self.productor = self.cliente.create_producer('anonimizacion')

    def despachar(self, evento):
        self.productor.send(evento.id_datos.encode('utf-8'))

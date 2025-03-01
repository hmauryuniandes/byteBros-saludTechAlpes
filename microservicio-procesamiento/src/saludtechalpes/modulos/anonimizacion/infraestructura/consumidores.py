import threading
from pulsar import Client, ConsumerType
from modulos.anonimizacion.infraestructura.repositorios import RepositorioAnonimizacionSQL

class ConsumidorEventosPulsar:
    def __init__(self):
        self.cliente = Client('pulsar://localhost:6650')
        self.consumidor = self.cliente.subscribe('anonimizacion', subscription_name='sub_anon', consumer_type=ConsumerType.Shared)
        self.repositorio = RepositorioAnonimizacionSQL()

    def consumir(self):
        while True:
            mensaje = self.consumidor.receive()
            id_datos = mensaje.data().decode("utf-8")
            print(f'📩 Evento recibido para: {id_datos}')

            resultado = self.repositorio.obtener(id_datos)

            # 🔥 Agregamos un print para verificar si los datos existen en el repositorio
            print(f'🔍 Buscando en repositorio: {resultado}')

            if resultado:
                print(f'✅ Datos Anonimizados: {resultado.datos_procesados}')
            else:
                print(f'❌ No se encontraron datos para {id_datos}')

            self.consumidor.acknowledge(mensaje)

def iniciar_consumidor():
    consumidor = ConsumidorEventosPulsar()
    hilo = threading.Thread(target=consumidor.consumir, daemon=True)
    hilo.start()

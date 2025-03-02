import threading
from pulsar import Client, ConsumerType
from src.saludtechalpes.modulos.anonimizacion.infraestructura.repositorios import RepositorioImagenesSQL

class ConsumidorEventosPulsar:
    def __init__(self):
        self.cliente = Client('pulsar://broker:6650')

        # 🔥 Dos consumidores: uno para anonimización y otro para consulta
        self.consumidor_anonimizacion = self.cliente.subscribe(
            'anonimizacion', subscription_name='sub_anon', consumer_type=ConsumerType.Shared
        )
        self.consumidor_consulta = self.cliente.subscribe(
            'consulta_anonimizacion', subscription_name='sub_consulta', consumer_type=ConsumerType.Shared
        )

        self.repositorio = RepositorioImagenesSQL()

    def consumir_anonimizacion(self):
        """Consume eventos de anonimización"""
        while True:
            mensaje = self.consumidor_anonimizacion.receive()
            id_datos = mensaje.data().decode("utf-8")
            print(f'📩 Evento de ANONIMIZACIÓN recibido para ID: {id_datos}')

            resultado = self.repositorio.obtener_por_id(id_datos)

            if resultado:
                print("✅ Datos Anonimizados Guardados:")
                print(resultado)
            else:
                print(f'❌ No se encontraron datos para ID {id_datos}')

            self.consumidor_anonimizacion.acknowledge(mensaje)

    def consumir_consulta(self):
        """Consume eventos de consulta de datos anonimizados"""
        while True:
            mensaje = self.consumidor_consulta.receive()
            id_datos = mensaje.data().decode("utf-8")
            print(f'🔍 Evento de CONSULTA recibido para ID: {id_datos}')

            resultado = self.repositorio.obtener_por_id(id_datos)

            if resultado:
                print(f"✅ Imagen Consultada: {resultado}")
            else:
                print(f'❌ No se encontraron datos para ID {id_datos}')

            self.consumidor_consulta.acknowledge(mensaje)

def iniciar_consumidor():
    consumidor = ConsumidorEventosPulsar()
    
    hilo_anonimizacion = threading.Thread(target=consumidor.consumir_anonimizacion, daemon=True)
    hilo_consulta = threading.Thread(target=consumidor.consumir_consulta, daemon=True)

    hilo_anonimizacion.start()
    hilo_consulta.start()

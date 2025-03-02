from pulsar import Client, ConsumerType
from src.saludtechalpes.modulos.anonimizacion.infraestructura.repositorios import RepositorioImagenesSQL

class ObtenerImagenAnonimizada:
    """Query para obtener una imagen anonimizada consumiendo un evento desde Pulsar"""

    def __init__(self):
        self.repositorio = RepositorioImagenesSQL()
        self.cliente = Client('pulsar://broker:6650')
        self.consumidor = self.cliente.subscribe(
            'consulta_anonimizacion', 
            subscription_name='sub_consulta', 
            consumer_type=ConsumerType.Shared
        )

    def ejecutar(self):
        """Escucha eventos de consulta desde Pulsar y responde con los datos anonimizados"""
        while True:
            mensaje = self.consumidor.receive()
            id_datos = mensaje.data().decode("utf-8")
            print(f'🔍 Evento de CONSULTA recibido en Query para ID: {id_datos}')

            resultado = self.repositorio.obtener_por_id(id_datos)

            if resultado:
                print(f"✅ Imagen Consultada: {resultado}")
            else:
                print(f'❌ No se encontraron datos para ID {id_datos}')

            self.consumidor.acknowledge(mensaje)  # 🔥 Confirmamos que el mensaje fue procesado

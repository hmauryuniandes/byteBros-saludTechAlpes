import threading
from pulsar import Client, ConsumerType
from modulos.anonimizacion.infraestructura.repositorios import RepositorioImagenesSQL

class ConsumidorEventosPulsar:
    def __init__(self):
        self.cliente = Client('pulsar://localhost:6650')
        self.consumidor = self.cliente.subscribe('anonimizacion', subscription_name='sub_anon', consumer_type=ConsumerType.Shared)
        self.repositorio = RepositorioImagenesSQL()

    def consumir(self):
        while True:
            mensaje = self.consumidor.receive()
            id_datos = mensaje.data().decode("utf-8")
            print(f'📩 Evento recibido para ID: {id_datos}')

            resultado = self.repositorio.obtener_por_id(id_datos)

            if resultado:
                print("✅ Datos Anonimizados Recibidos:")
                print(f"🆔 ID Imagen: {resultado['id_imagen']}")
                print(f"📷 Modalidad: {resultado['modalidad']}")
                print(f"🩻 Patología: {resultado['patologia']}")
                print(f"🦴 Región Anatómica: {resultado['region_anatomica']}")
                print(f"📂 Formato: {resultado['formato_imagen']}")
                print(f"🏥 Fuente de Datos: {resultado['fuente_de_datos']}")
                print(f"📜 Antecedentes: {resultado['antecedentes']}")
                print(f"🔒 ID Paciente Anonimizado: {resultado['id_paciente']}")
                print(f"📅 Año de Ingesta: {resultado['fecha_ingesta']}")
            else:
                print(f'❌ No se encontraron datos para ID {id_datos}')

            self.consumidor.acknowledge(mensaje)

def iniciar_consumidor():
    consumidor = ConsumidorEventosPulsar()
    hilo = threading.Thread(target=consumidor.consumir, daemon=True)
    hilo.start()

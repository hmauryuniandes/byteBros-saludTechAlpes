class EventoAnonimizacion:
    def __init__(self, id_datos: str):
        self.id_datos = str(id_datos)

class EventoConsultaAnonimizacion:
    """Evento para indicar que se ha consultado una imagen anonimizada"""

    def __init__(self, id_datos):
        self.id_datos = str(id_datos)  # 🔥 Convertimos el ID en string

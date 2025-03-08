import json


class EventoAnonimizacion:
    def __init__(self, datos):
        self.datos = datos  # Ahora `datos` es un diccionario

    def serializar(self):
        return json.dumps(self.datos).encode("utf-8")


class EventoConsultaAnonimizacion:
    """Evento para indicar que se ha consultado una imagen anonimizada"""

    def __init__(self, id_datos):
        self.id_datos = str(id_datos)
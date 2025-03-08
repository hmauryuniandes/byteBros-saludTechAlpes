class EventStore:
    def __init__(self):
        # En este caso, utilizaremos una lista en memoria para guardar los eventos
        self.eventos = []

    def save_event(self, evento):
        # Guarda el evento en la lista (o en una base de datos)
        self.eventos.append(evento)
        print(f"Evento guardado: {evento}")

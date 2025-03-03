import json

class EventStore:
    def __init__(self, filename="event_store.json"):
        self.filename = filename
    
    def save_event(self, event):
        # Guardamos el evento en un archivo JSON
        with open(self.filename, 'a') as file:
            file.write(json.dumps(event) + "\n")
    
    def get_all_events(self):
        # Recuperamos todos los eventos almacenados
        events = []
        with open(self.filename, 'r') as file:
            for line in file:
                events.append(json.loads(line.strip()))
        return events

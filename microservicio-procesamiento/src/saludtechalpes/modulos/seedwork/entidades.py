from abc import ABC
import uuid

class Entidad(ABC):
    """ Clase base para todas las entidades del dominio """
    
    def __init__(self, id=None):
        self.id = id if id else str(uuid.uuid4())

    def __eq__(self, other):
        if isinstance(other, Entidad):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)

from abc import ABC, abstractmethod

class Repositorio(ABC):
    """ Clase base para todos los repositorios """

    @abstractmethod
    def obtener_por_id(self, id):
        pass

    @abstractmethod
    def guardar(self, entidad):
        pass

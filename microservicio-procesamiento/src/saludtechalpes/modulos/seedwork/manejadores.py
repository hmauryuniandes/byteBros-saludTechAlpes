from abc import ABC, abstractmethod

class ManejadorEventos(ABC):
    """ Clase base para manejar eventos del dominio """

    @abstractmethod
    def manejar(self, evento):
        pass

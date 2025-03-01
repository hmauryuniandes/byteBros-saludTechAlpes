from abc import ABC, abstractmethod

class UnidadTrabajo(ABC):
    """ Patrón Unit of Work """

    @abstractmethod
    def iniciar(self):
        pass

    @abstractmethod
    def confirmar(self):
        pass

    @abstractmethod
    def abortar(self):
        pass

from abc import ABC, abstractmethod

class RepositorioAnonimizacion(ABC):
    @abstractmethod
    def guardar(self, datos):
        pass

    @abstractmethod
    def obtener(self, id_datos):
        pass

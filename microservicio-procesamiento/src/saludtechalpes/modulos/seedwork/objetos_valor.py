from abc import ABC

class ObjetoValor(ABC):
    """ Clase base para representar objetos de valor en el dominio """

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))

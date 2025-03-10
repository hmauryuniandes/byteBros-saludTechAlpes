""" Excepciones del dominio de Sagas

En este archivo usted encontrará los Excepciones relacionadas
al dominio de Sagas

"""

from saludtechalpes.seedwork.dominio.excepciones import ExcepcionFabrica

class TipoObjetoNoExisteEnDominioSagasExcepcion(ExcepcionFabrica):
    def __init__(self, mensaje='No existe una fábrica para el tipo solicitado en el módulo de Sagas'):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)
""" Excepciones del dominio de suscripciones

En este archivo usted encontrará los Excepciones relacionadas
al dominio de suscripciones

"""

from saludtechalpes.seedwork.dominio.excepciones import ExcepcionFabrica

class TipoObjetoNoExisteEnDominioSuscripcionesExcepcion(ExcepcionFabrica):
    def __init__(self, mensaje='No existe una fábrica para el tipo solicitado en el módulo de suscripciones'):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)
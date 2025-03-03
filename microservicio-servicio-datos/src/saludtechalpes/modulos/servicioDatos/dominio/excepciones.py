""" Excepciones del dominio de servicio de datos

En este archivo usted encontrará los Excepciones relacionadas
al dominio de servicio de datos

"""

from saludtechalpes.seedwork.dominio.excepciones import ExcepcionFabrica

class TipoObjetoNoExisteEnDominioServicioDatosExcepcion(ExcepcionFabrica):
    def __init__(self, mensaje='No existe una fábrica para el tipo solicitado en el módulo de servicio de datos'):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)
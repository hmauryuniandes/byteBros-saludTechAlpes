""" Excepciones para la capa de infrastructura del dominio de servicio de datos

En este archivo usted encontrará los Excepciones relacionadas
a la capa de infraestructura del dominio de servicio de datos

"""

from saludtechalpes.seedwork.dominio.excepciones import ExcepcionFabrica

class NoExisteImplementacionParaTipoFabricaExcepcion(ExcepcionFabrica):
    def __init__(self, mensaje='No existe una implementación para el repositorio con el tipo dado.'):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)
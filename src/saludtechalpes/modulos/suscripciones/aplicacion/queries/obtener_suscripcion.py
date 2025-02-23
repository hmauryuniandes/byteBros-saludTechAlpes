from saludtechalpes.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from saludtechalpes.seedwork.aplicacion.queries import ejecutar_query as query
from saludtechalpes.modulos.suscripciones.infraestructura.repositorios import RepositorioSuscripciones
from dataclasses import dataclass
from .base import SuscripcionQueryBaseHandler
from saludtechalpes.modulos.suscripciones.aplicacion.mapeadores import MapeadorSuscripcion
import uuid

@dataclass
class ObtenerSuscripcion(Query):
    id: str

class ObtenerSuscripcionHandler(SuscripcionQueryBaseHandler):

    def handle(self, query: ObtenerSuscripcion) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioSuscripciones.__class__)
        suscripcion =  self.fabrica_suscripciones.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorSuscripcion())
        return QueryResultado(resultado=suscripcion)

@query.register(ObtenerSuscripcion)
def ejecutar_query_obtener_suscripcion(query: ObtenerSuscripcion):
    handler = ObtenerSuscripcionHandler()
    return handler.handle(query)
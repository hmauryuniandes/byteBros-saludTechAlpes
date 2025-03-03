from saludtechalpes.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from saludtechalpes.seedwork.aplicacion.queries import ejecutar_query as query
from saludtechalpes.modulos.servicioDatos.infraestructura.repositorios import RepositorioServicioDatos
from dataclasses import dataclass
from .base import ServicioDatosQueryBaseHandler
from saludtechalpes.modulos.servicioDatos.aplicacion.mapeadores import MapeadorServicioDatos
import uuid

@dataclass
class ObtenerServicioDatos(Query):
    id: str

class ObtenerServicioDatosHandler(ServicioDatosQueryBaseHandler):

    def handle(self, query: ObtenerServicioDatos) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioServicioDatos.__class__)
        serviciodatos =  self.fabrica_servicio_datos.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorServicioDatos())
        return QueryResultado(resultado=serviciodatos)

@query.register(ObtenerServicioDatos)
def ejecutar_query_obtener_servicio_datos(query: ObtenerServicioDatos):
    handler = ObtenerServicioDatosHandler()
    return handler.handle(query)
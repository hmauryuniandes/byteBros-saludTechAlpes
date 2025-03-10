import saludtechalpes.seedwork.presentacion.api as api
from saludtechalpes.modulos.servicioDatos.aplicacion.queries.obtener_servicio_datos import ObtenerServicioDatos
from saludtechalpes.seedwork.aplicacion.queries import ejecutar_query
from saludtechalpes.modulos.servicioDatos.aplicacion.mapeadores import MapeadorServicioDatosDTOJson

bp = api.crear_blueprint('serviciodatos', '/serviciodatos')

@bp.route('/serviciodatos-query/<id>', methods=('GET',))
def dar_serviciodatos(id=None):
    query_resultado = ejecutar_query(ObtenerServicioDatos(id))
    map_serviciodatos = MapeadorServicioDatosDTOJson()
    
    return map_serviciodatos.dto_a_externo(query_resultado.resultado)
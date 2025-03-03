import saludtechalpes.seedwork.presentacion.api as api
import json
from saludtechalpes.modulos.suscripciones.aplicacion.comandos.crear_suscripcion import CrearSuscripcion
from saludtechalpes.modulos.suscripciones.aplicacion.queries.obtener_suscripcion import ObtenerSuscripcion
from saludtechalpes.seedwork.dominio.excepciones import ExcepcionDominio
from saludtechalpes.seedwork.aplicacion.comandos import ejecutar_commando
from saludtechalpes.seedwork.aplicacion.queries import ejecutar_query

from flask import request
from flask import Response
from saludtechalpes.modulos.suscripciones.aplicacion.mapeadores import MapeadorSuscripcionDTOJson

bp = api.crear_blueprint('suscripciones', '/suscripciones')

@bp.route('/suscripcion-query/<id>', methods=('GET',))
def dar_suscripcion(id=None):
    query_resultado = ejecutar_query(ObtenerSuscripcion(id))
    map_suscripcion = MapeadorSuscripcionDTOJson()
    
    return map_suscripcion.dto_a_externo(query_resultado.resultado)
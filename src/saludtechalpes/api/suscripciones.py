import saludtechalpes.seedwork.presentacion.api as api
import json
from saludtechalpes.modulos.suscripciones.aplicacion.servicios import ServicioSuscripcion
from saludtechalpes.seedwork.dominio.excepciones import ExcepcionDominio

from flask import request
from flask import Response
from saludtechalpes.modulos.suscripciones.aplicacion.mapeadores import MapeadorSuscripcionDTOJson

bp = api.crear_blueprint('suscripciones', '/suscripciones')

@bp.route('/suscripcion', methods=('POST',))
def suscripcion():
    try:
        suscripcion_dict = request.json

        map_suscripcion = MapeadorSuscripcionDTOJson()
        suscripcion_dto = map_suscripcion.externo_a_dto(suscripcion_dict)

        sr = ServicioSuscripcion()
        dto_final = sr.crear_suscripcion(suscripcion_dto)

        return map_suscripcion.dto_a_externo(dto_final)
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/suscripcion', methods=('GET',))
@bp.route('/suscripcion/<id>', methods=('GET',))
def dar_suscripcion(id=None):
    if id:
        sr = ServicioSuscripcion()
        
        return sr.obtener_suscripcion_por_id(id)
    else:
        return [{'message': 'GET!'}]
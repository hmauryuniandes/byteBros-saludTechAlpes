
import json
import uuid
from flask import  Blueprint 
from flask import request
from flask import Response

from src.despachadores import Despachador
from . import utils

bp = Blueprint('suscripciones', __name__, url_prefix='/suscripciones')

@bp.route('/suscripcion-comando', methods=('POST',))
def suscripcion():
    # try:
    suscripcion_dict = request.json
    payload = dict(
        cliente_codigo = suscripcion_dict['cliente']['codigo'],
        cliente_nombres = suscripcion_dict['cliente']['nombre']['nombres'],
        cliente_apellidos = suscripcion_dict['cliente']['nombre']['apellidos'],
        cliente_usuario = suscripcion_dict['cliente']['usuario'],
        cliente_rut = suscripcion_dict['cliente']['rut']['numero'],
        cliente_cedula = suscripcion_dict['cliente']['cedula']['numero'],
        cliente_email = suscripcion_dict['cliente']['email'],
        plan_codigo =  suscripcion_dict['plan']['codigo'],
        plan_nombre =  suscripcion_dict['plan']['nombre'],
    )
    comando = dict(
        id = str(uuid.uuid4()),
        time=utils.time_millis(),
        specversion = "v1",
        type = "ComandoCrearSuscripcion",
        ingestion=utils.time_millis(),
        datacontenttype="AVRO",
        service_name = "BFF Web",
        data = payload
    )
    despachador = Despachador()
    despachador.publicar_mensaje(comando, 'comandos-suscripcion', "public/default/comando-suscripcion")

    return Response('{}', status=202, mimetype='application/json')
    # except:
    #     return Response(status=400, mimetype='application/json')

# @bp.route('/suscripcion-query/<id>', methods=('GET',))
# def dar_suscripcion(id=None):
#     query_resultado = ejecutar_query(ObtenerSuscripcion(id))
#     map_suscripcion = MapeadorSuscripcionDTOJson()
    
#     return map_suscripcion.dto_a_externo(query_resultado.resultado)
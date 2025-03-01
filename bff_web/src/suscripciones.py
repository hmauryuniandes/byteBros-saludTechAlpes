
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
        # cliente = suscripcion_dict['cliente'],
        # plan = suscripcion_dict['plan'],
        # faturas = suscripcion_dict['facturas']
        id_suscripcion = suscripcion_dict['id_suscripcion']
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
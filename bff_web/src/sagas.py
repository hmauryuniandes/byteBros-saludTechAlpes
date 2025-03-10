
import json
import uuid
from flask import  Blueprint 
from flask import request
from flask import Response

from src.despachadores import Despachador
from . import utils

bp = Blueprint('sagas', __name__, url_prefix='/sagas')

@bp.route('/iniciar-suscripcion-comando', methods=('POST',))
def suscripcion():
    try:
        payload = request.json

        print(payload)

        comando = dict(
            id = str(uuid.uuid4()),
            time=utils.time_millis(),
            specversion = "v1",
            type = "ComandoIniciarSuscripcion",
            ingestion=utils.time_millis(),
            datacontenttype="AVRO",
            service_name = "BFF Web",
            data = payload
        )
        despachador = Despachador()
        despachador.publicar_mensaje(comando, 'comandos-iniciar-suscripcion', "public/default/comandos-iniciar-suscripcion")

        return Response('{}', status=202, mimetype='application/json')
    except:
        return Response(status=400, mimetype='application/json')
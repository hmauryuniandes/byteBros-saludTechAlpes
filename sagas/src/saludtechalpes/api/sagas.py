import saludtechalpes.seedwork.presentacion.api as api
import json
from saludtechalpes.modulos.sagas.aplicacion.comandos.iniciar_suscripcion import IniciarSuscripcion
from saludtechalpes.seedwork.dominio.excepciones import ExcepcionDominio
from saludtechalpes.seedwork.aplicacion.comandos import ejecutar_commando

from flask import request
from flask import Response

bp = api.crear_blueprint('sagas', '/sagas')

@bp.route('/iniciar-suscripcion-comando', methods=('POST',))
def suscripcion():
    try:
        suscripcion_dict = request.json
        comando = IniciarSuscripcion(data=suscripcion_dict)
        ejecutar_commando(comando)

        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')


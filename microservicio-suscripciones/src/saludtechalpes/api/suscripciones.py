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

@bp.route('/suscripcion-comando', methods=('POST',))
def suscripcion():
    try:
        suscripcion_dict = request.json

        map_suscripcion = MapeadorSuscripcionDTOJson()
        suscripcion_dto = map_suscripcion.externo_a_dto(suscripcion_dict)

        comando = CrearSuscripcion(suscripcion_dto.cliente, suscripcion_dto.plan, suscripcion_dto.id, suscripcion_dto.facturas)
        
        # TODO Reemplaze es todo código sincrono y use el broker de eventos para propagar este comando de forma asíncrona
        # Revise la clase Despachador de la capa de infraestructura
        ejecutar_commando(comando)

        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/suscripcion-query/<id>', methods=('GET',))
def dar_suscripcion(id=None):
    query_resultado = ejecutar_query(ObtenerSuscripcion(id))
    map_suscripcion = MapeadorSuscripcionDTOJson()
    
    return map_suscripcion.dto_a_externo(query_resultado.resultado)
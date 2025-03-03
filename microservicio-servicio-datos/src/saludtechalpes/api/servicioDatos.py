import saludtechalpes.seedwork.presentacion.api as api
import json
from saludtechalpes.modulos.servicioDatos.aplicacion.comandos.crear_servicio_datos import CrearServicioDatos
from saludtechalpes.modulos.servicioDatos.aplicacion.queries.obtener_servicio_datos import ObtenerServicioDatos
from saludtechalpes.seedwork.dominio.excepciones import ExcepcionDominio
from saludtechalpes.seedwork.aplicacion.comandos import ejecutar_commando
from saludtechalpes.seedwork.aplicacion.queries import ejecutar_query

from flask import request
from flask import Response
from saludtechalpes.modulos.servicioDatos.aplicacion.mapeadores import MapeadorServicioDatosDTOJson

bp = api.crear_blueprint('serviciodatos', '/serviciodatos')

@bp.route('/serviciodatos-comando', methods=('POST',))
def serviciodatos():
    try:
        serviciodatos_dict = request.json

        map_serviciodatos = MapeadorServicioDatosDTOJson()
        serviciodatos_dto = map_serviciodatos.externo_a_dto(serviciodatos_dict)

        comando = CrearServicioDatos(serviciodatos_dto.suscripcion, serviciodatos_dto.experto, serviciodatos_dto.nube, serviciodatos_dto.dataset, serviciodatos_dto.id)
        
        # TODO Reemplaze es todo código sincrono y use el broker de eventos para propagar este comando de forma asíncrona
        # Revise la clase Despachador de la capa de infraestructura
        ejecutar_commando(comando)

        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/serviciodatos-query/<id>', methods=('GET',))
def dar_serviciodatos(id=None):
    query_resultado = ejecutar_query(ObtenerServicioDatos(id))
    map_serviciodatos = MapeadorServicioDatosDTOJson()
    
    return map_serviciodatos.dto_a_externo(query_resultado.resultado)
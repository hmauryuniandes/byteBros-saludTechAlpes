import time
import os
import requests
import json
from fastavro.schema import parse_schema
from pulsar.schema import *

def time_millis():
    return int(time.time() * 1000)

def broker_host():
    return os.getenv('PULSAR_ADDRESS', default="localhost")

def consultar_schema_registry(topico: str) -> dict:
    schema = requests.get(f'http://{broker_host()}:8080/admin/v2/schemas/{topico}/schema')
    json_registry = schema.json()
    return json.loads(json_registry.get('data',{}))

def obtener_schema_avro_de_diccionario(json_schema: dict) -> AvroSchema:
    definicion_schema = parse_schema(json_schema)
    return AvroSchema(None, schema_definition=definicion_schema)

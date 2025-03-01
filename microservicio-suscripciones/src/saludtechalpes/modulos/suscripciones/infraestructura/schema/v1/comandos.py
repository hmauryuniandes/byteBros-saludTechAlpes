from pulsar.schema import *
from dataclasses import dataclass, field
from saludtechalpes.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearSuscripcionPayload(ComandoIntegracion):
    id_suscripcion = String()
    # TODO Cree los records para itinerarios

class ComandoCrearSuscripcion(ComandoIntegracion):
    data = ComandoCrearSuscripcionPayload()
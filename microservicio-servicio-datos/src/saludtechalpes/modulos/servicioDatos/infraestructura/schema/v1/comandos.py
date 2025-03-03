from pulsar.schema import *
from dataclasses import dataclass, field
from saludtechalpes.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearServicioDatosPayload(ComandoIntegracion):
    id_usuario = String()
    # TODO Cree los records para itinerarios

class ComandoCrearServicioDatos(ComandoIntegracion):
    data = ComandoCrearServicioDatosPayload()

class ComandoIniciarServicioDatosPayload(ComandoIntegracion):
    id_usuario = String()

class ComandoIniciarServicioDatos(ComandoIntegracion):
    data = ComandoIniciarServicioDatosPayload()

class ComandoTerminarServicioDatosPayload(ComandoIntegracion):
    id_usuario = String()

class ComandoTerminarServicioDatos(ComandoIntegracion):
    data = ComandoTerminarServicioDatosPayload()

class ComandoAsignarExpertoServicioDatosPayload(ComandoIntegracion):
    id_usuario = String()

class ComandoAsignarExpertoServicioDatos(ComandoIntegracion):
    data = ComandoAsignarExpertoServicioDatosPayload()
from pulsar.schema import *
from dataclasses import dataclass, field
from saludtechalpes.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearInfraestructuraPayload(ComandoIntegracion):
    id_cliente = String()
    id_plan = String()
    id_suscripcion = String()

class ComandoCrearInfraestructura(ComandoIntegracion):
    data = ComandoCrearInfraestructuraPayload()

class ComandoCompensacionCrearInfraestructuraPayload(ComandoIntegracion):
    id_serviciodatos = String()
    id_suscripcion = String()

class ComandoCompensacionCrearInfraestructura(ComandoIntegracion):
    data = ComandoCrearInfraestructuraPayload()

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
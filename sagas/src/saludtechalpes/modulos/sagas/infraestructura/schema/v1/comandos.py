from pulsar.schema import *
from dataclasses import dataclass, field
from saludtechalpes.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoIniciarSuscripcionPayload(ComandoIntegracion):
    cliente_codigo = String()
    cliente_nombres = String()
    cliente_apellidos = String()
    cliente_usuario = String()
    cliente_rut = String()
    cliente_cedula = String()
    cliente_email = String()
    plan_codigo = String()
    plan_nombre = String()
    id_suscripcion = String()

class ComandoIniciarSuscripcion(ComandoIntegracion):
    data = ComandoIniciarSuscripcionPayload()

class ComandoCrearSuscripcionPayload(ComandoIntegracion):
    cliente_codigo = String()
    cliente_nombres = String()
    cliente_apellidos = String()
    cliente_usuario = String()
    cliente_rut = String()
    cliente_cedula = String()
    cliente_email = String()
    plan_codigo = String()
    plan_nombre = String()
    id_suscripcion = String()

class ComandoCrearSuscripcion(ComandoIntegracion):
    data = ComandoCrearSuscripcionPayload()

class ComandoCompensacionCrearSuscripcionPayload(ComandoIntegracion):
    cliente_codigo = String()
    plan_codigo = String()
    id_suscripcion = String()

class ComandoCompensacionCrearSuscripcion(ComandoIntegracion):
    data = ComandoCrearSuscripcionPayload()
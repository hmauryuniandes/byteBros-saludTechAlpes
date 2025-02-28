"""Reglas de negocio del dominio de suscripcion

En este archivo usted encontrará reglas de negocio del dominio de suscripcion

"""

from saludtechalpes.seedwork.dominio.reglas import ReglaNegocio
from .entidades import Plan, Suscripcion

class AlmenosUnaPlan(ReglaNegocio):
    plan: Plan

    def __init__(self, plan, mensaje='La suscripcion debe tener un plan selecionado'):
        super().__init__(mensaje)
        self.plan = plan

    def es_valido(self) -> bool:
        return self.plan is not None 
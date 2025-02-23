from __future__ import annotations
from dataclasses import dataclass, field
import uuid
from saludtechalpes.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

@dataclass
class SuscripcionCreada(EventoDominio):
    id_suscripcion: uuid.UUID = None
    codigo_cliente: str = None
    codigo_plan: str = None
    
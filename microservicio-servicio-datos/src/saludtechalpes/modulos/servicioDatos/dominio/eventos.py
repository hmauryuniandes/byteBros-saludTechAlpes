from __future__ import annotations
from dataclasses import dataclass, field
import uuid
from saludtechalpes.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

@dataclass
class ServicioDatosCreada(EventoDominio):
    id_serviciodatos: uuid.UUID = None
    codigo_suscripcion: str = None
    codigo_experto: str = None
    codigo_nube: str = None
    codigo_data_set: str = None
    
from dataclasses import dataclass

@dataclass(frozen=True)
class DatosOriginales:
    id: str
    contenido: str

from src.saludtechalpes.modulos.anonimizacion.dominio.entidades import ImagenAnonimizada
from src.saludtechalpes.modulos.anonimizacion.infraestructura.repositorios import RepositorioImagenesSQL
from src.saludtechalpes.modulos.anonimizacion.infraestructura.uow import UnidadTrabajoSQL
from src.saludtechalpes.modulos.anonimizacion.infraestructura.despachadores import DespachadorEventosPulsar
from datetime import datetime
from src.saludtechalpes.modulos.anonimizacion.dominio.eventos import EventoAnonimizacion

import uuid

class Anonimizador:
    def __init__(self):
        self.repositorio = RepositorioImagenesSQL()
        self.uow = UnidadTrabajoSQL()
        self.despachador = DespachadorEventosPulsar()

    def ejecutar(self, datos_imagen: dict):
        print(f'🔍 Procesando imagen con datos: {datos_imagen}')
        fecha_ingesta_str = datos_imagen.get("fecha_ingesta", None)
        if fecha_ingesta_str:
            fecha_ingesta = datetime.strptime(fecha_ingesta_str, "%Y-%m-%d %H:%M:%S").year
        else:
            fecha_ingesta = datetime.now()

        imagen = ImagenAnonimizada(
            id_imagen=datos_imagen["id_imagen"],
            modalidad=datos_imagen.get("modalidad", "Desconocida"),
            patologia=datos_imagen.get("patologia", "Desconocido"),
            region_anatomica=datos_imagen.get("region_anatomica", "No especificada"),
            formato_imagen=datos_imagen.get("formato_imagen"),
            fuente_de_datos="***ANONIMIZADO***",
            antecedentes="***ANONIMIZADO***",
            id_paciente=str(uuid.uuid4()),
            fecha_ingesta=fecha_ingesta
        )


        with self.uow.iniciar() as session:
            nuevo_id = self.repositorio.guardar(imagen)
            self.uow.confirmar()

        evento = EventoAnonimizacion(nuevo_id)
        self.despachador.despachar(evento)

        return {"id": nuevo_id, "datos_procesados": imagen.__dict__}

from modulos.anonimizacion.dominio.entidades import DatosAnonimizados
from modulos.anonimizacion.dominio.eventos import EventoAnonimizacion
from modulos.anonimizacion.infraestructura.despachadores import DespachadorEventosPulsar
from modulos.anonimizacion.infraestructura.repositorios import RepositorioAnonimizacionSQL


class Anonimizador:
    def __init__(self):
        self.repositorio = RepositorioAnonimizacionSQL()
        self.despachador = DespachadorEventosPulsar()

    def ejecutar(self, contenido: str):
        datos_procesados = "***ANONIMIZADO***"
        datos = DatosAnonimizados(id=None, datos_procesados=datos_procesados)

        # 🔥 Guardamos los datos en la BD y obtenemos el nuevo ID
        nuevo_id = self.repositorio.guardar(datos)

        # 🔥 Ahora enviamos el evento con el ID correcto
        self.despachador.despachar(EventoAnonimizacion(id_datos=str(nuevo_id)))

        return DatosAnonimizados(id=nuevo_id, datos_procesados=datos_procesados)


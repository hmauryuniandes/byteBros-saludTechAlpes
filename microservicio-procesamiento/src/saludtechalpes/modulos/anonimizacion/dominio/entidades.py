from src.saludtechalpes.modulos.seedwork.entidades import Entidad

class ImagenAnonimizada(Entidad):
    """Entidad que representa una imagen procesada con anonimización"""

    def __init__(self, id_imagen, modalidad, patologia, region_anatomica, formato_imagen, 
                 fuente_de_datos, antecedentes, id_paciente, fecha_ingesta, id=None):
        super().__init__(id)
        self.id_imagen = id_imagen
        self.modalidad = modalidad
        self.patologia = patologia
        self.region_anatomica = region_anatomica
        self.formato_imagen = formato_imagen
        self.fuente_de_datos = fuente_de_datos
        self.antecedentes = antecedentes
        self.id_paciente = id_paciente
        self.fecha_ingesta = fecha_ingesta

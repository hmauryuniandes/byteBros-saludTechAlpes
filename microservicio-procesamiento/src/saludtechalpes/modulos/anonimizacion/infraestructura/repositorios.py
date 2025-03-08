from src.saludtechalpes.modulos.seedwork.repositorios import Repositorio
from src.saludtechalpes.config.db import SessionLocal, DatosAnonimizadosDB
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy.dialects.postgresql import insert

class RepositorioImagenesSQL(Repositorio):
    """Repositorio que maneja las operaciones de la base de datos para imágenes anonimizadas"""

    def __init__(self):
        self.db: Session = SessionLocal()

    def obtener_por_id(self, id_imagen):
        """Obtiene una imagen anonimizada por ID de imagen y la convierte en un diccionario"""
        db_datos = self.db.query(DatosAnonimizadosDB).filter_by(id_imagen=id_imagen).first()

        if db_datos:
            return {column.name: getattr(db_datos, column.name) for column in db_datos.__table__.columns}  # 🔥 Convierte a dict limpio
        
        return None

    def guardar(self, imagen):
        print(f'💾 Guardando en DB: {imagen}')

        nuevo_registro = DatosAnonimizadosDB(
            id_imagen=imagen.id_imagen,
            modalidad=imagen.modalidad,
            patologia=imagen.patologia,
            region_anatomica=imagen.region_anatomica,
            formato_imagen=imagen.formato_imagen,
            fuente_de_datos=imagen.fuente_de_datos,
            antecedentes=imagen.antecedentes,
            id_paciente=imagen.id_paciente,
            fecha_ingesta=imagen.fecha_ingesta
        )

        try:
            self.db.add(nuevo_registro)  # Insertar directamente
            self.db.commit()
            return nuevo_registro.id  # Devuelve el ID autoincremental
        except IntegrityError as e:
            self.db.rollback()
            print(f'❌ Error al insertar en DB: {e}')
            return None


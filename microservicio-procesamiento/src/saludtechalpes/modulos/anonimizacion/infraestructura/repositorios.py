from src.saludtechalpes.modulos.seedwork.repositorios import Repositorio
from src.saludtechalpes.config.db import SessionLocal, DatosAnonimizadosDB
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy.dialects.postgresql import insert

class RepositorioImagenesSQL(Repositorio):
    """Repositorio que maneja las operaciones de la base de datos para imágenes anonimizadas"""

    def __init__(self):
        self.db: Session = SessionLocal()

    def obtener_por_id(self, id):
        """Obtiene una imagen anonimizada por ID y la convierte en un diccionario"""
        db_datos = self.db.query(DatosAnonimizadosDB).filter_by(id=id).first()

        if db_datos:
            return {column.name: getattr(db_datos, column.name) for column in db_datos.__table__.columns}  # 🔥 Convierte a dict limpio
        
        return None
    def guardar(self, imagen):
        print(f'💾 Guardando en DB: {imagen}')

        stmt = insert(DatosAnonimizadosDB).values(
            id_imagen=imagen.id_imagen,
            modalidad=imagen.modalidad,
            patologia=imagen.patologia,
            region_anatomica=imagen.region_anatomica,
            formato_imagen=imagen.formato_imagen,
            fuente_de_datos=imagen.fuente_de_datos,
            antecedentes=imagen.antecedentes,
            id_paciente=imagen.id_paciente,
            fecha_ingesta=imagen.fecha_ingesta
        ).on_conflict_do_update(
            index_elements=["id_imagen"],
            set_={
                "modalidad": imagen.modalidad,
                "patologia": imagen.patologia,
                "region_anatomica": imagen.region_anatomica,
                "formato_imagen": imagen.formato_imagen,
                "fuente_de_datos": imagen.fuente_de_datos,
                "antecedentes": imagen.antecedentes,
                "id_paciente": imagen.id_paciente,
                "fecha_ingesta": imagen.fecha_ingesta
            }
        )

        try:
            result = self.db.execute(stmt)
            self.db.commit()
            return result.inserted_primary_key[0] if result.inserted_primary_key else None
        except IntegrityError as e:
            self.db.rollback()
            print(f'Error al insertar en DB: {e}')
            return None


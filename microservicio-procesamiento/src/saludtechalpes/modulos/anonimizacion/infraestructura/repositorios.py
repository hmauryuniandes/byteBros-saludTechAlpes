from sqlalchemy.orm import Session
from config.db import SessionLocal, DatosAnonimizadosDB
from modulos.anonimizacion.dominio.entidades import DatosAnonimizados

class RepositorioAnonimizacionSQL:
    def __init__(self):
        self.db: Session = SessionLocal()

    def guardar(self, datos: DatosAnonimizados):
        print(f'💾 Guardando en DB: {datos}')

        # 🔥 Solo guardamos `datos_procesados`, la BD genera `id`
        db_datos = DatosAnonimizadosDB(datos_procesados=datos.datos_procesados)
        self.db.add(db_datos)
        self.db.commit()
        self.db.refresh(db_datos)  # 🔥 Esto obtiene el ID generado

        return db_datos.id  # ✅ Retorna el ID generado por la BD

    def obtener(self, id_datos):
        db_datos = self.db.query(DatosAnonimizadosDB).filter_by(id=id_datos).first()
        if db_datos:
            return DatosAnonimizados(db_datos.id, db_datos.datos_procesados)
        return None

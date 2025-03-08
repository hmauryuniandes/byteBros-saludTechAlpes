from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE_URL = os.environ.get('DB_URL')
print(f"Conectando a la base de datos en: {DATABASE_URL}")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class DatosAnonimizadosDB(Base):
    __tablename__ = "datos_anonimizados"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_imagen = Column(String, nullable=False)
    modalidad = Column(String, nullable=False)
    patologia = Column(String, nullable=True)
    region_anatomica = Column(String, nullable=True)
    formato_imagen = Column(String, nullable=False)
    fuente_de_datos = Column(String, nullable=False, default="***ANONIMIZADO***")  
    antecedentes = Column(String, nullable=False, default="***ANONIMIZADO***")  
    id_paciente = Column(String, nullable=False)
    fecha_ingesta = Column(Integer, nullable=False)  

    
def init_db():
    print("Creando tablas en la base de datos...")
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas.")

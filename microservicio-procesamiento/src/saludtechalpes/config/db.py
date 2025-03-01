from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://admin:admin@localhost:5432/anonimizacion"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class DatosAnonimizadosDB(Base):
    __tablename__ = "datos_anonimizados"

    id = Column(Integer, primary_key=True, autoincrement=True)  # 🔥 Genera automáticamente
    datos_procesados = Column(String)

    
def init_db():
    Base.metadata.create_all(bind=engine)

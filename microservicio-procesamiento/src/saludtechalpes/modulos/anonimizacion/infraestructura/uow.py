from modulos.seedwork.uow import UnidadTrabajo
from config.db import SessionLocal

class UnidadTrabajoSQL(UnidadTrabajo):
    """Unit of Work para manejar transacciones"""

    def __init__(self):
        self.db = SessionLocal()

    def iniciar(self):
        print("🔄 Iniciando Unidad de Trabajo")
        return self.db

    def confirmar(self):
        print("✅ Confirmando transacción")
        self.db.commit()

    def abortar(self):
        print("❌ Revirtiendo transacción")
        self.db.rollback()

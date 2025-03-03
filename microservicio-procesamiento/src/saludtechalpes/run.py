from src.saludtechalpes.presentacion.api import app
from src.saludtechalpes.config.db import init_db
from src.saludtechalpes.modulos.anonimizacion.infraestructura.consumidores import iniciar_consumidor

if __name__ == '__main__':
    init_db()
    iniciar_consumidor()
    app.run(host='0.0.0.0', port=5000, debug=True)

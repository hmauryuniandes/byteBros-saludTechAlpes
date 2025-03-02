from src.saludtechalpes.presentacion.api import app

from src.saludtechalpes.modulos.anonimizacion.infraestructura.consumidores import iniciar_consumidor

if __name__ == '__main__':
    iniciar_consumidor()
    app.run(host='0.0.0.0', port=5000, debug=True)

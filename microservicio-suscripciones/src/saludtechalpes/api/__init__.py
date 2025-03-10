import os
from flask import Flask, jsonify
from flask_swagger import swagger

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))

def importar_modelos_alchemy():
    import saludtechalpes.modulos.suscripciones.infraestructura.dto

def comenzar_consumidor(app):
    """
    Este es un código de ejemplo. Aunque esto sea funcional puede ser un poco peligroso tener 
    threads corriendo por si solos. Mi sugerencia es en estos casos usar un verdadero manejador
    de procesos y threads como Celery.
    """

    import threading
    import saludtechalpes.modulos.suscripciones.infraestructura.consumidores as suscripciones

    # Suscripción a eventos
    # threading.Thread(target=suscripciones.suscribirse_a_evento_suscription_creada).start()
    # threading.Thread(target=suscripciones.suscribirse_a_evento_suscription_fallida).start()

    # Suscripción a comandos
    threading.Thread(target=suscripciones.suscribirse_a_comandos, args=[app]).start()
   
def create_app(configuracion={}):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)

    # Configuracion de BD
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URL') or 'sqlite:///' + os.path.join(basedir, 'test_database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e32c'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['TESTING'] = configuracion.get('TESTING')

     # Inicializa la DB
    from saludtechalpes.config.db import init_db
    init_db(app)

    from saludtechalpes.config.db import db

    importar_modelos_alchemy()

    with app.app_context():
        db.create_all()
        if not app.config.get('TESTING'):
            comenzar_consumidor(app)

     # Importa Blueprints
    from . import suscripciones
   

    # Registro de Blueprints
    app.register_blueprint(suscripciones.bp)

    @app.route("/spec")
    def spec():
        swag = swagger(app)
        swag['info']['version'] = "1.0"
        swag['info']['title'] = "Suscripciones API"
        return jsonify(swag)

    @app.route("/health")
    def health():
        return {"status": "up"}

    return app

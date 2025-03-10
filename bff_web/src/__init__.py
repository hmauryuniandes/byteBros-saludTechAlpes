import os
from flask import Flask, jsonify
from flask_swagger import swagger

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))
   
def create_app(configuracion={}):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)

     # Importa Blueprints
    from . import suscripciones
    from . import procesamiento
    from . import sagas

    # Registro de Blueprints
    app.register_blueprint(suscripciones.bp)
    app.register_blueprint(procesamiento.bp)
    app.register_blueprint(sagas.bp)
    @app.route("/spec")
    def spec():
        swag = swagger(app)
        swag['info']['version'] = "1.0"
        swag['info']['title'] = "BFF WEB"
        return jsonify(swag)

    @app.route("/health")
    def health():
        return {"status": "up"}

    return app

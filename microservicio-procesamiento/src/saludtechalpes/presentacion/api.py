from flask import Flask, request, jsonify
from modulos.anonimizacion.aplicacion.comandos.anonimizar_datos import Anonimizador
from modulos.anonimizacion.infraestructura.repositorios import RepositorioImagenesSQL

app = Flask(__name__)

repositorio = RepositorioImagenesSQL()
anonimizador = Anonimizador()

@app.route('/anonimizar', methods=['POST'])
def anonimizar():
    datos_imagen = request.get_json()

    campos_requeridos = {"id_imagen", "modalidad", "formato_imagen", "fuente_de_datos", "fecha_ingesta"}
    if not campos_requeridos.issubset(set(datos_imagen.keys())):
        return jsonify({"error": "Faltan campos requeridos"}), 400

    resultado = anonimizador.ejecutar(datos_imagen)

    return jsonify({
        "id": resultado["id"],
        "datos_procesados": resultado
    })


@app.route('/anonimizado/<int:id_datos>', methods=['GET'])
def obtener_anonimizado(id_datos):
    resultado = repositorio.obtener(id_datos)
    if resultado is None:
        return jsonify({"error": "Datos no encontrados"}), 404

    return jsonify({"id": resultado.id, "datos_procesados": resultado.datos_procesados})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

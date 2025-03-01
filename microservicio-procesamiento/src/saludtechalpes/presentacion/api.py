from flask import Flask, request, jsonify
from modulos.anonimizacion.aplicacion.comandos.anonimizar_datos import Anonimizador
from modulos.anonimizacion.infraestructura.repositorios import RepositorioAnonimizacionSQL

app = Flask(__name__)

repositorio = RepositorioAnonimizacionSQL()
anonimizador = Anonimizador()

@app.route('/anonimizar', methods=['POST'])
def anonimizar():
    datos = request.get_json()
    contenido = datos.get('contenido')

    if not contenido:
        return jsonify({"error": "Faltan datos"}), 400

    # 🔥 Solo pasamos `contenido`, sin `id`
    resultado = anonimizador.ejecutar(contenido)

    # 🔥 Guardamos en la base de datos y obtenemos el nuevo ID
    nuevo_id = repositorio.guardar(resultado)

    return jsonify({"id": nuevo_id, "datos_procesados": resultado.datos_procesados})


@app.route('/anonimizado/<int:id_datos>', methods=['GET'])
def obtener_anonimizado(id_datos):
    resultado = repositorio.obtener(id_datos)
    if resultado is None:
        return jsonify({"error": "Datos no encontrados"}), 404

    return jsonify({"id": resultado.id, "datos_procesados": resultado.datos_procesados})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

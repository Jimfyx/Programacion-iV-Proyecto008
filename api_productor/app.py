import os

from flask import Flask, request, abort, jsonify

from services import sms_sender

app = Flask(__name__)

with app.app_context():
    id_app = os.environ.get('HOSTNAME')


@app.route('/requerimiento/', methods=['POST'])
def requerimiento():
    body = request.get_json()

    #validacion de contenido
    if not body:
        abort(400, 'Solicitud invalida')

    datos = ['nombre', 'telefono', 'requerimiento']
    for dato in datos:
        if dato not in body:
            abort(400, f"El dato de {dato} es obligatorio")

    #prueba enviar los datos a la cola de mensajes
    try:
        sms_sender.sms_sender(body['nombre'],body['telefono'],body['requerimiento'],id_app)
    except Exception as e:
        print(f'Error al procesar la solicitud: {e}')
        abort(500, 'Error al procesar la solicitud')
    return jsonify({"message": "Su solicitud a sido enviada a la cola"}), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
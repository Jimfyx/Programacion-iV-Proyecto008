import pika

def get_pika_connection():
    conexion_config = pika.ConnectionParameters(host='rabbitmq-app',port= 5672)
    try:
        conexion = pika.BlockingConnection(conexion_config)
        channel = conexion.channel()
        return channel, conexion
    except pika.exceptions.AMQPConnectionError:
        print("No se pudo establecer conexión con RabbitMQ")
        return None
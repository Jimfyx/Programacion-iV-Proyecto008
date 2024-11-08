import pika
from config import get_pika_connection

def sms_sender(nombre, telefono, requerimiento, enviado_por):
    channel, conexion = get_pika_connection()

    channel.queue_declare(queue='cola', durable=True)

    message = (f"{nombre}|{telefono}|{requerimiento}|{enviado_por}|")

    channel.basic_publish(exchange='', routing_key='cola', body=message, properties=pika.BasicProperties(delivery_mode=2))

    print(f"sent message: {message}")

    channel.close()
    conexion.close()
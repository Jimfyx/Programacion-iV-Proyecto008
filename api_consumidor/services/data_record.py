from app import app
from config import db
from models import message

def data_record(data):

    data_parts = data.split('|')

    nombre = data_parts[0]
    telefono = data_parts[1]
    requerimiento = data_parts[2]
    enviado_por = data_parts[3]

    #print(f"Los datos recibidos son: {nombre}, {telefono}, {requerimiento}, {enviado_por}")

    nuevo_requerimiento = message.Requerimiento(
        nombre = nombre,
        telefono = telefono,
        requerimiento = requerimiento,
        enviado_por = enviado_por
    )
    try:
        db.session.add(nuevo_requerimiento)
        db.session.commit()
        print("Registro guardado en la base de datos")
    except Exception as e:
        db.session.rollback()
        print(f"Error al guardar el registro: {e}")
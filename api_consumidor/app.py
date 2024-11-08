from flask import Flask
from sqlalchemy import text, create_engine
from threading import Thread

from services import sms_reciver
from config import Config, db
from models import message

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

def crear_database(uri):
    db_uri = uri.rsplit('/', 1)[0]
    engine = create_engine(db_uri, echo=True)
    try:
        with engine.connect() as connection:
            connection.execute(text("CREATE DATABASE IF NOT EXISTS itdb"))
            print("Base de datos creada o ya existente.")
            connection.close()            
    except Exception as e:
        print(f'Error al crear la base de datos: {e}')

def start_sms_receiver():
    sms_reciver.main()

with app.app_context():

    crear_database(Config.SQLALCHEMY_DATABASE_URI)

    try:
        db.session.execute(text('SELECT 1'))
        print('Conexión exitosa con la base de datos')

        db.create_all()
        print('Creación exitosa de las tablas')

    except Exception as e:
        print(f'Error en la creación de la base de datos: {e}')



if __name__ == '__main__':

    receiver_thread = Thread(target=start_sms_receiver, daemon=True)
    receiver_thread.start()

    app.run(debug=True, host='0.0.0.0')
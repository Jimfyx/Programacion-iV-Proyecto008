from config import db

class Requerimiento(db.Model):
    __tablename__ = 'requerimiento_it'

    id_req = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    telefono = db.Column(db.Integer, nullable=False)
    requerimiento = db.Column(db.String(50), nullable=False)
    enviado_por = db.Column(db.String(50), nullable=False, default='admin')

    def to_dict(self):
        return {
            'id_req': self.id_req,
            'nombre': self.nombre,
            'telefono': self.telefono,
            'requerimiento': self.requerimiento,
            'enviado_por': self.enviado_por
        }
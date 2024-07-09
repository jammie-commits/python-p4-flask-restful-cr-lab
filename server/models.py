from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import Column, Integer, String, Float


db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    image = Column(String(200))
    price = Column(Float, nullable=False, default=0.0)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image,
            'price': self.price,
        }

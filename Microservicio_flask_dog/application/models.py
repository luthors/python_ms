from . import db
from datetime import datetime

class Dog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    color = db.Column(db.String(80), nullable=False)
    size = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(80), nullable=False)
    breed = db.Column(db.String(80), nullable=False)
    adopted = db.Column(db.Boolean, nullable=False, default=False)
    date_added = db.Column(db.DateTime, default=datetime.now)
    date_updated = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'color': self.color,
            'size': self.size,
            'age': self.age,
            'gender': self.gender,
            'breed': self.breed,
            'adopted': self.adopted
        }
from dataclasses import dataclass
from app import db

@dataclass
class Paymet(db.Model):
    
    __tablename__ = 'paymets'

    id_paymet = db.Column('id_paymet', db.Integer, primary_key=True, autoincrement=True)
    id_product = db.Column('product_id', db.Integer, nullable=False)
    price = db.Column('price', db.Float, nullable=False)
    means_of_payment = db.Column('means_of_payment', db.String(120), nullable=False)
    deleted_at = db.Column(db.DateTime, nullable=True)
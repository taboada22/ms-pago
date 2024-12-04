from marshmallow import Schema, fields, post_load
from app.models import Paymet
from datetime import datetime

class PaymetSchema(Schema):
    id_paymet: int = fields.Integer()
    id_product: int = fields.Integer(required=True)
    price: float = fields.Float(required=True)
    means_of_payment: str = fields.String(required=True)
    deleted_at: datetime = fields.DateTime(dump_only=True) 

    @post_load
    def deserealizar_pago(self, data, **kwargs):
        return Paymet(**data)
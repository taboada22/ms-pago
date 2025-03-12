from flask import Blueprint, request
from app.Services.payments import PaymentServices
from app.Schemas.payments import payment_schema, payments_schema

payment = Blueprint('payment', __name__, url_prefix='/api/payment')
services = PaymentServices()


@payment.route('/add_payment', methods=['POST'])
def add_payment():
    payment = payment_schema.loads(request.json)
    status_code = 201
    try:
        status_code = 201
        return payment_schema.dumps(services.add_payment(payment)), status_code
    except:
        status_code = 400
        return payment_schema.dumps(services.add_payment(payment)), status_code

@payment.route('/delete/<int:id>', methods=['PUT'])  
def delete_payment(id):
    try:
        status_code = 200
        return payment_schema.dumps(services.delete_payment(id)), status_code
    except:
        status_code = 404
        return payment_schema.dumps(services.delete_payment(id)), status_code

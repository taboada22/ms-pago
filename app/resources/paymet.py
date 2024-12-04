from flask import Blueprint, request, jsonify
from app.services.paymet_service import PaymetService
from app.schemas.paymet_schema import PaymetSchema

paymet = Blueprint('paymet', __name__, url_prefix='/api/pago') # payment
service = PaymetService()

paymet_schema = PaymetSchema ()
@paymet.route('/addpaymet', methods=['POST'])
def add_paymet():
    paymet = service.register_paymet(paymet_schema.load(request.json))
    return paymet_schema.dump(paymet)

@paymet.route('/delete/<int:id>', methods=['PUT'])
def delete_paymet(id):
    service.delete_paymet(id)
    return '', 200  

@paymet.route('/find_by_id/<int:id>', methods=['GET'])
def find_by_id(id):
    paymet = paymet_schema.dump(service.get_paymet_by_id(id))
    if paymet is None:
        return jsonify({'message': 'Not foundx'}), 404
    return paymet



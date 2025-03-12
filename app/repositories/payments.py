from app import db
from sqlalchemy.exc import IntegrityError, NoResultFound
from app.Models.payments import Payment
from app.Services.format_logs import format_logs

logging = format_logs('PaymentRepository')

class PaymentRepository:

    def add_payment(self, payment: Payment) -> Payment:
        try:
            db.session.add(payment) 
            db.session.commit()
            logging.info(f'Payment {payment.id_payment} added successfully')
            return payment
        except IntegrityError as e:
            db.session.rollback()
            logging.error(f'Payment {payment.id_payment} cannot save, error {e}')
            raise e
        
    # def update_payment(self, payment: Payment) -> Payment:
    #     try:
    #         db.session.add(payment)
    #         db.session.commit()
    #         logging.info(f'Payment {payment.id_payment} updated successfully')
    #         return payment
    #     except IntegrityError as e:
    #         db.session.rollback()
    #         logging.error(f'Payment {payment.id_payment} cannot update, error {e}')
    #         raise e        

    def delete(self, payment: Payment) -> None:
        try:
            db.session.delete(payment)
            db.session.commit()
            logging.info(f'Payment {payment.id_payment} deleted successfully')
        except IntegrityError as e:
            db.session.rollback()
            logging.error(f'Payment {payment.id_payment} cannot be deleted, error {e}')
            raise e

    def find_by_id(self, id: int) -> Payment :
        try:
            res = db.session.query(Payment).filter(Payment.id_payment == id).one()
            logging.info(f'Payment with id {id} found successfully')
            return res
        except NoResultFound as e:
            logging.error(f'Payment id {id} not found, error {e}')
            raise e
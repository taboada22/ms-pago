from app import cache
from app.Models.payments import Payment
from app.Repositories.payments import PaymentRepository
from .format_logs import format_logs
from dataclasses import dataclass

logging = format_logs('PaymentServices')

@dataclass
class PaymentServices():
    repository = PaymentRepository()

    def add_payment(self, args: dict) -> Payment:
        payment = Payment()
        for key, value in args.items():
            if not payment.id_payment:
                setattr(payment, key, value) if hasattr(payment, key) else logging.warning("Unknown attr in add_payment")
        new_payment = self.repository.add_payment(payment)
        cache.set(f'payment_{new_payment.id_payment}', new_payment, timeout=300)
        logging.info(f'Payment_{new_payment.id_payment} added to cache')  
        return new_payment
    
    def delete_payment(self, id_payment: int) -> None:
        payment = self.repository.find_by_id(id_payment)
        if payment:
            payment.active = False
            cache.delete(f'payment_{id_payment}')
            logging.info(f'payment_{payment.id_payment} deleted to cache')
            self.repository.delete(payment)
            #payment = Payment()
            return None
            
        logging.error("Unknown payment to delete")
        return payment

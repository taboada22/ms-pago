from datetime import datetime
from app import cache
import logging
from app.models import Paymet
from app.repositories.paymet_repository import PaymetRepository

class PaymetService:  
    def __init__(self):  
        self.repository = PaymetRepository()  

    def register_paymet(self, paymet_data: Paymet) -> Paymet:
        return self.repository.save(paymet_data)
    
    def delete_paymet(self, id_paymet: int) -> bool:  
        paymet = self.repository.find_by_id(id_paymet)  
        if paymet:
            try:
                paymet.deleted_at = datetime.now()
                result = self.repository.save(paymet)
                cache.delete(f'pago_{result.id_paymet}')
            except Exception as e:
                logging.error(f'cancelando pago: {e}')
            return result
 
    
    def get_paymet_by_id(self, id_paymet: int) -> Paymet:  
        return self.repository.find_by_id(id_paymet)  

    def get_all(self) -> list:  
        return self.repository.get_all()
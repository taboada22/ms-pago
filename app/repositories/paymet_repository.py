from app import db
from app.models.paymet import Paymet
from sqlalchemy.exc import IntegrityError, NoResultFound

class PaymetRepository:
    def save(self, stock: Paymet) -> Paymet:
        try:
            db.session.add(stock) 
            db.session.commit()
            return stock
        except IntegrityError:
            db.session.rollback()
            print("Rollback en repository 1")
            
            
            
    def find_by_id(self, id: int) -> Paymet :
        try:
            return db.session.query(Paymet).filter(Paymet.id_paymet == id).one()
        except NoResultFound:
            return None

    def get_all(self) -> list:  
        return db.session.query(Paymet).all()
    

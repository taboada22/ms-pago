import unittest
from app.Services.payments import PaymentServices
from . import BaseTestClass

class PaymentTestCase(BaseTestClass):

    service = PaymentServices()

    def test_add_payment(self):
        payment = self.service.add_payment(self.payment_4)

        for key in self.payment_4.keys():
            self.assertEqual(self.payment_4[key], getattr(payment, key))
    
    def test_update_payment(self):
        payment = self.service.update_payment(2, self.payment_4)
        for key in self.payment_4.keys():
            self.assertEqual(self.payment_4[key], getattr(payment, key))

    def test_get_by_id(self):
        payment = self.service.find_by_id(3)

        for key in self.payment_3.keys():
            self.assertEqual(self.payment_3[key], getattr(payment, key))

    def test_delete_payment(self):
        payment = self.service.delete_payment(1)
        self.assertIsNone(payment)


if __name__ == '__main__':
    unittest.main()
    
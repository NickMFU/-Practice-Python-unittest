import bankinittest.banking as banking
import unittest
# Create Class Test
class TestBankAccount:
    # Create Test Method
    def test_deposit(self):
        obj = banking.BankAccount(1000001, 5000)
        obj.deposit(100)
        obj.deposit(500)
        obj.deposit(400)
        assert obj.balance == 6000

    def test_withdraw(self):
        obj = banking.BankAccount(1000002, 1000)
        obj.withdraw(100)
        obj.withdraw(200)
        obj.withdraw(400)
        assert obj.balance == 300 


if __name__ == '__main__':
    unittest.main()
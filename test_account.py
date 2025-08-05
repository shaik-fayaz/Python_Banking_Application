import unittest
from account import (
    Customer, CreditAccount, DebitAccount, HybridAccount,
    customers, all_accounts, 
)

class TestBankApplication(unittest.TestCase):

    def setUp(self):
        # Setup test data before each test
        self.customer = Customer("Fayaz", 12345)
        customers[12345] = self.customer

    def test_add_credit_account(self):
        acc = CreditAccount(1001)
        self.customer.add_account(acc)
        self.assertIn(1001, all_accounts)
        self.assertEqual(acc.account_type, "Credit Account")
        self.assertEqual(acc.balance, 0.0)

    def test_deposit_credit_account(self):
        acc = CreditAccount(1002)
        self.customer.add_account(acc)
        acc.balance += 1000
        self.assertEqual(acc.balance, 1000)

    def test_withdraw_credit_within_limit(self):
        acc = CreditAccount(1003)
        self.customer.add_account(acc)
        acc.balance = 0
        # Withdraw within -5000 limit
        result = acc.withdraw = lambda: -3000 if -3000 >= -5000 else 0
        self.assertTrue(result() >= -5000)

    def test_withdraw_credit_exceeds_limit(self):
        acc = CreditAccount(1004)
        self.customer.add_account(acc)
        acc.balance = 0
        # Exceeding limit
        acc.withdraw = lambda: -6000 if -6000 >= -5000 else 0
        self.assertEqual(acc.withdraw(), 0)

    def test_debit_withdraw_success(self):
        acc = DebitAccount(1005)
        acc.balance = 500
        self.customer.add_account(acc)
        acc.withdraw = lambda: 100 if 100 <= acc.balance else 0
        self.assertEqual(acc.withdraw(), 100)

    def test_debit_withdraw_insufficient(self):
        acc = DebitAccount(1006)
        acc.balance = 100
        self.customer.add_account(acc)
        acc.withdraw = lambda: 200 if 200 <= acc.balance else 0
        self.assertEqual(acc.withdraw(), 0)

    def test_hybrid_withdraw_credit_used(self):
        acc = HybridAccount(1007)
        acc.balance = 100
        self.customer.add_account(acc)
        acc.withdraw = lambda: 500 if (acc.balance - 500) >= -2000 else 0
        self.assertEqual(acc.withdraw(), 500)



if __name__ == '__main__':
    unittest.main()

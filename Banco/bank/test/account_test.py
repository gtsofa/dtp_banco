#account test goes here

import unittest

from bank.account import Account

class TestAccountClass(unittest.TestCase):
    """Test Account Class"""
    def test_account_object_returns_current_balance(self):
        """Test if account object returns current balance."""
        account = Account('001', 50)
        self.assertEqual(account.account_number, '001')
        self.assertEqual(account.account_balance, 50)

if __name__ == '__main__':
    unittest.main()


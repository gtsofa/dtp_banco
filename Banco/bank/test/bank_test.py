#bank test for a bank class

import unittest

from bank.bank import Bank
from bank.account import Account

class TestBankClass(unittest.TestCase):
    """Test bank class if it can uniquely identify account number and retrieve it's balance """
    
    def test_bank_is_initially_empty(self):
        """Test bank if it is initially empty"""
        bank = Bank()
        self.assertEqual({}, bank.accounts)
        self.assertEqual(len(bank.accounts), 0)
        
    def test_add_account(self):
        """Test add bank account """
        bank = Bank()
        
        account_1 = Account('001', 50)
        account_2 = Account('002', 30)
        
        bank.add_account(account_1)
        bank.add_account(account_2)
        
        self.assertEqual(len(bank.accounts), 2)
        
    def test_get_account_balance(self):
        """Test get account balance """
        bank = Bank()
        
        account_1 = Account('001', 50)
        bank.add_account(account_1)
        
        self.assertEqual(bank.get_account_balance('001'), 50)
        
    
if __name__ == '__main__':
    unittest.main()
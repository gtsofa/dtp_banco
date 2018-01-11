#bank test for a bank class

import unittest

from bank.bank import Bank

class TestBankClass(unittest.TestCase):
    """Test bank class """
    
    def test_bank_is_initially_empty(self):
        """Test bank if it is empty"""
        bank = Bank()
        self.assertEqual({}, bank.accounts)
        self.assertEqual(len(bank.accounts), 0)
    
if __name__ == '__main__':
    unittest.main()
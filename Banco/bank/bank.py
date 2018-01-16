#bank class
"""
accounts = {
  'tsofa nyule': {
    'account_number':'001',
    'account_balance':50
  },
  'sarah munga': {
    'account_number':'002',
    'account_balance':300
  },
  'maestro giulio': {
    'account_number': '003',
    'account_balance': 720
  }
  
}

for user, account in accounts.items():
  print(user +"..> " "Account number: "+ account['account_number'] + " Account balance: " + str(account['account_balance']))
  

"""

class Bank():
    """Bank class that stores All Accounts in a dictionary."""
    
    def __init__(self):
        """initialize bank class"""
        self.accounts = {} #empty dictionary that will contain all the accounts
        
    def add_account(self, account):
        """add individual account to the bank class"""
        self.accounts[account.account_number] = account.account_balance
        
    def get_account_balance(self, account_number):
        """return account balance"""
        return self.accounts.get(account_number)
        
        
        

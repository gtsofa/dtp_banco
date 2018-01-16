#account implementation code goes here 

class Account():
    """A class that model a bank account"""
    def __init__(self, account_number, account_balance):
        """initialize parameters"""
        self.account_number = account_number
        self.account_balance = account_balance
        
    def add_account(self):
        """this add bank account of an individual"""
        
        print("Account number "+ self.account_number +" has Kshs."+ str(self.account_balance) + " only as balance")
        
account = Account('001', 20)
accountb = Account('002', 30)
account_1 = account.add_account()
account_2 = accountb.add_account()
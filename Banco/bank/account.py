#account implementation code goes here 

class Account():
    """A class that model a bank account"""
    def __init__(self, account_number, account_balance):
        """initialize parameters"""
        self.account_number = account_number
        self.account_balance = account_balance
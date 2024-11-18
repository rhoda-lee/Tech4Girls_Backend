class BankAccount:
    bank_name = 'Tech4Girls Bank' # added a class variable
    def __init__(self, account_holder, balance = 0):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        '''method to deposit to account'''
        if amount > 0:
            self.balance += amount
            return f'${amount} added successfully.\nCurrent balance: {self.balance}\n'
        else:
            return f'Enter a positive number to deposit\n'
        
    def withdraw(self, amount):
        '''method to withdraw from account'''
        if amount <= 0:
            return f'Amount to be withdrawn must be positive\n'
        
        if amount > self.balance:
            return f'Insufficient balance. Withdraw a lesser amount\n'
        else:
            self.balance -= amount
            return f'${amount} withdrawn successfully. \nCurrent balance: {self.balance}\n'
        
    ''''static method ro display bank policy'''
    @staticmethod
    def bank_policy():
        return f'We are committed to your financial freedom'
    
    '''class method toreturn our bank's name'''
    @classmethod
    def get_bank_name(cls):
        return cls.bank_name
    

# Creating the first instance of the class BankAccount
acc1 = BankAccount('Dede')
print(acc1.deposit(5000))
print(acc1.balance)

# Creating the second instance of the class BankAccount
acc2 = BankAccount('Rhoda')
print(acc2.deposit(4000))
print(acc2.balance)
print(acc2.withdraw(5000))
print(acc2.balance)

# Creating the third instance of the class BankAccount
acc3 = BankAccount('Nabi')
print(acc3.withdraw(-4500))
print(acc3.deposit(-650))

# Use of class method get_bank_name()
print(BankAccount.get_bank_name())

# Use of static method bank_policy()
print(BankAccount.bank_policy())





        

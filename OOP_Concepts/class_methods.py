class BankAccount:
    bank_name = 'Tech4Girls Bank'
    def __init__(self, account_holder, balance = 0):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f'${amount} added successfully.\nCurrent balance: {self.balance}\n'
        else:
            return f'Enter a positive number to deposit\n'
        
    def withdraw(self, amount):
        if amount <= 0:
            return f'Amount to be withdrawn must be positive\n'
        
        if amount > self.balance:
            return f'Insufficient balance. Withdraw a lesser amount\n'
        else:
            self.balance -= amount
            return f'${amount} withdrawn successfully. \nCurrent balance: {self.balance}\n'
        
    @staticmethod
    def bank_policy():
        return f'We are committed to your financial freedom'
    
    @classmethod
    def get_bank_name(cls):
        return cls.bank_name
    


acc1 = BankAccount('Dede')
print(acc1.deposit(5000))
print(acc1.balance)

acc2 = BankAccount('Rhoda')
print(acc2.deposit(4000))
print(acc2.balance)
print(acc2.withdraw(5000))
print(acc2.balance)

acc3 = BankAccount('Nabi')
print(acc3.withdraw(-4500))
print(acc3.deposit(-650))

print(BankAccount.get_bank_name())

print(BankAccount.bank_policy())





        

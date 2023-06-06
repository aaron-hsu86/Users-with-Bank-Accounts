class BankAccount:
    # declare a class attribute
    all_accounts = []

    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    def deposit(self, amount):
        # your code here
        self.balance += amount
        # print(f'User deposited ${amount}')
        return self
    def withdraw(self, amount):
        # your code here
        if amount <= self.balance:
            self.balance -= amount
            # print(f'User withdrew {amount}\nUpdated balance: ${self.balance}')
        else:
            print('Insufficient funds: Charging a $5 fee')
            self.balance -= 5
        return self
    def display_account_info(self):
        # your code here
        print(f'Balance: ${self.balance}')
        return self
    def yield_interest(self):
        # your code here
        if self.balance > 0:
            self.balance += self.balance*self.int_rate
            # print(f'Yeld Interest: {self.int_rate*100}%\nUpdated balance: ${self.balance}')
        else:
            print('Not enough money in account')
        return self
    # NINJA BONUS: use a classmethod to print all instances of a Bank Account's info
    @classmethod
    def display_all_bank_info(cls):
        for index, account in enumerate(cls.all_accounts):
            print(f'Account {index+1} Balance: ${account.balance}')

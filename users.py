from bank_accounts import BankAccount

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {
            "checking" : BankAccount(0.02, 0),
            "savings" : BankAccount(0.01, 0)
        }
    
    # make deposit into account
    def make_deposit(self, account_name, amount):
        if self.valid_account(account_name, self):
            self.accounts[account_name].deposit(amount)
        return self
    # make withdrawal from account
    def make_withdrawal(self, account_name, amount):
        if self.valid_account(account_name, self):
            self.accounts[account_name].withdraw(amount)
        return self
    # display account balance
    def display_user_balance(self):
        print(f'{self.name}\'s Bank Accounts')
        # display balance for all user's accounts
        for acc in self.accounts:
            print(f'{acc.capitalize()} Account')
            self.accounts[acc].display_account_info()

        return self
    # transfer from one account to another
    def transfer_money(self, account_name, amount, other_user, other_account):
        # check if both users have valid accounts
        if self.valid_account(account_name, self) and other_user.valid_account(other_account, other_user):
            # attempt withdrawal
            self.accounts[account_name].withdraw(amount)
            # only proceed with giving other account money if user has enough
            if self.accounts[account_name].balance >= amount:
                other_user.accounts[other_account].deposit(amount)
        else:
            print('Please check account names')
        return self

    @staticmethod
    # Function to check if account name is valid
    def valid_account(account_name, self):
        if account_name == 'savings' or account_name == 'checking':
            return True
        else:
            print(f'{self.name} does not have a {account_name} account.\nPlease check spelling.')
            return False

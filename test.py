from users import User

adriensAccount = User('Adrien', 'adrien@mail.com')
sadiesAccount = User('Sadie', 'sadie@mail.com')

adriensAccount.make_deposit('checking', 500)
adriensAccount.display_user_balance('savings')
sadiesAccount.display_user_balance('checking')
adriensAccount.transfer_money('savings', 100, sadiesAccount, 'checking')
adriensAccount.display_user_balance('savings')
sadiesAccount.display_user_balance('checking')
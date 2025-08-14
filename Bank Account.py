class PersonAccount:
    def __init__(self, firstname='Fred', lastname='James'):
        self.firstname = firstname
        self.lastname = lastname
        self.income = {}
        self.expenses = {}

    def ask_name(self):
        self.firstname = input('What is your first name? ')
        self.lastname = input('What is your last name? ')
        return f'\nWelcome to your Bank Account, {self.firstname} {self.lastname}' 


    def add_income(self):
        ask_inc = int(input('\nHow many sources of income? '))
        for i in range(ask_inc):
            user_inc = input('\nWhat is the income? ')
            inc_amt = int(input('How much do you earn in this? '))
            self.income[user_inc] = inc_amt
        
        total_income = sum(self.income.values())
        return f'\nYour total income is {total_income}'


    def add_expenses(self):
        ask_exp = int(input('\n\nHow many expenses? '))
        for i in range(ask_exp):
            user_exp = input('\nWhat is the expense? ')
            inc_exp = int(input('How much is this? '))
            self.expenses[user_exp] = inc_exp
        
        total_expense = sum(self.expenses.values())
        return f'\nYour total expenses is {total_expense}'


    def account_balance(self):
        total_income = sum(self.income.values())
        total_expense = sum(self.expenses.values())
        balance = total_income - total_expense
        return f'Your account balance is {balance}'


p1 = PersonAccount()
print(p1.ask_name())
print(p1.add_income())
print(p1.add_expenses())
print(p1.account_balance())
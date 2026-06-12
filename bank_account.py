class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def show_balance(self):
        print(f'{self.owner} ваш баланс: {self.balance}')

    def deposit(self, ammount):
        self.balance += ammount

    def withdraw (self, ammount):
        if self.balance >= ammount:
            self.balance = self.balance - ammount
        else:
            print("Недостаточно средств")

account_1 = Account("Денис", 10000)
account_1.show_balance()
account_1.deposit(10000)
account_1.show_balance()
account_1.withdraw(100000)
account_1.show_balance()






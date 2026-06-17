class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit (self, ammount):
        self.__balance += ammount

    def withdraw (self, ammount):
        if ammount <= self.__balance:
            self.__balance -= ammount
        else:
            print("Недостаточно средств")

    def show_balance(self):
        print(f"На вашем балансе {self.__balance}")

BankAccount1 = BankAccount("Денис", 100)
BankAccount1.deposit(500)
BankAccount1.show_balance()
print(BankAccount1.__balance)
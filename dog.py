class Dog:
    def __init__(self, name):
        self.name = name

    def meet(self, other):
        print(f"{self.name} встретил {other.name}")

dog1 = Dog("Шарик")
dog2 = Dog("Бобик")

dog1.meet(dog2)

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def transfer(self, other, amount):
        other.balance += amount
        self.balance -= amount
        print(self.owner, self.balance)
        print(other.owner, other.balance)


denis = BankAccount("Денис", 10000)
ivan = BankAccount("Иван", 5000)

denis.transfer(ivan, 5000)
class Safe:

    def __init__(self, owner, money):
        self.owner = owner
        self.__money = money

    def put_money(self, amount):
        self.__money += amount

    def take_money(self, amount):
        if self.__money >= amount:
            self.__money -= amount
        else:
            print("Не хватает денег")

    def show_money(self):
        print(f"В сейфе {self.owner} находится {self.__money} рублей")

Safe1 = Safe("Денис", 1000)
Safe1.show_money()
Safe1.put_money(1000)
Safe1.show_money()
Safe1.take_money(500)
Safe1.show_money()
print(Safe1.__money)

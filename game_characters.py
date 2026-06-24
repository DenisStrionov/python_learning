class Character:
    def attack(self):
        print("Персонаж атакует")

class War(Character):
    def attack(self):
        print("Воин бьет мячом")

class Mage(Character):
    def attack(self):
        print("Маг кидает огненный шар")

class Archer(Character):
    def attack(self):
        print("Лучник стреляет из лука")

character1 = Character()
war = War()
mage = Mage()
archer = Archer()

character1.attack()
war.attack()
mage.attack()
archer.attack()
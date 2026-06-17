class Player:
     def __init__(self, name, hp):
         self.name = name
         self.__hp = hp

     def show_hp(self):
        print(self.__hp)

player = Player("Денис", 100)

player.show_hp()
print(player.__hp)

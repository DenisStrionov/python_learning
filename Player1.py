class Player:
    def __init__(self, hp):
        self.__hp = hp

    def get_hp(self):
        return self.__hp

    def set_hp(self, hp):
        self.__hp = hp


player = Player(100)
print(player.get_hp())
player.set_hp(200)
print(player.get_hp())
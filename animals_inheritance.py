class Animal:

    def voice(self):
        print("Животное издает звук")

class Cat(Animal):
    # pass
    def voice(self):
        print("Мяу")

class Dog(Animal):
    # pass
    def voice(self):
        print("Гаф")

animal = Animal()
cat = Cat()
dog = Dog()

animal.voice()
cat.voice()
dog.voice()
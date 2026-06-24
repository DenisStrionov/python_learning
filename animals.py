class Dog:

    def voice(self):
        print("Гаф")

class Cat:

    def voice(self):
        print("Мяу")

dog = Dog()
cat = Cat()
dog.voice()
cat.voice()

class Car:
    def move(self):
        print("Автомобиль едет")

class Plane:
    def move(self):
        print("Самолет летит")

class Boat:
    def move(self):
        print("Лодка плывет")

car = Car()
plane = Plane()
boat = Boat()

car.move()
plane.move()
boat.move()
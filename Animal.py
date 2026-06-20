class Animal:
    def eat(self):
        print("Я ем")

class Dog(Animal):
    pass

dog = Dog()
dog.eat()
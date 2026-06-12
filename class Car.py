class Car:

    def __init__(self, model, fuel):
        self.model = model
        self.fuel = fuel

    def refuel(self, litters):
        self.fuel += litters

    def show_info(self):
        print("Модель", self.model)
        print("Топливо", self.fuel)

car = Car("Toyota", 20)
car.show_info()
car.refuel(10)
car.show_info()
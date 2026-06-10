class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year
    def show_info(self):
        print("Марка:", self.model,)
        print("Год:", self.year)

car1 = Car("Ford", 2012 )
car2 = Car("Ferari", 2020)
car1.show_info()
car2.show_info()

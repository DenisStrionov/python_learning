class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_info(self):
        print(self.name)
        print(self.salary)

class Lawyer(Employee):

    def __init__(self, name, salary, rank):
        super().__init__(name, salary)
        self.rank = rank

    def show_info(self):
        super().show_info()
        print(self.rank)

denis = Lawyer("Денис", 10000, "советник")
denis.show_info()

class Investigator(Employee):
    pass

class Prosecutor(Employee):
    pass

investigator = Investigator("Иван", 20000)

prosecutor = Prosecutor("Петр", 40000)

prosecutor.show_info()
investigator.show_info()
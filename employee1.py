class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_info(self):
        print("Имя", self.name)
        print("Зарплата", self.salary)

    def raise_salary(self, amount):
        self.salary += amount

denis = Employee("Денис", 10000)

denis.show_info()

denis.raise_salary(5000)

denis.show_info()

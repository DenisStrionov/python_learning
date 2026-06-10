class Employee():

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def say_hello(self):
        print(f"Здраствуйте, меня зовут {self.name}")

employee1 = Employee("Денис", "Юрист")
print(employee1.name)
print(employee1.position)

employee1.say_hello()

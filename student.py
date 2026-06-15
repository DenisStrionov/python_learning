class Student:

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def show_info(self):
        print("Имя:", self.name)
        print("Возраст:", self.age)
        print("Средний балл:", self.score)

student1 = Student("Иванов И.И.", 20, 90)
student2 = Student("Петров П.П.", 18, 60)
student3 = Student("Сидоров С.С.", 23, 70)

student1.show_info()
student2.show_info()
student3.show_info()
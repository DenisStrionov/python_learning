def calculate_salary(hours, rate):
    return hours * rate

hours = int(input("Отработано часов: "))
rate = int(input("Ставка за час: "))

salary = calculate_salary(hours, rate)

print(f"Зарплата: {salary} руб.")
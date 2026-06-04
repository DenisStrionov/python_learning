user = {}

name = input("Введите имя: ")
city = input("Введите город: ")

skills_input = input("Введите навыки через пробел: ")

skills = skills_input.split()

user["name"] = name
user["city"] = city
user["skills"] = skills

print("\nПрофиль пользователя: ")
print(f"Имя: {user['name']}")
print(f"Город: {user['city']}")

print("Навыки: ")

for skill in user["skills"]:
    print("-", skill)
user = {}

name = input("Введите имя: ")
age = input("Введите возраст: ")
city = input("Введите город: ")

user["name"] = name
user["age"] = age
user["city"] = city

print("Карточка пользователя: ")
print(f"Имя: {user["name"]}")
print(f"Возраст: {user["age"]}")
print(f"Город: {user["city"]}")
print(user)
# name = input ("Введите имя: ")
# city = input("Введите город: ")
# age = int(input("Ввдите возраст: "))
# if age >= 18:
#     print("Доступ разрешен")
#     print("Привет, ", name.upper())
#     print("Ты из города ", city)
# else:
#     print("Доступ запрещен")
while True:
    name = input ("Введите имя: ")
    if len(name) >= 5:
        print("Нормальная длина имени!")
        city = input("Введите город: ")
        age = int(input("Введите возраст: "))
        break
    else:
        print ("Имя слишком короткое!")
if age >= 18:
    print("Доступ разрешен")
    print("Привет,", name.upper())
    if city.lower() == "москва":
        print("Ты из столицы!")
    else:
        print("Ты из города", city)
else:
    print("Доступ запрещен")
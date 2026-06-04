password = "12345"
attempts = 3

while attempts > 0:
    user_password = input("Введите пароль: ")

    if user_password == password:
        print("Доступ разрешен")
        break
    else:
        attempts = attempts - 1
        print("Неверный пароль. Осталось попыток: ", attempts)

else:
    print("Попытки закончились. Доступ заблокирован")

# password = "12345"
# attempts = 3
#
# while attempts > 0:
#     user_password = input("Введите пароль: ")
#     if user_password == password:
#         print("Доступ разрешен.")
#         break
#     else:
#         attempts = attempts - 1
#         print("Неверный пароль.")
# if attempts == 0:
#     print("Доступ заблокирован.")

count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print (count)

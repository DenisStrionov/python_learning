# count = 1
# while count <= 10:
#     print(count)
#     count = count + 1

while True:
    name = input("Введите имя: ")
    if len(name) >= 5 and name.isalpha():
        print("Имя принято.")
        break
    else:
        print("Имя не должно быть короче 5 символов")
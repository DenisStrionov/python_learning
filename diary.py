# note = input("Введите запись: ")
# file = open("notes.txt", "a", encoding="utf-8")
# file.write(input("Введите запись: ") + "\n")
# file.close()

# with open("notes.txt", "a", encoding="utf-8") as file:
#     file.write(input("Введите запись: ") + "\n")
# try:
#     while True:
#
#         note = input("Введите запись (выход для завершения): ")
#
#         if note.lower() == "выход":
#             break
#
#         with open("notes.txt", "a", encoding="utf-8") as file:
#             file.write(note + "\n")
#
#         print("Запись сохранена")
#
# except:
#     print("Произошла ошибка")

# file = open("notes.txt", "w", encoding="utf-8")
# print(file)

file = open("notes.txt", "a", encoding="utf-8")

file.write("Сегодня изучаю файлы")

file.close()




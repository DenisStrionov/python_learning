# file = open ("hello.txt", "r", encoding="utf-8")
# text = file.read()
# print(text)
# file.close()
#
# file = open ("notes.txt", "r", encoding="utf-8")
# file.write("Сегодня изучаю файлы")
# file.close()

file = open("notes.txt", "a", encoding="utf-8")
file.write("\nЗавтра изучаю исключения")
file.close()
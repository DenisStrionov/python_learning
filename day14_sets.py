# numbers = [1, 2, 2, 3, 3, 4, 5, 5]
# unique_numbers = set(numbers)
# print(unique_numbers)
#
# files = {"photo.jpg", "video.mp4", "doc.pdf"}
# file_name = input("Введите имя файла: ")
# if file_name in files:
#     print("Файл найден")
# else:
#     print("Файл не найден")

my_skills = {"python", "html", "css"}
job_skills = {"python", "git", "sql"}

print("Все навыки: ", my_skills | job_skills)
print("Совпадают: ", my_skills & job_skills)
print("Не хватает: ", job_skills - my_skills)
print("Лишние навыки", my_skills - job_skills)
print("Различаются: ", my_skills ^ job_skills)

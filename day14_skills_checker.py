required_skills = {"python", "git", "sql"}
junior_required = {"python", "git", "sql"}
middle_required = {"python", "git", "sql", "docker", "api"}

user_input = input("Введите ваши навыки через пробел: ")

my_skills = set(user_input.lower().split())

matched_skills = my_skills & required_skills
missing_skills = required_skills - my_skills
extra_skills = my_skills - required_skills
print()
print("=== Анализ навыков ===")
print("Ваши навыки: ", my_skills)
print("Совпадающие навыки: ", matched_skills)
print("Не хватает: ", missing_skills)
print("Дополнительные навыки: ", extra_skills)

if not missing_skills:
    print("Вы подходите по базовым навыкам")
else:
    print("Нужно подтянуть: ", missing_skills)

junior_missing = junior_required - my_skills
middle_missing = middle_required - my_skills

print("До junior не хватает: ", junior_missing)
print("До middle не хватает: ", middle_missing)

if not junior_missing:
    print("До junior требований вы дотягиваете")
else:
    print("До junior надо подтянуть: ", junior_missing)

if not middle_missing:
    print("До middle требований вы дотягиваете")
else:
    print("До middle надо подтянуть: ", middle_missing)




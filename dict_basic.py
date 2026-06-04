user = {"name": "Денис", "age": 35, "city": "Чита"}
print(user)
print(user["name"])
print(user["age"])
print(user["city"])

user["age"] = 36
user["profession"] = "Python-разработчик"
print(user)


countries = {
    "Россия": "Москва",
    "Белоруссия": "Минск",
    "Германия": "Берлин"
}
country = input("Введите страну: ")
print(countries[country])
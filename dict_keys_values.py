user = {
    "name": "Денис",
    "age": 35,
    "city": "Чита"
}
print(list(user.keys()))
print(list(user.values()))

for key, value in user.items():
    print(key,value)

del user["city"]
print(user)

age = user.pop("age")
print(age)
print(user)
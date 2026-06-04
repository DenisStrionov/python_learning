# def add(a, b):
#     return a + b
#
# result = add (10, 5)
# print(result)
#
# def show_user(name, age):
#     print(f"Имя: {name}")
#     print(f"Возраст: {age}")
#
# show_user("Денис", 35)

# def greet (name = "Гость"):
#     print(f"Привет, {name}")
#
# greet()
# greet("Денис")

def discount(price, percent):
    return price - (price * percent / 100)

result  = discount(10000, 15)

print(result)

user_name = input("Введите имя: ")

def create_greeting(name):
    return f"Привет, {name}"

message = create_greeting(user_name)

print(message)
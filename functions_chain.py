# def square(number):
#     return number ** 2
#
# def double(number):
#     return number * 2
#
# result = double(square(5))
#
# print(result)

def check_age(age):
    if age >= 18:
        return "Совершеннолетний"

    return "Несовершеннолетний"

print(check_age(25))
print(check_age(12))

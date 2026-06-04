numbers = [1, 2, 3, 4, 5, 6]
new_numbers = []

for number in numbers:
    new_numbers.append(number * 2)

print(new_numbers)

result = list(map(lambda x: x * 2, numbers))

print(result)

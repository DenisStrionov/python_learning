names = ["денис", "анна", "иван"]

result = list(map(lambda name: name.capitalize(), names))
print(result)

new_names = []
for name in names:
    new_names.append(name.capitalize())

print(new_names)
# numbers = [1, 2, 3, 1, 2, 4, 5, 5]
#
# unique_numbers = set(numbers)
# print("Список: ", numbers)
# print("Множество: ", unique_numbers)

products = {"Хлеб", "Молоко", "Сыр"}
print(products)
products.add("Чай")
print(products)

product = input("Введите продкут: ")

if product in products:
    print("Такой продукт уже есть в списке")
else:
    products.add(product)
    print("Продукт добавлен")
print(products)

delete_product = input("Какой продукт удалить?")
products.discard(delete_product)
print(products)

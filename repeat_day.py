from shoping_cheker import new_prices

products = ["Хлеб", "Молоко", "Сыр"]
prices = [50, 90, 60]
new_products = input("Введите новый продукт: ")

if new_products not in products:
    new_prices = int(input("Введите цену: "))
    products.append(new_products)
    prices.append(new_prices)

    print("Продукт добавлен: ")
else:
    print("Такой продкут уже есть в списке.")

items = list(zip(products, prices))
print(items)

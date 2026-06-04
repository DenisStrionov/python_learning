products = ["Хлеб", "Молоко", "Сыр"]
prices = [50, 100, 90]
new_product = input("Введите новый продукт: ")
if new_product not in products:
    new_prices = int(input("Введите цену: "))
    products.append(new_product)
    prices.append(new_prices)

    print("Продукт и цена добавлены.")
else:
    print("Такой продукт уже есть.")

print("Список продуктов: ", products)
print("Список продуктов: ", prices)

items = list(zip(products, prices))

print("Товары и цены: ", items)
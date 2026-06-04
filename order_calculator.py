from statistics import quantiles


def calculate_total(price, quantity):
    return price * quantity


price = int(input("Цена товара: "))
quantity = int(input("Количество: "))

total = calculate_total(price, quantity)

print(f"Итого: {total} руб.")
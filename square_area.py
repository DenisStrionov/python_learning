def square_area(side):
    return side * side

side = int(input("Введите сторону квадрата: "))
area = square_area(side)

print(f"Площадь квадрата: {area}")
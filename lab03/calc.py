num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

print(f"Сумма: {num1 + num2}")
print(f"Разность: {num1 - num2}")
print(f"Произведение: {num1 * num2}")


if num2 != 0:
    print(f"Частное: {num1 / num2}")
else:
    print("Ошибка: Деление на ноль невозможно!")

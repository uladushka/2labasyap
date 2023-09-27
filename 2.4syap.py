try:
    x = int(input("Введите число: "))
    result = 10 / x
    print("Результат:", result)

except ValueError:
    print("Ошибка! Введено некорректное число.")

except ZeroDivisionError:
    print("Ошибка! Деление на ноль.")

finally:
    print("Программа завершена.")
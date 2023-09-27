def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return factorial(n-1) * n

n = int(input("Введите число"))
if n < 0:
    print("ошибка ввода")
else:
    print(factorial(n))
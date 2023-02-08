# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

num = int(input("Введите n: "))
fib1 = 0
fib2 = 1
fib3 = 1
fib4 = -1
num_list = []
for i in range(1, num):
    a = fib4
    fib4 = fib3 - fib4
    fib3 = a
    num_list.append(a)
print(*num_list[:: -1], end=' ')
print(fib2,fib1, end=' ')
for i in range(1, num + 1):
    b = fib2
    fib2 = b + fib1
    fib1 = b
    print(b, end=' ')
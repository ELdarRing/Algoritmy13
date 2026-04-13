#Задание 1(4)
import time

n = 1000000

start = time.time()
sum_cycle = 0
for i in range(1, n + 1):
    sum_cycle += i
end = time.time()
print("Сумма через цикл:", sum_cycle)
print("Время (цикл):", end - start)

start = time.time()
sum_formula = n * (n + 1) // 2
end = time.time()
print("Сумма через формулу:", sum_formula)
print("Время (формула):", end - start)

#Задание 2(7)
n = 1000
i = 1
count = 0

while i < n:
    i *= 2
    count += 1

print("Количество шагов:", count)

#Задание 3(11)
import time

def fib_rec(n):
    if n <= 1:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)

def fib_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

n = 30

start = time.time()
print("Рекурсия:", fib_rec(n))
print("Время рекурсии:", time.time() - start)

start = time.time()
print("Итерация:", fib_iter(n))
print("Время итерации:", time.time() - start)

#Задание 4(20)
import random

arr = [random.randint(1, 10) for _ in range(10)]
print("Массив:", arr)

def range_sum(arr, l, r):
    return sum(arr[l:r+1])

prefix = [0] * len(arr)
prefix[0] = arr[0]

for i in range(1, len(arr)):
    prefix[i] = prefix[i-1] + arr[i]

def prefix_sum(l, r):
    if l == 0:
        return prefix[r]
    return prefix[r] - prefix[l-1]

print("Обычная сумма (2,5):", range_sum(arr, 2, 5))
print("Префиксная сумма (2,5):", prefix_sum(2, 5))
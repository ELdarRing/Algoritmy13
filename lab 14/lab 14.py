#Задание 1
nums = [1, 2, 3, 2, 4, 5, 1, 6]

duplicates = []
seen = set()

for num in nums:
    if num in seen and num not in duplicates:
        duplicates.append(num)
    seen.add(num)

print(duplicates)

#Задание 2
nums = [1, 2, 2, 3, 3, 3, 4]

most_common = max(set(nums), key=nums.count)

print(most_common)

#Задание 3
nums = [2, 7, 11, 15]
target = 9

seen = set()

for num in nums:
    if target - num in seen:
        print(num, target - num)
        break
    seen.add(num)

#Задание 4
strings = ["apple", "kiwi", "banana", "fig"]

sorted_strings = sorted(strings, key=len)

print(sorted_strings)

#Задание 5
from collections import Counter

text = "apple banana apple orange banana apple kiwi banana"

words = text.split()
counter = Counter(words)

top3 = counter.most_common(3)

print(top3)

#Задание 6
nums = [1, 2, 2, 3, 1, 4]

unique = []
seen = set()

for num in nums:
    if num not in seen:
        unique.append(num)
        seen.add(num)

print(unique)

#Задание 7
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

intersection = list(set(a) & set(b))

print(intersection)

#Задание 8
students = [
    ("Eldar", 85),
    ("Aruzhan", 92),
    ("Dias", 78)
]

top_student = max(students, key=lambda x: x[1])

print(top_student)

#Задание 9
nums = [1, 2, 3, 4, 5, 6]

even = [x for x in nums if x % 2 == 0]
odd = [x for x in nums if x % 2 != 0]

print("Чётные:", even)
print("Нечётные:", odd)

#Задание 10
nums = [1, 1, 2, 2, 2, 3, 3, 1]

max_len = 1
current_len = 1

for i in range(1, len(nums)):
    if nums[i] == nums[i - 1]:
        current_len += 1
        max_len = max(max_len, current_len)
    else:
        current_len = 1

print(max_len)

#Задание 11
users = {}

while True:
    print("\n1. Добавить")
    print("2. Найти")
    print("3. Удалить")
    print("4. Показать всех")
    print("5. Выход")

    choice = input("Выбор: ")

    if choice == "1":
        name = input("Имя: ")
        age = input("Возраст: ")
        users[name] = age
        print("✅ Добавлено")

    elif choice == "2":
        name = input("Имя для поиска: ")
        if name in users:
            print(f"{name}: {users[name]} лет")
        else:
            print("❌ Не найден")

    elif choice == "3":
        name = input("Имя для удаления: ")
        if name in users:
            del users[name]
            print("🗑 Удалено")
        else:
            print("❌ Не найден")

    elif choice == "4":
        print(users)

    elif choice == "5":
        break
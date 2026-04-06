#Задание 1
students = {
    "Алина": 5,
    "Диас": 4,
    "Данияр": 3,
    "Арыстан": 5
}

for name, grade in students.items():
    print(f"{name} – {grade}")

#Задание 2
numbers = [5, 2, 5, 3, 2, 5]
count_dict = {}

for num in numbers:
    count_dict[num] = count_dict.get(num, 0) + 1

print(count_dict)

#Задание 3
text = "algorithm"
char_count = {}

for char in text:
    char_count[char] = char_count.get(char, 0) + 1

print(char_count)

#Задание 4
phone_book = {
    "Алина": "123456",
    "Бекзат": "234567",
    "Данияр": "345678",
    "Ержан": "456789",
    "Айжан": "567890"
}

name = input("Введите имя: ")

if name in phone_book:
    print("Номер:", phone_book[name])
else:
    print("Контакт не найден")

#Задание 5
words = ["cat", "dog", "cat", "bird", "dog", "dog"]
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

duplicates = [word for word, count in word_count.items() if count > 1]

print(duplicates)

#Задание 6
str1 = "listen"
str2 = "silent"

if sorted(str1) == sorted(str2):
    print("Это анаграммы")
else:
    print("Это не анаграммы")

#Задание 7
products = {
    "Хлеб": 100,
    "Молоко": 300,
    "Яблоко": 200
}

products["Сок"] = 400

products["Молоко"] = 350

del products["Хлеб"]

product_name = input("Введите товар: ")
print("Цена:", products.get(product_name, "Товар не найден"))

#Задание 8
numbers = [4, 7, 1, 9, 7, 3, 1]
seen = set()

for num in numbers:
    if num in seen:
        print(num)
        break
    seen.add(num)

#Задание 9
text = "python is great and python is easy"
words = text.lower().split()

word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

most_common = max(word_count, key=word_count.get)

print(most_common)

#Задание 10
size = 5
hash_table = [[] for _ in range(size)]

def hash_function(key):
    return key % size

def insert(key):
    index = hash_function(key)
    hash_table[index].append(key)

numbers = [10, 15, 20, 7, 12, 17]

for num in numbers:
    insert(num)

print("Содержимое хеш-таблицы:")
for i, bucket in enumerate(hash_table):
    print(f"{i}: {bucket}")

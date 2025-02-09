# Task1

print("Task1")

with open("input.txt", "w") as file:
    file.write(" ".join(str(number) for number in range(1, 11)))

# Task2
print("\nTask2")

with open("input.txt", "r") as file:
    list_numbers = list(map(int, file.read().split()))

abc = 1
for number in list_numbers:
    abc *= number

with open("output.txt", "w") as file:
    file.write(str(abc))

# Task3
print("\nTask3")

from datetime import datetime, timedelta

products = [
    ("Table", 100, 450, "10.9.2024"),
    ("Board", 1000, 2590, "28.12.2024"),
    ("Chair", 800, 2500, "12.1.2025")
]

current_date = datetime.now()

for product in products:
    name, count, price, start_date = product

    if (current_date - datetime.strptime(start_date, "%d.%m.%Y") > timedelta(days=30)) and (price * count > 1000000):
        print(name)

# Task4
print("\nTask4")

with open('questions.txt', 'r', encoding='utf-8') as file:
    questions = [question.strip() for question in file.readlines()]

with open('answers.txt', 'r', encoding='utf-8') as file:
    answers = [answer.strip() for answer in file.readlines()]

score = 0

for index in range(len(questions)):
    print(questions[index])
    answer = input("Ответ: ")

    if answer.strip().lower() == answers[index].strip().lower():
        score += 1

print(f"Количество верных ответов: {score}/{len(questions)}")

# Task5
print("\nTask5")

import random
import json

dict_numbers = {}

for _ in range(1, random.randint(5, 6) + 1):
    key = random.randint(10000, 99999)
    name = random.choice(['Oleg', 'Dima', 'Alice', 'Alena', 'Darya', 'Kirill', 'Bob', 'Den'])
    age = random.randint(18, 30)
    dict_numbers[key] = (name, age)

with open("data.json", "w") as json_file:
    json.dump(dict_numbers, json_file, indent=4)

# Task6
print("\nTask6")

import csv

with open('data.json', 'r') as json_file:
    dict_numbers = json.load(json_file)

with open('data.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=';')

    csv_writer.writerow(['Key', 'Name', 'Age'])

    for key, (name, age) in dict_numbers.items():
        csv_writer.writerow([f'Person {key}', name, age])

# Task7
print("\nTask7")

with open("7.txt", "r") as file:
    words = [word.strip() for word in file.read().split()]

dict_text = {}
for word in words:
    if word in dict_text:
        dict_text[word] += 1
    else:
        dict_text[word] = 1

max_frequency = max(dict_text.values())
most_frequent_words = [word for word, count in dict_text.items() if count == max_frequency]
result_word = min(most_frequent_words)
print(result_word, max_frequency)

# Task8
print("\nTask8")

with open("8.txt", "r") as file:
    str_text = file.read().strip()
    print(str_text)
    new_str = ""
    index = 0

    while index != len(str_text):
        char = str_text[index]
        index += 1
        count_str = ""

        while index != len(str_text) and str_text[index].isdigit():
            count_str += str_text[index]
            index += 1

        count = int(count_str)
        new_str += char * count

print(new_str)

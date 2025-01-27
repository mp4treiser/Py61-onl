# 1
print("Task1")
number = 101
counter = 1
simple_number = 0
while number > simple_number:
    simple_number += counter
    counter += 2
    if number > simple_number:
        print(simple_number, end=" ")

# 2
print("\n\nTask2")
number = 9321
while True:
    if number // 10 == 0:
        print(number)
        break
    number //= 10

# 3
print("\nTask3")
number = 53485834150348534
min_digit = 9
while number > 0:
    digit = number % 10
    if digit < min_digit:
        min_digit = digit
    number //= 10
print(min_digit)

# 4
print("\nTask4")
input_str = "The quick brown fox jumps over the lazy dog"
print(input_str[2])
print(input_str[-2])
print(input_str[:5])
print(input_str[:-2])
print(input_str[::2])
print(input_str[1::2])
print(input_str[::-1])
print(input_str[::-2])
print(len(input_str))

# 5
print("\nTask5")
input_str = "Hello World!"
temp = input_str.split(" ")
print(temp[1], temp[0])

# 6
print("\nTask6")
input_str = "1331"
if input_str[:len(input_str) // 2] == input_str[:len(input_str) // 2 - 1:-1]:
    print("Палиндром")
else:
    print("Не палиндром")

# 7
print("\nTask7")
input_str = "Thef quick brown ffox jumps over the lazy dog"
count = input_str.count("f")
if count > 1:
    print(input_str.index("f"), count)
elif count == 1:
    print(count)

# 8
print("\nTask8")
list1 = [5, 12, 3, -1, 8, 6, 0, 1]
list2 = [1, 3, 4, 8, 3, 0, 6]
unique_elements = [element for element in list1 if element not in list2]
if unique_elements:
    min_element = min(unique_elements)
    print(min_element)
else:
    print("Нет уникальных элементов")

# 9
print("\nTask9")
list = [1, 5, 6, 3, 1, 0, 3]
length_list = len(list)
counter = 0
for index in range(length_list - 1):
    if list[index] > list[index + 1]:
        counter += 1
print(counter)

# 10
print("\nTask10")
input_str = input("Введите строку: \n")
result_str = []
for letter in input_str:
    if letter not in result_str:
        result_str.append(letter)
print("".join(result_str))

# 11
print("\nTask11")
text = "Яркие моменты жизни дорев22221олюционного Петербурга3333. Кафешантан Вилла Родэ. Antenna Daily (30 июня 2019). Дата обращения: 2 ноября 202499"
list_numbers = []
number = ""
for letter in text:
    if letter.isdigit():
        number += letter
    else:
        if number:
            list_numbers.append(int(number))
            number = ""
if number != "":
    list_numbers.append(int(number))
if list_numbers:
    print(max(list_numbers))
# как по мне, это более красиво, но вроде регулярные пока не изучали ещё
# import re
# list_numbers = re.findall(r'\d+', text)
# if list_numbers:
#     print(max(map(int, list_numbers)))

# 12
print("\nTask12")
input_str = input("Введите строку:\n")
result_str = ""
for letter in input_str:
    if result_str.find(letter) == -1:
        result_str += letter
print(result_str)

# 13
print("\nTask13")
numbers = [18, 42, 8, 122]
new_numbers = [f"{number} {str(number)[::-1]}" for number in numbers]
print(", ".join(new_numbers))

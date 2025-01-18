# 1
number = 13
result = str(number)[-1] == "3"
# or
#result = number % 10 == 3
# либо через if расписывать
print(f"Task #1\n"
      f"{result}\n")

# 2
print("Task #2")
number_1, number_2, number_3 = map(float, input("Введите 3 числа с клавиатуры через пробел: ").split())
if number_1 < 0 or number_2 < 0 or number_3 < 0:
    print(True)
else:
    print(False)

# 3
print("Task #3")
number_1 = 5
number_2 = 37
if number_1 % 2 == number_2 % 2:
    print(True)
else:
    print(False)

# 4
print("\nTask #4")
side_a = 6
side_b = 3
side_c = 5
if side_a == side_b == side_c: print("equilateral")
elif side_a == side_b or side_a == side_c or side_b == side_c: print("isosceles")
elif side_a != side_b and side_a != side_c and side_b != side_c: print("scalene")

# 5
print("\nTask #5")
number_1 = 1
number_2 = 3
number_3 = 5
count = 0
if number_1 % 2 == 0: count += 1
if number_2 % 2 == 0: count += 1
if number_3 % 2 == 0: count += 1
print(f"{count}\n")

# 6
print("\nTask #6")
number = 29
print(number // 10)
print(number % 10)
if number // 10 + number % 10 >= 10:
    print(True)
else:
    print(False)
# or
# print(number // 10 + number % 10 >= 10)

# 7
print("\nTask #7")
number = 3333
if number // 1000 == number // 100 % 10 == number // 10 % 10 == number % 10:
    print(True)
else:
    print(False)

# 8
print("\nTask #8")
year = 2025
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Високосный")
else:
    print("Не високосный")

# 9
print("\nTask #9")
for index in range(20): print("10")

# 10
print("\nTask #10")
start = 1
stop = 5
step = 1
if start > stop: step = -1
for index in range(start, stop, step): print(index)

# 11
print("\nTask #11")
for index in range(-100, 101): print(index, end=" ")

# 12
print("\n\nTask #12")
print(sum(range(100, 501)))
# or
# sum = 0
# for number in range(100, 501):
#     sum += number
# print(sum)

# 13
print("\nTask #13")
sum = 1
for number in range(100, 501):
    sum *= number
print(sum)

# 14
print("\nTask #14")
number = 5
factorial = 1
for index in range(1, number + 1):
    factorial *= index
print(factorial)

# 15
print("\nTask #15")
while True:
    number = int(input("Введите натуральное число <= 1000: "))
    if 1 <= number <= 1000:
        break
    else:
        print("Число не натуральное либо больше 1000")

for index in range(1, number + 1):
    last = index % 10
    if 11 <= index <= 19: print(f"На лугу {index} коров")
    elif last == 1: print(f"На лугу {index} корова")
    elif last in (2, 3, 4): print(f"На лугу {index} коровы")
    else: print(f"На лугу {index} коров")

# 16
print("\nTask #16")
number = 8
temp_1, temp_2 = 1, 1
print(1, end=" ")
for index in range(1, number):
    temp_1, temp_2 = temp_2, temp_1 + temp_2
    print(temp_1, end=" ")

# 17
print("\n\nTask #17")
x1 = 5
y1 = 5
x2 = 1
y2 = 6
if (x1 + y1) % 2 == (x2 + y2) % 2:
    print("Поля одного цвета")
else:
    print("Поля разного цвета")

if (x1 == x2) or (y1 == y2) or (abs(x1 - x2) == abs(y1 - y2)):
    print("Угрожает")
else:
    print("Не угрожает")

if (abs(x1 - x2) == abs(y1 - y2)): print("Слон бьёт коня")
elif (abs(x2 - x1) == 1 and abs(y2 - y1) == 2) or (abs(x2 - x1) == 2 and abs(y2 - y1) == 1): print("Конь бьёт слона")
else: print("Фигуры друг другу не угрожают")

# Вывод print реализован по разному специально
# 1
print("Task #1",
      17 / 2 * 3 + 2, 2 + 17 / 2 * 3, 19 % 4 + 15 / 2 * 3, 15 + 6 - 10 * 4, f"{17 / 2 % 2 * 3 ** 3}\n",
      sep="\n")

# 2
print("Task #2",
      17 / 2 * (3 + 2), (2 + 17) / 2 * 3, 19 % (4 + 15) / (2 * 3), (15 + 6 - 10) * 4, f"{(17 / 2) % (2 * 3 ** 3)}\n",
      sep="\n")

# 3
print("Task #3\n"
      f"У Анны осталось {11 - 1.5 * 3} рублей.\n")

# 4
apple_Anna = 2
apple_Pol = 5
print("Task #4\n"
      f"У Анны {apple_Anna} яблок, у Пола {apple_Pol} яблок.\n")

# 5
days = 5
print("Task #5\n"
      f"{days} суток = {days * 24} часов = {days * 24 * 60} минут = {days * 24 * 60 * 60} секунд\n")

# 6
print("Task #6\n"
      f"{182 // 7} полных недель прошло\n")

# 7
side_1 = 150
side_2 = 65
print("Task #7\n"
      f"{150 // 30 * 65 // 30} квадратов\n")

# 8
seconds = 4000
print("Task #8\n"
      f"{seconds // 3600} час\n"
      f"{(seconds % 3600) // 60} минут\n"
      f"{seconds % 60} секунд\n")

# 9
cash = 361
print("Task #9\n"
      f"{cash // 100} купюры по 100 рублей\n"
      f"{(cash % 100) // 50} купюры по 50 рублей\n"
      f"{(cash % 50) // 10} купюры по 10 рублей\n"
      f"{cash % 10} купюры по 1 рублю\n")

# 10
height = 10
up = 10
down = 7
print("Task #10\n"
      f"Улитка доползёт до вершины шеста за {(height - up - 1) // (up - down) + 2} дней\n")

# 11
speed = 133
hours = 2
minutes = 30

print("Task #11\n"
      f"Байкер остановится на {(speed * (hours + minutes / 60)) % 56} км МКАД")

# 1 / 2
print("Task1 / Task2")


def minimum(number_1: int | float, number_2: int | float) -> int | float:
    if number_1 < number_2:
        return number_1
    else:
        return number_2


number_1, number_2, number_3, number_4 = -3.99, -1, 1, -7.1
print(minimum(minimum(number_1, number_2), minimum(number_3, number_4)))

# 3
print("\nTask3")


def distance(x1: int | float, y1: int | float, x2: int | float, y2: int | float) -> int | float:
    dx = x2 - x1
    dy = y2 - y1
    result = (dx ** 2 + dy ** 2) ** 0.5
    return result


x1, y1, x2, y2 = -0.5, 3.1, 2, 3
print(distance(x1, y1, x2, y2))

# 4
print("\nTask4")


def simple_number(number: int) -> str:
    for index in range(2, int(number ** 0.5) + 1):
        if number % index == 0:
            return "NO"
        return "YES"


number = 500
print(simple_number(number))

# 5
print("\nTask5")


def fibonacci(number: int):
    temp_1, temp_2 = 1, 1
    print(1, end=" ")
    for index in range(1, number):
        temp_1, temp_2 = temp_2, temp_1 + temp_2
        print(temp_1, end=" ")


number = 7
fibonacci(number)

# 6
print("\n\nTask6")


def closest_mod_5(number: int) -> int:
    result = number + (5 - number % 5) % 5
    return result


number = 27
print(closest_mod_5(number))

# 7
print("\nTask7")


def modify_list(number_list: list):
    for index in range(len(number_list) - 1, -1, -1):
        if number_list[index] % 2 == 0:
            number_list[index] //= 2
        else:
            number_list.pop(index)


number_list = [1, 2, 3, 4, 5]
modify_list(number_list)
print(number_list)

# 8
print("\nTask8")


def check_variable(variable: str) -> str:
    letters_blocked = "! @ # $ % ^ & * ( )".split(" ")
    letters_blocked.append(" ")
    if variable == "":
        return "Нельзя использовать"
    elif variable[0].isdigit():
        return "Нельзя использовать"
    else:
        for letter in variable:
            for letter_block in letters_blocked:
                if letter.__contains__(letter_block):
                    return "Нельзя использовать"
    return "Можнр использовать"


while True:
    variable = input("Введите имя переменной (или 'Поработали, и хватит' для выхода): ")
    if variable == "Поработали, и хватит":
        break
    print(check_variable(variable))

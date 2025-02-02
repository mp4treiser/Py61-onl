# 1
print("Task1")
list_numbers = [number for number in range(10, 100) if number % 2 == 1]
print(" ".join(map(str, list_numbers)))

# 2
print("\nTask2")
list_numbers = [number ** 2 for number in range(1, 11)]
print(" ".join(map(str, list_numbers)))

# 3
print("\nTask3")
list_numbers = [number for number in range(100, 1000) if number % 3 == 0 and number % 5 == 0]
print(" ".join(map(str, list_numbers)))

# 4
print("\nTask4")
range_1, range_2, degree = map(int, input().split())
list_numbers = [number ** degree for number in range(range_1, range_2 + 1)]
print(" ".join(map(str, list_numbers)))

# 5
print("\nTask5")
list_numbers = list(filter(lambda digit: '0' in digit, input().split()))
print(" ".join(list_numbers))

# 6
print("\nTask6")
list_words = ["apple", "Hello", "World", "saaamsung", "avada", "kedavra"]
list_filtered = list(filter(lambda word: word.count('a') > 2, list_words))
print(" ".join(list_filtered))

# 7
print("\nTask7")
list_words = ["apple", "Hello", "World", "saaamsung", "avada", "kedavra"]
list_upper = [word.upper() for word in list_words]
print(" ".join(list_upper))

# 8
print("\nTask8")
list_words = ["apple22", "Hel32lo", "Wo1rld", "saaam3sung", "avada", "kedavra"]
list_filtered = list(map(lambda word: "".join(filter(lambda letter: not letter.isdigit(), word)), list_words))
print(" ".join(list_filtered))

# 9
print("\nTask9")
list_numbers = input().split()
list_filtered = list(filter(lambda digit: list_numbers.count(digit) > 1, set(list_numbers)))
print(*list_filtered)

# 10
print("\nTask10")


def is_simple(number: int) -> bool:
    for _ in range(2, int(number ** 0.5) + 1):
        if number % _ == 0:
            return False
    return True


list_numbers = [number for number in range(2, 101) if is_simple(number)]
print(*list_numbers)

# 11
print("\nTask11")
list_numbers = ["7", "4", "1", "3", "5"]
for index in range(len(list_numbers) - 1, 0, -1):
    list_numbers.insert(index, "0")
print(*list_numbers)

# 12
# Не осилил из-за нехватки времени

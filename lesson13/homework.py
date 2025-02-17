# Task1
print("Task1")


class RangeSquared:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __iter__(self) -> "RangeSquared":
        self.current = self.start
        return self

    def __next__(self) -> int:
        if self.current >= self.end:
            raise StopIteration
        result = self.current ** 2
        self.current += 1
        return result


for number in RangeSquared(1, 5):
    print(number)

# Task2
print("\nTask2")


def factorial_gen(number: int):
    current_factorial = 1
    for i in range(number + 1):
        if i == 0:
            yield current_factorial
        else:
            current_factorial *= i
            yield current_factorial


for fact in factorial_gen(5):
    print(fact)

# Task3
print("\nTask3")


def read_file_lines(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()


for line in read_file_lines('example.txt'):
    print(line)

# Task4
print("\nTask4")


def calculate_complex_formula(a: float, b: float, c: float, d: float, e: float, f: float, g: float, h: float) -> float:
    return (b * c if a > 0 else -d / e) + (f * (g + h) if g < h else -(d - f) / g)


result = calculate_complex_formula(1, 2, 3, 4, 5, 6, 7, 8)
print(result)

# Task5
print("\nTask5")


class User:
    adult_age = 18

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self) -> str:
        if self.age >= self.adult_age:
            return f"Привет, {self.name}! Добро пожаловать на сайт для взрослых."
        else:
            return f"Привет, {self.name}! Добро пожаловать на детский сайт."


user1 = User("Дима", 25)
print(user1.greet())

user2 = User("Даша", 16)
print(user2.greet())

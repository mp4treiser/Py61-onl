# 1
print("Task1")
list_words = ["Mary", "Dimitrius", "Elizabeth", "Richard", "Anna", "Holland", "MJ"]
list_words.sort(key=len, reverse=True)
print(*list_words)

# 2
print("\nTask2")
list_words = ["attract", "active", "albania", "asparagas", "accelerated", "Holland", "MJ"]
list_words.sort(key=lambda word: word.count("a"), reverse=True)
print(*list_words)

# 3
print("\nTask3")
school = {
    "9а": 22,
    "9б": 23,
    "9в": 21,
    "9г": 24,
    "9д": 27,
    "9е": 20
}
school['9в'] = 25
school['9ё'] = 29
del school['9е']

print(school)
print(sum(school.values()))

# 4
print("\nTask4")
contacts = {}
while True:
    contact = input()
    if contact == ".":
        break

    parts = contact.split()

    if len(parts) == 2:
        contacts[parts[0]] = parts[1]
    elif len(parts) == 1 and parts[0] in contacts:
        print(contacts[contact])
    else:
        print("Не найдено")

# 5
print("\nTask5")


def get_element(lst: list, index: int) -> any:
    try:
        return lst[index]
    except IndexError:
        return "IndexError Ошибка: индекс вне диапазона"


lst = [1, 2, 3, 4, 5]
print(get_element(lst=lst, index=6))

# 6
print("\nTask6")


def retry_on_exception(retries: int) -> callable:
    def decorator(func):
        def wrapper(*args, **kwargs):
            for retry in range(retries):
                try:
                    return func(*args, **kwargs)
                except ValueError:
                    print(f"Попытка {retry + 1} из {retries}")
                    if retry == retries - 1:
                        raise

        return wrapper

    return decorator


@retry_on_exception(retries=3)
def simple_func(value: float) -> float:
    if not isinstance(value, float):
        raise ValueError("Число не float")
    return value


try:
    print(simple_func(1))
except ValueError as error:
    print(f"Ошибка: {error}")

# Тут успешное выполнение
print(simple_func(5.2))

# 7
print("\nTask7")

import time


def timeout(limit_time: int | float) -> callable:
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time() - start_time
            if end_time > limit_time:
                raise TimeoutError(f"Функция превысила время выполнения {limit_time} секунд")
            return result

        return wrapper

    return decorator


@timeout(limit_time=2)
def time_function(seconds: int):
    print("Что-то долго делаем")
    time.sleep(seconds)


try:
    time_function(seconds=3)
except TimeoutError as error:
    print(f"Ошибка: {error}")

# Тут успешное выполнение
time_function(seconds=1)

# 8
print("\nTask8")
input_str = input()
list_words = input_str.lower().split()

words = {}

for word in list_words:
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

for word, count in words.items():
    print(f"{word} {count}")

# 9
print("\nTask9")
def cache_results(func: callable) -> callable:
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@cache_results
def simple_func(number) -> int | float:
    return number + 1

result1 = simple_func(2)
result2 = simple_func(2)
result3 = simple_func(10)

print(f"1: {result1} ID: {id(result1)}")
print(f"2: {result2} ID: {id(result2)}")
print(f"3: {result3} ID: {id(result3)}")
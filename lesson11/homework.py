# Task1
import json

print("Task1")


class Calculator:
    def __init__(self):
        self.number_1 = 0.0
        self.number_2 = 0.0

    def set_number_1(self, number_1: float):
        self.number_1 = number_1

    def set_number_2(self, number_2: float):
        self.number_2 = number_2

    def sum(self) -> float:
        return self.number_1 + self.number_2

    def max(self) -> float:
        return max(self.number_1, self.number_2)

    def print(self) -> callable:
        return print(f"number_1: {self.number_1} | number_2: {self.number_2}")


calc = Calculator()

calc.set_number_1(2)
calc.set_number_2(3.33)
print(calc.max())
print(calc.sum())
calc.print()

# Task2
print("\nTask2")


class Counter:
    def __init__(self, min_value=0, max_value=10, current_value=0):
        self.min_value = min_value
        self.max_value = max_value
        self.current_value = current_value

    def value(self):
        return self.current_value

    def increment(self):
        if self.current_value < self.max_value:
            self.current_value += 1
        else:
            print("Достигнуто максимальное значение.")

    def decrement(self):
        if self.current_value > self.min_value:
            self.current_value -= 1
        else:
            print("Достигнуто минимальное значение.")


counter = Counter()
print(f"Начальное значение: {counter.value()}")
counter.increment()
counter.increment()
print(f"Значение после двух инкрементов: {counter.value()}")
counter.decrement()
counter.decrement()
counter.decrement()
counter.decrement()
print(f"Значение после декрементов: {counter.value()}")

custom_counter = Counter(min_value=0, max_value=10, current_value=9)
print(f"Значение кастомного счётчика: {custom_counter.value()}")
custom_counter.increment()
custom_counter.increment()
custom_counter.increment()
print(f"Значение кастомного счётчика после инкрементов: {custom_counter.value()}")
custom_counter.decrement()
print(f"Значение кастомного счётчика после декремента: {custom_counter.value()}")

# Task3
print("\nTask3")


class Shop:
    def __init__(self):
        self.products = {}

    def add_products_from_json(self, products: json):
        for name, details in products["products"].items():
            price = details["price"]
            count = details["count"]
            self.products[name] = {"price": price, "count": count}

    def add_product(self, name: str, price: float, count: float):
        self.products[name] = {"price": price, "count": count}

    def search_product(self, name: str) -> dict | str:
        try:
            return self.products[name]
        except:
            return f"Продукт {name} не существует"

    def remove_product(self, name: str) -> str:
        try:
            del self.products[name]
            return f"Продукт {name} удалён"
        except:
            return f"Продукт {name} не существует"

    def list_products(self) -> dict:
        return self.products


WBBobrov = Shop()
WBBobrov.add_product("Ананас", 10.5, 25)

json_data = {
    "products": {
        "Яблоко": {
            "price": 5,
            "count": 50
        },
        "Груша": {
            "price": 8,
            "count": 30
        },
        "Абрикос": {
            "price": 11,
            "count": 77
        },
        "Виноград": {
            "price": 9,
            "count": 10
        }
    }
}

WBBobrov.add_products_from_json(json_data)
print(WBBobrov.list_products())

json_data = {
    "products": {
        "Перец": {
            "price": 15,
            "count": 50
        },
        "Огурец": {
            "price": 9,
            "count": 35
        },
        "Помидор": {
            "price": 14,
            "count": 11
        },
        "Морковь мытая": {
            "price": 1.5,
            "count": 1000
        }
    }
}

WBBobrov.add_products_from_json(json_data)
print(WBBobrov.list_products())
print(WBBobrov.remove_product(name="Помидор"))
print(WBBobrov.list_products())
print(WBBobrov.search_product(name="Чай"))

# Task4
print("\nTask4")


class MoneyBox:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current_capacity = 0

    def can_add(self, v: int) -> bool:
        if self.current_capacity + v <= self.capacity:
            return True
        else:
            return False

    def add(self, v: int) -> str:
        if self.can_add(v):
            self.current_capacity += v
            return f"Добавлено {v} монет"
        else:
            return f"Превышена вместимость копилки = {self.capacity}, невозможно добавить {v} монет, т.к. на текущий момент в копилке {self.current_capacity} монет"


travel_box = MoneyBox(capacity=10)
print(travel_box.can_add(15))
print(travel_box.can_add(5))
print(travel_box.add(8))
print(travel_box.add(10))
print(travel_box.current_capacity)

# Task5
print("\nTask5")


class Fraction:
    def __init__(self, numerator: int, denominator: int):
        nod = self.gcd(numerator, denominator)

        self.numerator = numerator // nod
        self.denominator = denominator // nod

    def __str__(self) -> str:
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, second: "Fraction") -> "Fraction":
        new_numerator = (self.numerator * second.denominator) + (second.numerator * self.denominator)
        new_denominator = self.denominator * second.denominator
        return Fraction(new_numerator, new_denominator).reduce()

    def gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    def reduce(self) -> "Fraction":
        nod = self.gcd(self.numerator, self.denominator)
        return Fraction(self.numerator // nod, self.denominator // nod)


fraction1 = Fraction(5, 10)
print(fraction1)
fraction2 = Fraction(3, 4)
print(fraction2)
print(fraction1 + fraction2)

# Task6
print("\nTask6")


class Facultet:
    def __init__(self, name: str):
        self.name = name
        self.abiturients = []

    def __str__(self):
        return self.name

    def enrollment_abiturient(self, abiturient: "Abiturient") -> str:
        if abiturient.average_score() >= 7.21:
            self.abiturients.append(abiturient)
            return f"Абитуриент {abiturient} был зачислен на факультет {self.name}"
        else:
            return f"Абитуриент {abiturient} не был зачислен на факультет {self.name}, т.к. не прошёл по среднему баллу"


class Abiturient:
    def __init__(self, name: str):
        self.name = name
        self.exams = []

    def __str__(self):
        return self.name

    def register_exam(self, exam: "Exam"):
        self.exams.append(exam)

    def set_exam_score(self, exam: "Exam", score):
        if exam in self.exams:
            self.exams[exam].set_score(self, score)

    def average_score(self) -> float:
        total_score = sum(exam.scores[self.name] for exam in self.exams)
        count_exams = len(self.exams)
        return round(total_score / count_exams, 2)


class Exam:
    def __init__(self, name: str):
        self.name = name
        self.scores = {}

    def __str__(self):
        return self.name

    def set_score(self, abiturient: "Abiturient", score: int):
        self.scores[abiturient.name] = score
        abiturient.set_exam_score(self.name, score)


class Teacher:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

    def estimate(self, exam: Exam, abiturient: Abiturient, score: int):
        exam.set_score(abiturient, score)


facultet = Facultet("Финансы")
print(f"Создан факультет {facultet}\n")

abiturent_1 = Abiturient("Иванов Иван Иванович")
abiturent_2 = Abiturient("Петров Петр Петрович")
abiturent_3 = Abiturient("Андреев Андрей Андреевич")
print(f"Созданы абитуриенты:\n"
      f"{abiturent_1}\n"
      f"{abiturent_2}\n"
      f"{abiturent_3}")

exam_1 = Exam("Экономическая теория")
exam_2 = Exam("Макроэкономика")
exam_3 = Exam("Микроэкономика")
print(f"\nСозданы экзамены:\n"
      f"{exam_1}\n"
      f"{exam_2}\n"
      f"{exam_3}")

abiturent_1.register_exam(exam_1)
abiturent_1.register_exam(exam_2)
abiturent_2.register_exam(exam_1)
abiturent_2.register_exam(exam_3)
abiturent_3.register_exam(exam_1)
abiturent_3.register_exam(exam_2)
abiturent_3.register_exam(exam_3)
print("Абитуриенты зарегистрированы на экзамены\n")

teacher_1 = Teacher("Преподаватель экономической теории")
teacher_2 = Teacher("Преподаватель макроэкономики")
teacher_3 = Teacher("Преподаватель микроэкономики")

teacher_1.estimate(exam_1, abiturent_1, 8)
teacher_1.estimate(exam_1, abiturent_2, 4)
teacher_1.estimate(exam_1, abiturent_3, 9)
teacher_2.estimate(exam_2, abiturent_1, 6)
teacher_2.estimate(exam_2, abiturent_3, 5)
teacher_3.estimate(exam_3, abiturent_2, 3)
teacher_3.estimate(exam_3, abiturent_3, 9)

print(facultet.enrollment_abiturient(abiturent_1))
print(facultet.enrollment_abiturient(abiturent_2))
print(facultet.enrollment_abiturient(abiturent_3))

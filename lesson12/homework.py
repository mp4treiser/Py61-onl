# Task1
import time

print("Task1")


class BankAccount:
    def __init__(self, balance: float = 0):
        self.__balance = balance
        self.daily_limit = 5000
        self.withdrawals_today = 0
        self.max_withdrawals = 3

    def deposit(self, amount: float) -> str:
        if amount > 0:
            self.__balance += amount
            return f"Успешно пополнено на сумму {amount}. Баланс: {self.__balance}"
        else:
            return "Сумма должна быть положительной"

    def withdraw(self, amount: float) -> str:
        if amount > self.__balance:
            return "Недостаточно средств на счёте"
        elif amount > self.daily_limit:
            return "Превышен суточный лимит снятия"
        elif self.withdrawals_today >= self.max_withdrawals:
            return "Превышено количество снятий в сутки"
        else:
            self.__balance -= amount
            self.withdrawals_today += 1
            return f"Успешно снято на сумму {amount}. Баланс: {self.__balance}"

    def get_balance(self) -> float:
        return self.__balance


# Task2
print("\nTask2")
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.hunger = 100  # 100 - сыт, 0 - голоден

    @abstractmethod
    def make_sound(self):
        pass

    def eat(self):
        self.hunger = 100
        print(f"{self.name} поел и теперь сыт.")

    def hungry(self):
        while True:
            self.hunger -= 10
            time.sleep(10)


class Lion(Animal):
    def make_sound(self):
        print(f"{self.name} рычит: Рррр-рр!")

    def hunt(self):
        print(f"{self.name} охотится.")


class Elephant(Animal):
    def make_sound(self):
        print(f"{self.name} трубит: Ту-ту-тууу!")

    def trumpet(self):
        print(f"{self.name} издает звук трубы.")


class Penguin(Animal):
    def make_sound(self):
        print(f"{self.name} издает звук: Квик-квик!")

    def swim(self):
        print(f"{self.name} бульк.")


animals = [Lion(name="Симба", age=5), Elephant(name="Дамбо", age=10), Penguin(name="Пенгу", age=3)]
for animal in animals:
    animal.make_sound()

# Task3
print("\nTask3")


class Temperature:
    def __init__(self, celsius: float):
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        if value < -273.15:
            raise ValueError("Температура не может быть ниже -273.15°C")
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        return (self._celsius * 9 / 5) + 32

    @property
    def kelvin(self) -> float:
        return self._celsius + 273.15


temp = Temperature(celsius=25)
print(f"Температура в Цельсиях: {temp.celsius}")
print(f"Температура в Фаренгейтах: {temp.fahrenheit}")
print(f"Температура в Кельвинах: {temp.kelvin}")

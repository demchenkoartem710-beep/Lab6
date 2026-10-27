# 1. Імперативна парадигма
def imperative_example():
    numbers = [10, 20, 30, 40, 50]
    total = 0

    for number in numbers:
        total += number

    print("=== Імперативне програмування ===")
    print("Список:", numbers)
    print("Сума елементів:", total)


# 2. Об'єктно-орієнтована парадигма
class Car:
    def __init__(self, model):
        self.model = model
        self.running = False

    def start(self):
        self.running = True
        print(f"{self.model} запущено.")

    def stop(self):
        self.running = False
        print(f"{self.model} зупинено.")


def oop_example():
    car = Car("Tesla Model S")

    print("\n=== Об'єктно-орієнтоване програмування ===")
    car.start()
    print("Стан автомобіля:", car.running)

    car.stop()
    print("Стан автомобіля:", car.running)


# 3. Функціональна парадигма
def functional_example():
    numbers = [2, 4, 6, 8, 10]
    squares = list(map(lambda x: x ** 2, numbers))

    print("\n=== Функціональне програмування ===")
    print("Початковий список:", numbers)
    print("Квадрати елементів:", squares)


# Запуск усіх прикладів
if __name__ == "__main__":
    imperative_example()
    oop_example()
    functional_example()
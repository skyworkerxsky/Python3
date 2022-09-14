"""Класс для представления автомобиля."""

class Car():
    """Простая модель автомобиля."""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometr(self):
        """Выводит пробег машины в милях."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometr(self, millies):
        if millies >= self.odometer_reading:
            self.odometer_reading = millies
        else:
            print("You cant roll back odometr")

    def increment_odometer(self, miles):
        """Увеличивает показания одометра с заданным приращением."""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("fill gas tank")


my_new_car = Car('audi', 'a4', 2019)
my_new_car.update_odometr(1)
my_new_car.fill_gas_tank()
print(my_new_car.get_descriptive_name())
from car import Car

class Dog():
    """Простая модель собаки."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        """Собака садится по команде."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Собака перекатывается по команде."""
        print(f"{self.name} rolled over!")


myDog = Dog('Billy', 8)
myDog.sit()
myDog.roll_over()

class Battery():
    """Простая модель аккумулятора электромобиля."""

    def __init__(self, battery_size = 75):
        """Инициализирует атрибуты аккумулятора."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Выводит приблизительный запас хода для аккумулятора."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

# Inheritance
class ElectricCar(Car):

    def __init__(self, make, model, year):
        """
        Инициализирует атрибуты класса-родителя.
        Затем инициализирует атрибуты, специфические для электромобиля.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print(f"This car has a {self.battery.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        print("override method")

my_tesla = ElectricCar('tesla', 'model s', 2019)
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
# Инициализация Экземпляра
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        # Добавление Приватного Атрибута
        self.__engine_type = 1.6

    # Для чтения приватного атрибута
    def get_engine_type(self):
        return self.__engine_type

    # Для изменения значения приватного атрибута
    def set_engine_type(self, value):
        self.__engine_type = value


# Создание экземпляра класса Car
my_car = Car("Lada", 2020)

# Использование атрибутов и методов объекта
print(my_car.brand)  # Вывод: Lada
print(my_car.year)  # Вывод: 2020
print(my_car.get_engine_type())  # Вывод: 1.6
my_car.set_engine_type(1.8)  # Изменения значения на 1.8
print(my_car.get_engine_type())  # Вывод: 1.8
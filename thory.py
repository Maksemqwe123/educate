# first_name = input("Введите ваше имя ")
# last_name = input("Введите вашу фамилию ")
#
# print(f"{first_name} \n {last_name}")

'''Ввод и вывод строки'''

 # nums = 123
# str_nums = str(nums)
#
# print(type(nums))
# print(type(str_nums))
# go = "тут что-то не так,не будь я д'Артаньян\" - подумал он."
# print(go)

# a= "тут что-то не так,не будь я д'Артаньян\" - подумал он."
# z = "пока"
# b = a[3:8]
#
# print(len(a))
# -
# string = 'Helloooo'
# print(string[::3])na
# name = input("Введите ваше имя ")
# age = int(input("Введите ваш возраст"))
# weight = int(input("Введите ваш вес"))
# print(f'Заика сказал:{name * 2}')
# print(f'Возрас в секундах:{age * 365 * 24 * 60 * 60} ')
# print(f'вес на луне:{weight // 6}')

# number = 0
# if number > 0:
#     print("число больше нуля")
#     if number % 2 == 0:
#         print("число чётное")
#     else:
#         print("число не чётное")
# elif number < 0:
#     print("число меньше нуля")
#     if number % 2 == 0:
#         print("число чётное")
#     else:
#         print("число не чётное")
# else:
#     print("число равно нулю")
# print("конец проги")

# health = 25
#
# if  health <= 0:
#     print("персанаж умер")
# else:
#     print("персонаж жив")
#"""ФУНКЦИИ"""

class Dog:

    def __init__(self, name):
        self.name = name

    def sit(self):
       """Собака садится по команде"""
       print(f'{self.name}сел')

    def run(self):
        print(f'{self.name}побежал')

    def get_info(self, age):
        print(f'Имя:{self.name}\nВозраст:{age}')


# my_pet = Dog('Bobik')
#   # my_pet.run()
#   # my_pet.sit()
# my_pet.get_info(2)
#
# my_pet_2 = Dog('Sharik')
# my_pet_2.run()
# my_pet_2.get_info(2)

# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.name = restaurant_name
#         self.cuisine = cuisine_type
#
#     def describe_restaurant(self,city=None):
#         if city:
#             print(f'Название ресторана: {self.name} в городе {city} ')
#         else:
#             print(f'Название ресторана: {self.name}')
#     def open_restaurant(self):
#         print(f'Ресторан {self.name} открыт')
#     def _cuisine_(self):
#         print(f'Блюдо:{self.cuisine}')
# info = Restaurant('KFC', 'Наггетсы')
# info.describe_restaurant()
# info.open_restaurant()
# info._cuisine_()


"""написать прогу с применением ООП для подсчета прямоугольника"""
class Rectangle:
    def __init__(self,width: int,height: int):
        self.width = width
        self.height = height

    def getArea(self):
        print(f'площадь прямоугольника: {self.width}*{self.height} = {self.width * self.height}')

    def drawRect(self):
        print('*'* self.width)
        self.width -= 1
        for i in range(1, self.height-1):
            self.width -= 1
            print("*", "" * self.width,"*")
        self.width +=2
        print("*" * self.width)





r1 = Rectangle(5,3)
r1.getArea()
r1.drawRect()
class Car:
    """модель авто и её описание"""

    def __init__(self, model, year, cash):
        self.module = model
        self.year = year
        self.cash = cash
        self.odometer = 0

    def description(self, odometer=None):
        if self.year >= 2021:
            print(f'модель: {self.module}, год выпуска: {self.year}, стоимость:{self.cash}, пробег:{self.odometer}')
        else:
            print(f'модель: {self.module}, год выпуска: {self.year}, стоимость:{self.cash}, пробег:{self.odometer}')


    def edit_odometer(self, km):
        self.odometer += km

class Battery:

    def __init__(self,battery = 75):
        self.battery = battery

    def describe_battery(self):
        print(f'Мощность акума: {self.battery} кВт')


class ElectricCar(Car):
    def __init__(self, model, year, cash):
        super().__init__(model, year, cash)
        self.battery = Battery()


my_electric_car = ElectricCar("Tesla", 2020, 40000)
my_electric_car.description(20000)
my_electric_car.battery.describe_battery()

# my_car = Car('BMW', 2021, 50000)
# my_car.edit_odometer(25000)
# my_car.description()


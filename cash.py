"""программа подсчет финансо"""
food = int(input ("Введите расходы на еду в рублях"))
internet = int(input("Введите расходы на интернет в рублях"))


# print(type(food))
# print(food)
# print(type(internet))
# print(internet)
# total_cash = food + internet
# print(total_cash)
total_cash = food + internet
print(f"общие расходы :{total_cash}")



"""Функции"""

users = []


# def get_username(username, data=None):
#     global users
#
#     if data:
#         users.append(f'{username.title()}, {str(data)}')
#     else:
#         users.append(username.title())
#     return users
#
#
# get_username('Максим')
# get_username(username='Артём')
#
# users_1 = get_username('Пётр', '01.12.2012')
# print(users_1)
#
# for name in users_1:
#     print(name)

# def sum_range(start, end):
#     if start > end:
#         numbers = list(range(end, start + 1))
#     else:
#         numbers = list(range(start, end + 1))
#
#     print(sum(numbers))
#
#
# sum_range(17, 15)

import time


def timer():
    def wrapper(func):
        start_time = time.time()
        print('начинаю обертывание')
        func()
        print('заканчиваю обертывание')
        end_time = time.time()
        print(f'Время выполнения функции: {end_time - start_time}')
    return wrapper


@timer()
def get_name():
    name = input('Введите ваше имя:')
    print(name)

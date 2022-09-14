# create func
def greet_user(name='Alex'):
    ''' Documentation '''
    print(f"hello {name}")


greet_user()


def getBool():
    return False


testBool = getBool()


def build_person(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix')
print(musician)


# print models
def print_models(unprinted_designs, completed_models):
    """
    Имитирует печать моделей, пока список не станет пустым.
    Каждая модель после печати перемещается в completed_models.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
print(unprinted_designs, completed_models)


# Произвольный набора аргументов
def make_pizza(*toppings):
    """Вывод списка заказанных топпингов."""
    print(f"topings - {toppings}")


make_pizza(1, 2, 3, 4, "qwe")


def build_profile(first, last, **user_info):
    """Строит словарь с информацией о пользователе."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert',
                             'einstein',
                             location='princeton',
                             field='physics')

print(user_profile)

# import module

import pizzaModule as p
from pizzaModule import make_pizza as mp
from pizzaModule import *

mp(12, 'pepperoni')
p.make_pizza(40, 'mushrooms', 'green peppers', 'extra cheese')
make_pizza(40, 'cheeps')

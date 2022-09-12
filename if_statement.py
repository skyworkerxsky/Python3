# if statement
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# and, or
age_0 = 22 
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
print(age_0 >= 21 or age_1 >= 21)

# Checking if values ​​are in a list
requested_toppings = ['mushrooms', 'onions', 'pineapple']
has_mushrooms = 'mushrooms' in requested_toppings
has_pepperoni = 'pepperoni' in requested_toppings

# Not
banned_users = ['andrew', 'carolina', 'david']
user = 'mariex'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# If Else
age = 17
if age >= 18:
    print(f"true age - {age}")
else:
    print(f"false age - {age}")

# if-elif-else
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

# if list
requested_toppings = []
if requested_toppings:
    print("true test")
else:
    print("test")
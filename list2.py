# Worked with list
magicians = ['alice', 'david', 'carolina']
for el in magicians:
    print(el)

# Worked with integer list
for value in range(1,5):
    print(value)

numbers = list(range(1,6))
print(numbers)

# Even_numbers
even_numbers = list(range(2,11,2))
print(even_numbers)

# Min, max, sum
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] 
minDigits = min(digits)
maxDigits = max(digits)
sumDigits = sum(digits)

# List Generators
squares = [value for value in range(1,11)]
print(squares)

# Slices
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

# Copy List
my_foods = ['pizza', 'falafel', 'carrot cake'] 
friend_foods = my_foods[:]

my_foods.append('orange')
friend_foods.append('cheese')

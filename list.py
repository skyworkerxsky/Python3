# Index
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
print(bicycles[-1].upper())

# Changed
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# Added
motorcycles.append('blablacar') 
motorcycles.insert(0, 'lada')
print(motorcycles)

# Removed
motorcycles.remove('yamaha')

# Delete
del motorcycles[0]
print(motorcycles)

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

# Sort
print("\n---- List ordering Example ----")
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

print("\nHere is the sorted list:") 
print(sorted(cars))

# Reverse 
movies = ['Армагедец', 'Месть', 'Мумия', 'Сказка']
movies.reverse()
print(movies)

# Length
print(len(movies))
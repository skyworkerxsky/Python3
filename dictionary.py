# alien
alien_0 = {
    'color': 'green',
    'points': 5
}

alien_0['x_position'] = 0
alien_0['y_position'] = 25

# create empty dict
shop = {}

# delete key-value
del alien_0['color']

# get value
val = alien_0.get('color')
if val:
    print("not empty val")
else:
    print("empty val")

# enumertion
for key, value in alien_0.items():
    print(f"{key} - {value}")

# set
testDict = {
    'color1': 'green',
    'color2': 'blue',
    'color3': 'green'
}
print(set(testDict.values()))

# create Set
testSet = {1,2,3,4,1,4,5,1}
print(testSet)

# nested dictionary
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# dict in dict
users = {
      'aeinstein': {
          'first': 'albert',
          'last': 'einstein',
          'location': 'princeton',
      },
      'mcurie': {
          'first': 'marie',
          'last': 'curie',
          'location': 'paris',
      },
}
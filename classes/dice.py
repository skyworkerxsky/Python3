from random import randint

class Die():

    def __init__(self):
        self.sides = 6

    def roll_die(self):
        print(randint(1, self.sides))

die = Die()
die.roll_die()
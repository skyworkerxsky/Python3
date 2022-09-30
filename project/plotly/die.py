from random import randint

class Die():

    def __init__(self, num_sides=6):
        """По умолчанию 6-ти гранный кубик"""
        self.num_sides = num_sides

    def roll(self):
        side = randint(1, self.num_sides)
        return side
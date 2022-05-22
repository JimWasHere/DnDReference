import random


class Dice:
    """Dice class accepts how many sides you would like the die to have ie, d20 = Dice(20)"""
    def __init__(self, die):
        self.dice = die

    def dice_roll(self, rolls=1):
        """Lets the user roll the dice n number of times and produces a list of all the rolls
            as well as the sum of the list as a tuple, if no amount of rolls is input, it rolls one die"""
        roll = True
        current_roll = []
        while roll:
            die = self.dice
            while len(current_roll) < rolls:
                x = random.randint(1, die)
                current_roll.append(x)

            roll = False

        return current_roll, sum(current_roll)


# d20 = Dice(20)
# d10 = Dice(10)
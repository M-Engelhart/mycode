#!/usr/bin/python3
"""RZFeeser | Alta3 Research
   Player - Class model
   Cheat_Swapper(Player) - Subclass model
   Cheat_Loaded_Dice(Player) - Subclass model"""

# standard library
from random import randint

class Player:
    def __init__(self):
        self.dice = []

    def roll(self):
        self.dice = [] # clears current dice
        for i in range(3):  # make 3 rolls
            self.dice.append(randint(1,6))   # 1 to 6 inclusive

    def get_dice(self): # returns the dice rolls
        return self.dice

# allows user to turn their last roll into a 6
class Cheat_Swapper(Player):  # inheritance of Player
    def cheat(self):
        self.dice[-1] = 6

# allows user to increase all rolls if they were less than a 6
class Cheat_Loaded_Dice(Player): # inheritance of Player
    def cheat(self):
        i = 0
        while i < len(self.dice):
            if self.dice[i] < 6:
                self.dice[i] += 1
            i += 1
# allows the user to re-roll if dice sum is less than 9
class Cheat_Mulligan(Player): #inheritance of Player
    def cheat(self):
        if sum(self.dice) <= 9:
            self.dice = []
            for i in range(3):
                self.dice.append(random.randint(1,6))
           
# rolls one additional die
class Cheat_Additional_Die(Player): # inheritance of Player
    def cheat(self):
        self.dice.append(randint(1,6))

# the first die is weighted so it can't roll below a 3
class Cheat_Weighted_Die(Player):
    def cheat(self):
        while self.dice[0] < 3:
            roll()

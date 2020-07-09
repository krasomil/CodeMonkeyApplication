import random

class Dice:
    """
    Dice class for rolling in the game
    Keyword arguments:
        sides -- the number of sides on the dice
    Raises: 
        Value Error - Sides must be > 1
    """
    def __init__(self, sides=6): 
        if(sides <= 1):  
            raise ValueError("Dice must have sides")
        self.sides = sides

    def roll(self):
        """
        Roll the dice

        Returns:
            A random number between 1 and the number of sides on the dice
        """
        return random.randint(1,self.sides)


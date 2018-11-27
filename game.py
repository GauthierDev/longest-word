# game.py
import random
import string

class Game:
    def __init__(self):
        self.list_lettre = string.ascii_uppercase
        self.grid = random.choices(self.list_lettre,k=9)

    def is_valid(self, word):
    if not word:
        return False
    letters = self.rid.copy()g # Consume letters from the grid
    for letter in word:
        if letter in letters:
            letters.remove(letter)
        else:
            return False
    return True



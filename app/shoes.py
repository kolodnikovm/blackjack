from .cards import Deck
import random

class Shoes:
    """ Collection of current decks """
    def __init__(self, decks):
        self.stock = {n: Deck() for n in range(decks)}

    def shuffleDeck(self):
        for d in self.stock:
            random.shuffle(self.stock[d].cards)

from .cards import Deck
from itertools import chain
from random import shuffle

class Shoes:
    """ Collection of current decks """
    def __init__(self, decks):
        self.stock = list(chain(*[Deck(n).cards for n in range(decks)]))

    def shuffleDeck(self):
        shuffle(self.stock)

    def getCard(self):
        return self.stock.pop()

# make GetCard give cards batch on demand

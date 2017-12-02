from .cards import Deck
from itertools import chain
from random import shuffle

class Shoes:
    """ Collection of current decks """
    def __init__(self, decks):
        self.stock = list(chain(*[Deck(n).cards for n in range(decks)]))
        self.shuffleDeck()

    def shuffleDeck(self):
        shuffle(self.stock)

    def getCard(self, n = 1):
        cards = []
        for i in range(n):
            cards.append(self.stock.pop())
        return cards

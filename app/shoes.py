from .cards import Deck
from itertools import chain
from random import shuffle

class Shoes:
    def __init__(self, decks, shfl = True):
        self.stock = list(chain(*[Deck(n).cards for n in range(decks)]))
        if shfl: self.shuffleDeck()
        
    def shuffleDeck(self):
        shuffle(self.stock)

    def getCard(self, n = 1):
        cards = []
        for i in range(n):
            cards.append(self.stock.pop())
        return cards

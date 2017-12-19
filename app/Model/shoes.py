from itertools import chain
from random import shuffle
from .cards import Deck

class Shoes:
    def __init__(self, decks, shfl = True):
        self.stock = list(chain(*[Deck(n).cards for n in range(decks)]))
        if shfl: self.shuffle_deck()

    def shuffle_deck(self):
        shuffle(self.stock)

    def get_card(self, n = 1):
        if n == 1:
            return self.stock.pop()
        else:
            cards = []
            for i in range(n):
                cards.append(self.stock.pop())
            return cards

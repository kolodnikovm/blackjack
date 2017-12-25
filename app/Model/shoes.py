""" Модуль раздатчика карт, где хранятся все колоды """

from itertools import chain
from random import shuffle
from .cards import Deck

class Shoes:
    """ Класс раздатчика карт, где хранятся все колоды """
    def __init__(self, decks, shfl=True):
        self.stock = list(chain(*[Deck(n).cards for n in range(decks)]))
        if shfl:
            self.shuffle_deck()

    def shuffle_deck(self):
        """ Перетасовать карты в stock """
        shuffle(self.stock)

    def get_card(self, n=1):
        """ Возращает карту из stock """
        if n == 1:
            return self.stock.pop()
        return [self.stock.pop() for c in range(n)]

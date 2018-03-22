from itertools import chain
from random import shuffle
from app.model.cards import Deck


class Shoes:
    def __init__(self, decks=1, shfl=True):
        self.stock = list(
            chain(*[Deck(number).cards for number in range(decks)]))
        if shfl:
            self.shuffle_deck()

    def shuffle_deck(self):
        shuffle(self.stock)

    def get_card(self, number=1):
        if self.stock:
            if number == 1:
                return self.stock.pop()
            return [self.stock.pop() for card_number in range(number)]
        return None

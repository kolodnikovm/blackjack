from itertools import chain
from random import shuffle
from app.model.cards import Deck


class Shoes:
    def __init__(self, decks, shfl=True):
        self.stock = list(
            chain(*[Deck(number).cards for number in range(decks)]))
        if shfl:
            self.shuffle_deck()

    def shuffle_deck(self):
        """ Перетасовать карты в stock """
        shuffle(self.stock)

    def get_card(self, number=1):
        """ Возращает карту из stock """
        if self.stock:
            if number == 1:
                return self.stock.pop()
            return [self.stock.pop() for card_number in range(number)]
        return None


if __name__ == '__main__':
    test_shoe = Shoes(2)
    print(test_shoe.get_card(), 'Ohne Zahl')
    print(test_shoe.get_card(3), 'Mit Zahl')

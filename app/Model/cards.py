""" Модуль карт и колоды карт """

SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
RANKS = {
    "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8,
    "9":9, "10":10, "J":10, "Q":10, "K":10, "A":11
    }

class Card:
    """ Класс игральной карты """
    def __init__(self, suit, rank, deck_number):
        self.suit = suit
        self.rank = rank
        self.deck_number = deck_number
        self.score = RANKS[rank]

    def __repr__(self):
        return self.suit+'_'+str(self.rank)

class Deck:
    """ Класс колоды карт """
    def __init__(self, number):
        self.cards = [Card(suit, rank, number) for suit in SUITS for rank in RANKS]
        self.deck_number = number

    def __repr__(self):
        return 'Deck #{}'.format(self.deck_number)

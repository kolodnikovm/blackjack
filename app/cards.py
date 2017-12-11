SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
RANKS = {
    "2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,
    "9":9,"10":10,"J":10,"Q":10,"K":10,"A":11
    }

class Card:
    def __init__(self, suit, rank, deck_nmb):
        self.suit = suit
        self.rank = rank
        self.deck_nmb = deck_nmb
        self.score = RANKS[rank]

    def __repr__(self):
        return self.suit+'_'+str(self.rank)

class Deck:
    def __init__(self, n):
        self.cards = [Card(s,r,n) for s in SUITS for r in RANKS]

    def __repr__(self):
        return 'Deck #{}'.format(self.n)

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
RANKS = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]


class Card:
    def __init__(self, suit, rank, deck_nmb):
        self.suit = suit
        self.rank = rank
        self.deck_nmb = deck_nmb
        if is_number(rank):
            self.score = int(rank)
        elif rank in ["J", "Q", "K"]:
            self.score = 10
        else: self.score = 11

class Deck:
    def __init__(self, n):
        self.cards = [Card(s,r,n) for s in SUITS for r in RANKS]

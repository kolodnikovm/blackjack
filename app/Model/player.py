class Player:
    def __init__(self, init_cards):
        self.hand = [c.rank+"_"+c.suit for c in init_cards]
        self.score = sum([c.score for c in init_cards])
        self.winner = 0
        self.total = 0

    def hit_me(self, card):
        self.hand.append(card.rank+"_"+card.suit)
        if card.rank == "A" and self.score > 10:
            self.score += 1
        else:
            self.score += card.score

class User(Player):
    def __init__(self, init_cards):
        Player.__init__(self, init_cards[:2])
        self.stand = False

    def stand(self):
        self.stand = True

class Computer(Player):
    def __init__(self, init_cards):
        Player.__init__(self,init_cards[:1])

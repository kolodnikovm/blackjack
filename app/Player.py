class Player:
    def __init__(self, init_cards):
        self.hand = [c.rank+"_"+c.suit for c in init_cards]
        self.score = sum([c.score for c in init_cards])
        self.winner = 0

    def hitMe(self, card):
        """ Request a card """
        self.hand.append(card[0].rank+"_"+card[0].suit)
        if card[0].rank == "A" and self.score > 10:
            self.score += 1
        else:
            self.score += card[0].score

class User(Player):
    def __init__(self, init_cards):
        Player.__init__(self, init_cards[:2])
        self.stand = False

    def stand(self):
        self.stand = True

class Computer(Player):
    def __init__(self, init_cards):
        Player.__init__(self,init_cards[:1])

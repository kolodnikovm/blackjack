class Player:
    def __init__(self):
        self.score = 0
        self.hand = []

    def hitMe(self, card):
        """ Request a card """
        self.hand.append(""+card.suit+card.rank)
        self.score += card.score

    def stand(self):
        """ No more cards needed """
        pass

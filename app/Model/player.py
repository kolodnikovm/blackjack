class Player:
    def __init__(self, init_cards=None):
        self.hand = init_cards
        self.score = 0
        if init_cards:
            self.score = sum([card.score for card in init_cards])
        self._winner = 0
        self._bet = 0

    def hit_me(self, card):
        self.hand.append(card)
        if card.rank == "A" and self.score > 10:
            self.score += 1
        else:
            self.score += card.score

    @property
    def bet(self):
        return self._bet

    @property
    def winner(self):
        return self._winner

    @bet.setter
    def bet(self, value):
        if isinstance(value, int):
            self._bet = value

    @winner.setter
    def winner(self, value):
        self._winner = value


class User(Player):
    def __init__(self, init_cards):
        super().__init__(init_cards[:2])
        self.stand = False

    def no_more_cards(self):
        self.stand = True


class Computer(Player):
    def __init__(self, init_cards):
        super().__init__([init_cards])

class GameView():

    def __init__(self, controller):
        self._controller = controller
        self.actions = {'h': self._controller.give_cards,
                        's': self._controller.user_stand,
                        'e': self._controller.throw_exception,
                        'a': self.add_bet}

    def model_changed(self, data):
        print('\nSTATS\n')
        print("My score: {user_score}".format(user_score=data['user'].score),
              end='\n' + '-' * 40 + '\n')
        print("My cards:{user_cards}".format(user_cards=data['user'].hand),
              end='\n' + '-' * 40 + '\n')

    def show_start_game_message(self):
        message = """
        New game started
        Controls:
            h - get a card
            s - no cards
            a - add bet
        """
        print(message)

    def show_start_game_state(self, data):
        start_state = """
        My score: {user_score}
        My cards: {user_cards}
        """.format(user_score=data['user'].score, user_cards=data['user'].hand)
        print(start_state)

    def show_endgame_stats(self, data):
        stats = """
        User score: {user_score}
        User cards: {user_cards}
        ---------------------
        Computer score: {computer_score}
        Computer cards: {computer_cards}
        ---------------------
        Total score: User: {user_total} || Computer: {computer_total}
        """.format(
            user_score=data['user'].score,
            user_cards=data['user'].hand,
            computer_score=data['computer'].score,
            computer_cards=data['computer'].hand,
            user_total=data['user_total'],
            computer_total=data['computer_total']
        )

        print(stats)

    def set_bet(self):
        user_bet = input('Set your bet: ')
        self._controller.set_bet(user_bet)

    def add_bet(self):
        bet_to_add = input('Bet to add: ')
        self._controller.add_bet(bet_to_add)

    def request_action(self):
        action = input('Hit or Stand [h]/[s] - ')
        return action

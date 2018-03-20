class GameView():

    def __init__(self, controller):
        self._controller = controller
        self._actions = {'h': self._controller.give_cards,
                         's': self._controller.user_stand,
                         'e': self._controller.throw_exception}

    def model_changed(self, data):
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
        """
        print(message)

    def set_bet(self):
        user_bet = input('Set your bet: ')
        self._controller.set_bet(user_bet)

    def show_start_game_state(self):
        start_state = """
        My score: {user_score}
        My cards: {user_cards}
        """.format(user_score=self._controller._model._user.score, user_cards=self._controller._model._user.hand)
        print(start_state)

    def game_cycle(self):
        self.show_start_game_message()
        self.set_bet()
        self.show_start_game_state()

        while not self._controller._model._game_over:
            action = input('Hit or Stand [h]/[s] - ')
            try:
                self._actions[action]()
            except KeyError:
                print('Invalid input')

        self.show_stats()

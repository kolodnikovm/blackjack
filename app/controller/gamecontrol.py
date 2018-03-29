from app.view.gameview import GameView


class GameController:
    def __init__(self, model):
        self._model = model
        self._view = GameView(self)
        self._observers = []

        # Add observers to model and controller
        self._model.add_observer(self)
        self.add_observer(self._view)

# View actions handlers
    def give_cards(self, *args, **kwargs):
        self._model.hit_all()

    def user_stand(self, *args, **kwargs):
        self._model.computer_fill()

    def throw_exception(self, *args, **kwargs):
        raise Exception

    def set_bet(self):
        bet = self._view.set_bet()
        self._model.set_bet(bet)

    def add_bet(self, *args, **kwargs):
        bet_to_add = self._view.add_bet()
        self._model.add_bet(bet_to_add)

    def check_winner(self):
        self._model.check_winner()

    def get_db_data(self):
        db_data = self._model.get_history()[1:]
        return db_data

    def count_totals(self):
        data = self.get_db_data()
        totals = {'user_total': self._model.user.winner,
                  'computer_total': self._model.computer.winner}
        for row in data:
            totals['user_total'] += int(row['user win'])
            totals['computer_total'] += int(row['computer win'])
        return totals

    def get_model_data(self):
        data = {'user': self._model.user, 'computer': self._model.computer}
        return data

    def send_model_data(self):
        data = self.get_model_data()
        self.notify(data)

    def post_game_actions(self):
        self._model.save_history()

    # TODO Вынести работу с _view
    def game_cycle(self):
        self._view.show_start_game_message(new=self._model.new_game)
        if self._model.new_game:
            self._view.set_bet()
        else:
            self._view.show_start_game_state(self.get_model_data())

        while not self._model.stop_game():
            action = self._view.request_action()
            try:
                self._view.actions[action](self.get_model_data())
            except KeyError:
                self._view.show_error_input()

        self._view.show_endgame_stats(
            {**self.get_model_data(), **self.count_totals()})
        self.post_game_actions()

    def model_changed(self):
        self.send_model_data()

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify(self, data):
        for observer in self._observers:
            observer.model_changed(data)

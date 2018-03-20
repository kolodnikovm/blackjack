from app.view.gameview import GameView


class GameController:
    def __init__(self, model):
        self._model = model
        self._view = GameView(self)
        self._observers = []

        # Add observers to model and controller
        self._model.add_observer(self)
        self.add_observer(self._view)

    def give_cards(self):
        self._model.hit_all()

    def user_stand(self):
        self._model.computer_fill()

    def throw_exception(self):
        raise Exception

    def check_winner(self):
        self._model.check_winner()

    def set_bet(self, bet):
        self._model.user.bet = bet

    def retrieve_model_data(self):
        data = {'user': self._model.user, 'computer': self._model.computer}
        self.notify(data)

    def model_changed(self):
        self.retrieve_model_data()

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify(self, data):
        for observer in self._observers:
            observer.model_changed(data)

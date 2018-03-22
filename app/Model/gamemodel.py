from app.database.dababase import DataBase
from app.model.player import Computer, User
from app.model.shoes import Shoes
from app.utilities.functions import define_winner
import collections


class GameModel:
    def __init__(self, db_filename=None):
        self._win_checker = define_winner
        self._shoes = Shoes()
        self._user = User(self.shoes.get_card(2))
        self._computer = Computer(self.shoes.get_card())
        self._game_over = False
        self._new_game = True
        self._observers = []
        self.database = DataBase(db_filename)

    @property
    def user(self):
        return self._user

    @property
    def computer(self):
        return self._computer

    @property
    def shoes(self):
        return self._shoes

    def check_winner(self):
        self._game_over, winners = self._win_checker(
            self._user.score, self._computer.score, stand=self._user.stand)
        if self._game_over:
            self._user.winner, self._computer.winner = list(winners.values())
        return not self._game_over

    def _give_card_to_user(self):
        self._user.hit_me(self._shoes.get_card())

    def _give_card_to_comp(self):
        self._computer.hit_me(self._shoes.get_card())

    def hit_all(self):
        self._give_card_to_comp()
        self._give_card_to_user()
        self.notify()

    def computer_fill(self):
        self._user.no_more_cards()
        while self._computer.score <= 17:
            self._give_card_to_comp()
        self.notify()

    def save_history(self):
        data = {
            'user cards': self.user.hand,
            'computer cards': self.computer.hand,
            'user win': self.user.winner,
            'computer win': self.computer.winner,
        }
        self.database.save_data(data)

    def get_history(self):
        data = self.database.load_data()
        return data

    def set_bet(self, bet):
        self.user.bet = bet
        self.notify()

    def add_bet(self, bet):
        self.user.bet += bet
        self.notify()

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.model_changed()

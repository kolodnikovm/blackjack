import logging

from app.database.dababase import DataBase
from app.model.player import Computer, User
from app.model.shoes import Shoes
from app.utilities.functions import define_winner


class GameModel:
    _DBFIELDS = ['user cards', 'computer cards', 'user win', 'computer win']

    def __init__(self, db_filename=None):
        self._win_checker = define_winner
        self.database = DataBase(
            db_filename=db_filename, fieldnames=GameModel._DBFIELDS)
        try:
            restored_data = self.database.load_data(restore=True)
            self._shoes = restored_data['shoes']
            self._user = restored_data['user']
            self._computer = restored_data['computer']
            self._new_game = False
            self.database.reset_file()
        except Exception as e:
            logging.warning(
                'Error occured while retrieving backup data\n => %s', e)
            self._shoes = Shoes()
            self._user = User(self.shoes.get_card(2))
            self._computer = Computer(self.shoes.get_card())
            self._new_game = True
        self._game_over = False
        self._observers = []

    @property
    def game_over(self):
        return self._game_over

    @property
    def new_game(self):
        return self._new_game

    @property
    def user(self):
        return self._user

    @property
    def computer(self):
        return self._computer

    @property
    def shoes(self):
        return self._shoes

    @game_over.setter
    def game_over(self, value):
        self._game_over = value

    def stop_game(self):
        self.game_over, winners = self._win_checker(
            self.user.score, self._computer.score, stand=self._user.stand)
        if self.game_over:
            self.user.winner, self.computer.winner = list(winners.values())
        return self.game_over

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

    def backup_data(self):
        data = {
            'user': self.user,
            'computer': self.computer,
            'shoes': self.shoes
        }
        self.database.save_data(data, backup=True)

    def close_db(self):
        self.database.close_database()

    def set_bet(self, bet):
        self.user.bet = int(bet)
        self.notify()

    def add_bet(self, bet):
        self.user.bet += int(bet)
        self.notify()

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.model_changed()

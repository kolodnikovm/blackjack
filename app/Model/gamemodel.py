""" Модуль модели игры """

from .player import User, Computer
from .shoes import Shoes
from ..utilities.supfuncs import check_winner


class GameModel:
    """ Model в паттерне MVC """

    def __init__(self, decks=1):
        self.__win_checker = check_winner
        self._shoes = Shoes(decks)
        self._user = User(self.shoes.get_card(2))
        self._computer = Computer(self.shoes.get_card())
        self._game_over = False
        self._observers = []

    @property
    def user(self):
        return self._user

    @property
    def computer(self):
        return self._computer

    @property
    def shoes(self):
        return self._shoes

    def is_game_over(self):
        return self.__win_checker(self._user, self._computer)

    def give_card_to_user(self):
        """ Добавляет в набор карт юзера одну карту из общей колоды. """
        self._user.hit_me(self._shoes.get_card())

    def give_card_to_comp(self):
        """ Добавляет в набор кард компа одну карту из общей колоды. """
        self._computer.hit_me(self._shoes.get_card())

    def add_observer(self, observer):
        """ Добавляет слушателя """
        self._observers.append(observer)

    def remove_observer(self, observer):
        """ Удаляет слушателя """
        self._observers.remove(observer)

    def notify(self):
        """ Оповещает слушателей """
        for observer in self._observers:
            observer.model_changed()

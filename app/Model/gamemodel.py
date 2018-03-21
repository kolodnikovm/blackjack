from app.database.dababase import DataBase
from app.model.player import Computer, User
from app.model.shoes import Shoes
from app.utilities.functions import define_winner


class GameModel:
    def __init__(self, decks=1):
        self._win_checker = define_winner
        self._shoes = Shoes(decks)
        self._user = User(self.shoes.get_card(2))
        self._computer = Computer(self.shoes.get_card())
        self._game_over = False
        self._new_game = True
        self._observers = []
        self.database = DataBase()

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
        """
        Определяет состояние игры.
        Возращает кортеж из 2 элементов:
            - 1 элемент: True - победитель определен, False - игра продолжается
            - 2 элемент: словарь вида 'игрок':1(0) - победа(поражение)
        """
        self._game_over, winners = self._win_checker(
            self._user.score, self._computer.score, stand=self._user.stand)
        if self._game_over:
            self._user.winner, self._computer.winner = list(winners.values())
        return not self._game_over

    def _give_card_to_user(self):
        """ Добавляет в набор карт юзера одну карту из общей колоды. """
        self._user.hit_me(self._shoes.get_card())

    def _give_card_to_comp(self):
        """ Добавляет в набор кард компа одну карту из общей колоды. """
        self._computer.hit_me(self._shoes.get_card())

    def hit_all(self):
        """ Раздает по одной карте компьютеру и юзеру,
        затем оповещает модель об изменении данных. """
        self._give_card_to_comp()
        self._give_card_to_user()
        self.notify()

    def computer_fill(self):
        """ Если пользователь решил не брать карту, то комп добирает карты
        пока не  наберем минимум 17 очков. Затем оповещает модель об изменении."""
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

    def set_bet(self, bet):
        self._user.bet = bet
        self.notify()

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

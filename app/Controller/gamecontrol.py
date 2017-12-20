""" Module Docstring """
from ..Utilities.supfuncs import check_winner
from ..Utilities.database import DataBase
from ..View.gameview import GameView


class GameController:
    """ Контроллер вмодели MVC.  """

    def __init__(self, model, db_path):
        self.model = model
        self.view = GameView(self, self.model)
        self.checker = check_winner
        self.database = DataBase(db_path)

    def hit_all(self):
        """ Раздает по одной карте компьютеру и юзеру,
        затем оповещает модель об изменении данных. """
        self.model.give_card_to_comp()
        self.model.give_card_to_user()
        self.model.notify()

    def computer_fill(self):
        """ Если пользователь решил не брать карту, то комп добирает карты
        пока не  наберем минимум 17 очков. Затем оповещает модель об изменении."""
        self.model.user.no_more_cards()
        while self.model.computer.score <= 17:
            self.model.give_card_to_comp()
        self.model.notify()

    def game_over(self):
        """ Вызывается при окончании игры. Выбранные данные в переменной entrance передаются в метод
        БД save_data(data) для сохранения data в БД.
        Затем происходит закрытие дескриптора на файл БД. """
        entrance = [self.model.user.hand, self.model.computer.hand,
                    self.model.user.winner, self.model.computer.winner]
        self.database.save_data(entrance)
        self.allocate_total_score()
        print("___TOTAL___", self.model.user.total)
        self.database.db_file.close()

    def allocate_total_score(self):
        """ Считывает общую историю побед для каждого из игроков.
        Записывает результат в параметры total каждого из объектов. """
        self.model.user.total = self.model.user.winner
        self.model.computer.total = self.model.computer.winner
        totals = self.database.read_total_score()
        self.model.user.total += totals[0]
        self.model.computer.total += totals[1]

    def get_players(self):
        """ Возращает обекты юзера и компа """
        return self.model.user, self.model.computer

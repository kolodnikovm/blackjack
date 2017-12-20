""" Вынести в отдельный файл? А здесь сделать функцию create_game,
возращающую экземпляр GameManager """

import dill
from .Utilities.supfuncs import reset_file
from .Model.gamemodel import GameModel
from .Controller.gamecontrol import GameController

class GameManager:
    """ Верхнеуровневый класс урпавления игрой """

    def __init__(self, db_path='./db.csv', decks=1):
        """ Конструктор класса GameManager.Создает компоненты view, model.
        В качестве входных параметров принимает количество колод карт для игры
        и путь до файла БД. """
        self.data = None
        self._model = GameModel(decks)
        self._controller = GameController(self._model, db_path)

    def run_game(self):
        """ Запускает игровой цикл.
        Проверяет файл data, который служит буфером для хранения
        состояния игры, которая крашнулась на предыдущем запуске.
        Если он пустой, создается новая игра, в проитвном случае
        загружается предыдущее состояние.
        Каждый запуск игрового цикла обернут в try для перехвата ошибок.
        При возникновении ошибки во время цикла игры, текущее состояние
        сохраняется в data."""
        with open('data', 'r+b') as self.data:
            try:
                self = dill.load(self.data)
                try:
                    self._controller.view.show_game()
                except Exception as e:
                    reset_file(self.data)
                    dill.dump(self, self.data)
                else:
                    reset_file(self.data)
            except EOFError:
                try:
                    self._controller.view.show_game()
                except Exception as e:
                    dill.dump(self, self.data)

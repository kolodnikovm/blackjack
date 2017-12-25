""" Верхнеуровневый класс управления игрой """

import traceback
import dill
from .Utilities.supfuncs import reset_file
from .game import Game

class GameManager:
    """ Верхнеуровневый класс урпавления игрой """
    def __init__(self, decks=1, db_path='./db.csv'):
        self._game = None
        self.decks = decks
        self.db_path = db_path

    def run_game(self):
        """ Запускает игровой цикл.
        Проверяет файл data, который служит буфером для хранения
        состояния игры, которая крашнулась на предыдущем запуске.
        Если он пустой, создается новая игра, в проитвном случае
        загружается предыдущее состояние.
        Каждый запуск игрового цикла обернут в try для перехвата ошибок.
        При возникновении ошибки во время цикла игры, текущее состояние
        сохраняется в data."""
        with open('data', 'r+b') as bufer_data:
            try:
                print('Try reloading')
                self._game = dill.load(bufer_data)
                try:
                    print('Reloading Passed. Game retry')
                    self._game.show()
                except Exception as e:
                    print(e,'Reloaded game error')
                    traceback.print_tb(e.__traceback__)
                    reset_file(bufer_data)
                    dill.dump(self._game, bufer_data)
                else:
                    reset_file(bufer_data)
            except EOFError:
                try:
                    print('New game created')
                    self._game = Game(self.decks, self.db_path)
                    self._game.show()
                except Exception as e:
                    print(e, 'New game error')
                    traceback.print_tb(e.__traceback__)
                    dill.dump(self._game, bufer_data)

            
    def test_game(self):
        print('New test game created')
        self._game = Game(self.decks, self.db_path)
        self._game.show()
from .game import Game
import dill

class GameManager:
    __decks = 1

    def __init__(self, decks = 1):
        self.game = Game(decks)
        __decks = decks

    def run(self):
        with open('data', 'r+b') as data:
            try:
                print('Try restoring\n')
                self.game = dill.load(data)
                print('Succsessful restore :: ', self.game.user.hand,'\n')
                try:
                    print('Run restored game')
                    self.game.runGame()
                except Exception as e:
                    print('Restored Game runtime error', e)
                    GameManager.fileReset(data)
                    dill.dump(self.game, data)
                else:
                    GameManager.fileReset(data)
            except EOFError:
                print('Empty File => EOFError\nTry New Game')
                self.game = Game(GameManager.__decks)
                try:
                    print('\nNew Game running')
                    self.game.runGame()
                except Exception as e:
                    print('\nNew Game Runtime Error occured', e)
                    dill.dump(self.game, data)

    def fileReset(f):
        f.seek(0)
        f.truncate()

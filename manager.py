from app import createGame, fileReset
import dill

if __name__ == '__main__':
        with open('data', 'r+b') as data:
            try:
                print('Try restoring\n')
                restored = dill.load(data)
                print('Succsessful restore :: ', restored.user.hand,'\n')
                try:
                    print('Run restored game')
                    restored.runGame()
                except Exception as e:
                    print('Restored Game runtime error', e)
                    fileReset(data)
                    dill.dump(restored, data)
                else:
                    fileReset(data)
            except EOFError:
                print('Empty File => EOFError\nTry New Game')
                gm = createGame()
                try:
                    print('\nNew Game running')
                    gm.runGame()
                except Exception as e:
                    print('\nNew Game Runtime Error occured', e)
                    dill.dump(gm, data)

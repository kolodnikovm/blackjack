from .gamemanager import GameManager

def createGame(d = 1):
    return GameManager(d)

def fileReset(f):
    f.seek(0)
    f.truncate()

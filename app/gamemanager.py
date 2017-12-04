from .player import User, Computer
from .shoes import Shoes
import csv

class GameManager:
    class __GameManager:
        def __init__(self, decks = 1):
            self.shoes = Shoes(decks)
            self.user = User(self.shoes.getCard(2))
            self.computer = Computer(self.shoes.getCard())
            self.db = open("db.csv",'r+', newline='')
        def __str__(self):
            return repr(self)

    instance = None

    def __init__(self, decks = 1):
        if not GameManager.instance:
            GameManager.instance = GameManager.__GameManager(decks)
        else:
            GameManager.instance.shoes = Shoes(decks)
            GameManager.instance.user = User(self.shoes.getCard(2))
            GameManager.instance.computer = Computer(self.shoes.getCard())

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def gameStatus(self,u,c):
        entrance = [u.hand, c.hand, u.winner, c.winner]
        writer = csv.writer(self.db)
        writer.writerow(entrance)
        # self.db.flush()
        reader = csv.reader(self.db)
        u.total, c.total = u.winner, c.winner
        for row in reader:
            u.total += int(row[2]); c.total += int(row[3])
        status = "\nUser's score:{} || Computer's score: {}\nMy cards{}\nComps's{}\nTotal score: User: {}, Computer: {}"\
                        .format(u.score, c.score, u.hand, c.hand, u.total, c.total)
        self.db.close()
        print(status)

    def checkWinner(self, u, c):
        if u.stand:
            if (c.score > u.score) and (c.score <= 21):
                print('Computer wins')
                c.winner = 1
                return False
            elif (c.score == u.score):
                print('Draw')
                return False
            else:
                print('User wins')
                u.winner = 1
                return False
        if u.score < 21 and c.score < 21:
            return True
        elif (c.score == 21 and u.score == 21) or (u.score > 21 and c.score > 21):
            print('Draw')
            return False
        elif (c.score <= 21 and u.score > 21) or (c.score == 21 and u.score < 21):
            print('Computer wins')
            c.winner = 1
            return False
        elif (c.score > 21 and u.score <= 21) or (u.score == 21 and c.score < 21):
            print('User wins')
            u.winner = 1
            return False

    def runGame(self):
        print('\nGame started\n')

        while self.checkWinner(self.user, self.computer):
            print("My score: {}".format(self.user.score), end='\n'+'-'*40+'\n')
            print("My cards:{}".format(self.user.hand), end='\n'+'-'*40+'\n')
            opt = input('Hit or Stand [h]/[s]')
            if opt == 'h':
                self.computer.hitMe(self.shoes.getCard())
                self.user.hitMe(self.shoes.getCard())
            elif opt == 's':
                self.user.stand = True
                while self.computer.score < 17:
                    self.computer.hitMe(self.shoes.getCard())

        self.gameStatus(self.user, self.computer)

from app.player import User, Computer, Player
from app.shoes import Shoes

shoes = Shoes(4)
shoes.shuffleDeck()

computer = Computer(shoes.getCard())
user = User(shoes.getCard(2))


def gameStatus(u,c):
    status = "\nUser's score:{} || Computer's score: {}\nMy cards{}\nComps's{}"\
                    .format(u.score, c.score, u.hand, c.hand)
    print(status)

def checkWinner(u, c):
    if u.stand:
        if (c.score > u.score) and (c.score <= 21):
            print('Computer wins')
            return False
        elif (c.score == u.score):
            print('Draw')
            return False
        else:
            print('User wins')
            return False
    if u.score < 21 and c.score < 21:
        return True
    elif (c.score == 21 and u.score == 21) or (u.score > 21 and c.score > 21):
        print('Draw')
        return False
    elif (c.score <= 21 and u.score > 21) or (c.score == 21 and u.score < 21):
        print('Computer wins')
        return False
    elif (c.score > 21 and u.score <= 21) or (u.score == 21 and c.score < 21):
        print('User wins')
        return False

print('\nGame started\n')

while checkWinner(user, computer):
    print("My score: {}".format(user.score), end='\n'+'-'*40+'\n')
    print("My cards:{}".format(user.hand), end='\n'+'-'*40+'\n')
    opt = input('Hit or Stand [h]/[s]')
    if opt == 'h':
        computer.hitMe(shoes.getCard())
        user.hitMe(shoes.getCard())
    elif opt == 's':
        user.stand = True
        while computer.score < 17:
            computer.hitMe(shoes.getCard())

gameStatus(user, computer)

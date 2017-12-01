from app.player import User, Computer, Player
from app.shoes import Shoes

shoes = Shoes(1)
shoes.shuffleDeck()

computer = Computer(shoes.getCard())
user = User(shoes.getCard(2))


def gameStatus(u,c):
    status = "\nUser's score:{} || Computer's score: {}\nMy cards{}\nComps's{}" \
                    .format(u.score, c.score, u.hand, c.hand)
    print(status)

def checkWinner(u, c):
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
        pass

gameStatus(user, computer)

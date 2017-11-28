from app.player import Player
from app.shoes import Shoes


user = Player()
computer = Player()
shoes = Shoes(1)
shoes.shuffleDeck()

def gameStatus(u,c):
    status = "User's score:{} || Computer's score: {}".format(u.score, c.score)
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
    print("My score: {}".format(user.score))
    print("My Cards:{}".format(user.hand))
    opt = input('Hit or Stand [h]/[s]')
    if opt == 'h':
        computer.hitMe(shoes.stock[0].cards.pop())
        user.hitMe(shoes.stock[0].cards.pop())
    elif opt == 's':
        pass

gameStatus(user, computer)

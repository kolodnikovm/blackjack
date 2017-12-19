def check_winner(u, c):
        if u.stand:
            if (c.score > u.score) and (c.score <= 21):
                print('\nComputer wins')
                c.winner = 1
                return False
            elif (c.score == u.score):
                print('\nDraw')
                return False
            else:
                print('\nUser wins')
                u.winner = 1
                return False
        if u.score < 21 and c.score < 21:
            return True
        elif (c.score==21 and u.score==21) or (u.score>21 and c.score>21):
            print('\nDraw')
            return False
        elif (c.score<=21 and u.score>21) or (c.score==21 and u.score<1):
            print('\nComputer wins')
            c.winner = 1
            return False
        elif (c.score>21 and u.score<=21) or (u.score==21 and c.score<21):
            print('\nUser wins')
            u.winner = 1
            return False
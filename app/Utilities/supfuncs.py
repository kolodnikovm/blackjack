""" Модуль вспомогательных функций """


def check_winner(u, c):
    """ Функция проверки победителя. Принимает объекты экземпляров
    с парамтером score. """
    if u.stand:
        if (c.score > u.score) and (c.score <= 21):
            print('\nComputer wins')
            c.winner = 1
            return False
        elif c.score == u.score:
            print('\nDraw')
            return False
        print('\nUser wins')
        u.winner = 1
        return False
    if u.score < 21 and c.score < 21:
        return True
    elif (c.score == 21 and u.score == 21) or (u.score > 21 and c.score > 21):
        print('\nDraw')
        return False
    elif (c.score <= 21 and u.score > 21) or (c.score == 21 and u.score < 1):
        print('\nComputer wins')
        c.winner = 1
        return False
    elif (c.score > 21 and u.score <= 21) or (u.score == 21 and c.score < 21):
        print('\nUser wins')
        u.winner = 1
        return False

def reset_file(data):
    """ Очищает файл data """
    data.seek(0)
    data.truncate()

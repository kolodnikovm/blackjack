""" Модуль вспомогательных функций """


def check_winner(user, computer):
    """ 
    Функция проверки победителя. Принимает объекты экземпляров
    с парамтером score. Возращает False, если игра должна продолжаться, 
    True - определен результат, игра должна завершиться. 
    При этом определяется победитель в свойстве соответствующего игрока.
    """
    if user.score < 21 and computer.score < 21:
        if user.stand:
            if user.score > computer.score:
                print('\nUser wins')
                user.winner = True
            elif computer.score > user.score:
                print('\nlogComputer wins')
                computer.winner = True
            else:
                print('\nlogDraw')
            return True
        return False
    elif (computer.score == 21 and user.score == 21) or (user.score > 21 and computer.score > 21):
        print('\nlogDraw')
        return True
    elif (computer.score <= 21 and user.score != 21):
        print('\nlogComputer wins')
        computer.winner = True
        return True
    elif (user.score <= 21 and computer.score != 21):
        print('\nUser wins')
        user.winner = True
        return True


def reset_file(data):
    """ Очищает файл data """
    data.seek(0)
    data.truncate()
    print('logdata cleared')

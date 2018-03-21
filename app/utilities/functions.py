import logging


def define_winner(user_score, computer_score, stand=False):
    """ 
    Функция проверки победителя.
    Возращает False, если игра должна продолжаться, 
    True - определен результат, игра должна завершиться. 
    При этом определяется победитель в свойстве соответствующего игрока.
    """

    if user_score < 21 and computer_score < 21:
        if stand:
            result_winner = {'user': 0, 'computer': 0}
            if user_score > computer_score:
                logging.debug('User wins')
                result_winner['user'] = 1
            elif computer_score > user_score:
                logging.debug('Computer wins')
                result_winner['computer'] = 1
            else:
                logging.debug('Draw')
            return True, result_winner
        return False, None
    elif (computer_score == 21 and user_score == 21) or (user_score > 21 and computer_score > 21):
        logging.debug('Draw')
        result_winner = {'user': 0, 'computer': 0}
        return True, result_winner
    elif (computer_score <= 21 and user_score != 21):
        logging.debug('Computer wins')
        result_winner = {'user': 0, 'computer': 1}
        return True, result_winner
    elif (user_score <= 21 and computer_score != 21):
        logging.debug('User wins')
        result_winner = {'user': 1, 'computer': 0}
        return True, result_winner


# def reset_file(data):
#     """ Очищает файл data """
#     data.seek(0)
#     data.truncate()
#     print('log_data cleared')

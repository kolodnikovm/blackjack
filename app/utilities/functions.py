import logging


def define_winner(user_score, computer_score, stand=False):
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


def logger(f):
    def wrapper(self, *args, **kwargs):
        logging.debug('Action: {action_name} || args: {args} kwargs: {kwargs}'
                      .format(action_name=f.__name__, args=args, kwargs=kwargs))
        f(self, *args, **kwargs)
    return wrapper

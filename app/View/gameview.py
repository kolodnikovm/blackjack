class GameView():

    def __init__(self, controller, model):
        self.controller = controller
        self.model = model

        # добавляет view компонент в слушатели model
        self.model.add_observer(self)

    def model_changed(self):
        """ Отображает измененый набор карт и очков для игрока. """

        print("My score: {}".format(self.model.user.score),
              end='\n' + '-' * 40 + '\n')
        print("My cards:{}".format(self.model.user.hand),
              end='\n' + '-' * 40 + '\n')

    def game_status(self, user, computer):
        """ Принтует финальный статус игры """
        data = {
            'u_score': user.score, 'c_score': computer.score,
            'u_cards': user.hand, 'c_cards': computer.hand
        }
        status = ("\nUser's score:{u_score} || Computer's score: {c_score}" +
                  "\nMy cards{u_cards}\nComps's cards: {c_cards}") \
            .format(data)
        print(status)

    def show_game(self):
        """ Выводит информацю о начале игры и запускает игровой цикл. """

        print('\nGame started\n')

        # отобразить стартовое состояние игры
        print("My score: {}".format(self.model.user.score),
              end='\n' + '-' * 40 + '\n')
        print("My cards:{}".format(self.model.user.hand),
              end='\n' + '-' * 40 + '\n')

        while self.controller.checker(*self.controller.get_players()):
            opt = input('Hit or Stand [h]/[s] - ')
            if opt == 'h':
                self.controller.hit_all()
            elif opt == 's':
                self.controller.computer_fill()
            elif opt == 'e':
                raise Exception

        self.controller.game_over()
        self.game_status(*self.controller.get_players())

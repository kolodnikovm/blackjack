class GameView():

    def __init__(self, controller, model):
        self.controller = controller
        self.model = model

        # добавляет view компонент в слушатели model
        self.model.add_observer(self)

    def model_changed(self):
        """ Отображает измененый набор карт и очков для игрока. """

        print("My score: {}".format(self.model.user.score), end='\n'+'-'*40+'\n')
        print("My cards:{}".format(self.model.user.hand), end='\n'+'-'*40+'\n')

    def game_status(self, u, c):
        status = ("\nUser's score:{} || Computer's score: {}\nMy cards{}" +
                  "\nComps's{}\nTotal score: User: {}, Computer: {}") \
                  .format(u.score, c.score, u.hand, c.hand, u.total, c.total)
        print(status)

    def show_game(self):
        """ Выводит информацю о начале игры и запускает игровой цикл. """

        print('\nGame started\n')

        #отобразить стартовое состояние игры
        print("My score: {}".format(self.model.user.score), end='\n'+'-'*40+'\n')
        print("My cards:{}".format(self.model.user.hand), end='\n'+'-'*40+'\n')

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
        
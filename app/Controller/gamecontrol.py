from ..Utilities.database import DataBase
from ..View.gameview import GameView
from ..Utilities.supfuncs import check_winner

class GameController:
    def __init__(self, model):
        self.model = model
        self.view = GameView(self, self.model)
        self.checker = check_winner
        self.database = DataBase('./db.csv')

    def hit_all(self):
        self.model.give_card_to_comp()
        self.model.give_card_to_user()
        self.model.notify()
    
    def computer_fill(self):
        self.model.user.stand = True
        while self.model.computer.score < 17:
            self.model.give_card_to_comp()
        self.model.notify()

    def game_over(self):
        entrance = [self.model.user.hand, self.model.computer.hand, 
                    self.model.user.winner, self.model.computer.winner]
        self.database.save_data(entrance)
        self.database.db_file.close()
    
    def get_players(self):
        return self.model.user, self.model.computer
from .player import User, Computer
from .shoes import Shoes

class GameModel:
    def __init__(self, decks = 1):
        self._mShoes = Shoes(decks)
        self._mUser = User(self.shoes.get_card(2))
        self._mComputer = Computer([self.shoes.get_card()])

        self._mObservers = []
    
    @property
    def user(self):
        return self._mUser
    
    @property
    def computer(self):
        return self._mComputer
    
    @property
    def shoes(self):
        return self._mShoes

    def give_card_to_user(self):
        self._mUser.hit_me(self._mShoes.get_card())
    
    def give_card_to_comp(self):
        self._mComputer.hit_me(self._mShoes.get_card())

    def add_observer(self, observer):
        self._mObservers.append(observer)
    
    def remove_observer(self, observer):
        self._mObservers.remove(observer)

    def notify(self):
        for x in self._mObservers:
            x.model_changed()
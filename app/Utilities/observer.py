from abc import ABCmeta, abstractmethod

class GameObserver(metaclass = ABCmeta):

    def model_changed(self):
        pass
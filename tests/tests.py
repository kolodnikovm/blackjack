import unittest


class TestModelMethods(unittest.TestCase):

    def setUp(self):
        from app.model.gamemodel import GameModel
        from app.configs.configs import CONFIGS
        self.__configs = CONFIGS['test']()
        self.__game_model = GameModel(self.__configs.DATABASE)

    def test_give_card_to_user(self):
        pass

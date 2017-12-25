from .gamemanager import GameManager

def create_app():
    game_manager = GameManager()
    return game_manager
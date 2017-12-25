from app import create_app

game_manager = create_app()

if __name__ == '__main__':
    game_manager.test_game()

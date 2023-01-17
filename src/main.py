from src.game.game import Game

game = Game()
while not game.is_ended:
    game.show_info()
    game.get_command()
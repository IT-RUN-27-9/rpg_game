from src.game.game import Game

game = Game()
while not game.is_ended:
    game.show_info()
    game.monster_actions()
    game.get_command()
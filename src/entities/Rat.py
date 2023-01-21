from src.entities.Monster import Monster


class Rat(Monster):
    def __init__(self, x_coord, y_coord, game):
        super().__init__(x_coord, y_coord, 10, 2, game)

    def __str__(self):
        return 'Крыса'
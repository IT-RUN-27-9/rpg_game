from src.entities.Monster import Monster


class Rat(Monster):
    def __init__(self, x_coord, y_coord):
        super().__init__(x_coord, y_coord, 10, 2)

from src.entities.base_entity import Entity
from src.incantation.fireball import Fireball
from src.incantation.superheal import SuperHeal


class Player(Entity):

    def __init__(self, x_coord, y_coord, game):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.hp = 500
        self.attack = 50
        self.mana = 25
        self.game = game
        self.incantations = [SuperHeal, Fireball]
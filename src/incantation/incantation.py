from abc import ABC, abstractmethod


class Incantation(ABC):
    def __init__(self, mana, allow_target_self, allow_target_monster):
        self.mana = mana
        self.allow_target_self = allow_target_self
        self.allow_target_monster = allow_target_monster
    @abstractmethod
    def cast(self, target):
        pass

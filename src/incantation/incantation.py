from abc import ABC, abstractmethod


class Incantation(ABC):
    def __init__(self, mana):
        self.mana = mana
    @abstractmethod
    def cast(self, target):
        pass

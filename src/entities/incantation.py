from abc import ABC, abstractmethod


class Incantaion(ABC):
    @abstractmethod
    def cast(self, target):
        pass

class Fireball(Incantaion):
    def cast(self, target):
        target.hp -= 10


class Heal(Incantaion):
    def cast(self, target):
        target.hp += 5
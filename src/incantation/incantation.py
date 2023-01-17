from abc import ABC, abstractmethod


class Incantation(ABC):
    @abstractmethod
    def cast(self, target):
        pass

class Fireball(Incantation):
    def cast(self, target):
        target.hp -= 10


class Heall(Incantation):
    def cast(self, target):
        target.hp += 5

class SuperHeal(Incantation):
    def cast(self, target):
        target.hp += 50
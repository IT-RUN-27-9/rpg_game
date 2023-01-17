from abc import ABC, abstractmethod


class Incantation(ABC):
    @abstractmethod
    def cast(self, target):
        pass

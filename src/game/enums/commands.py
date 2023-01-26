from enum import Enum


class Commands(str, Enum):
    nothing = "Ничего не делать"
    move = "Сделать ход"
    hit = "Ударить текущую цель"

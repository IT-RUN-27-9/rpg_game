

# Система заклинаний. Нужно создать базовый класс Incantation, в котором будет одна функция cast, которая принимает
# target и ничего с ней не делает. От него унаследовать пару классов, типа Heal и Fireball, которые лечат и дамажат
# соответственно. Далее можешь пофантазировать, что ещё можно сделать с целью, например сжечь ману или заморозить
# (для второго нужно будет подправить класс Entity)
class Incantaion:
    @classmethod
    def cast(self, target):
        pass

class Fireball(Incantaion):
    def cast(self, target):
        target.hp -= 10


class Heal(Incantaion):
    def cast(self, target):
        target.hp += 5



# ЭТО ТЕСТЫ ЗАКЛИНАНИЙ
# class Monster(Fireball):
#     def __init__(self, hp):
#         self.hp = hp
#
# testdemon = Monster(1000)
# test2demon = Monster(50)
# testdemon.cast(test2demon)
# print(test2demon.hp)
# print(testdemon.hp)
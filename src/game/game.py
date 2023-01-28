import random

from src.entities.FileGolem import FireGolem
from src.entities.Monster import Monster
from src.entities.Player import Player
from src.entities.Rat import Rat
from src.entities.Vampire import Vampire
from src.entities.base_entity import Direction
from src.game.enums.commands import Commands


def check_distance(monster, xcoord, ycoord):
    if ((monster.x_coord - xcoord) ** 2 + (monster.y_coord - ycoord) ** 2) ** 0.5 <= 2:
        return True


all_coords = []
set_all_coords = set()


def check_identical_coordinates(monsters):
    for monster in monsters:
        all_coords.append((monster.x_coord, monster.y_coord))
        set_all_coords.add((monster.x_coord, monster.y_coord))
    if len(all_coords) == len(list(set_all_coords)):
        return True


class Game:
    def __init__(self):
        self.entities = [Rat(random.randint(1, 100), random.randint(1, 100), self),
                         Rat(random.randint(1, 100), random.randint(1, 100), self),
                         Rat(random.randint(1, 100), random.randint(1, 100), self),
                         Monster(random.randint(1, 100), random.randint(1, 100), hp=10, attack=1, game=self),
                         FireGolem(random.randint(1, 100), random.randint(1, 100), self),
                         Vampire(random.randint(1, 100), random.randint(1, 100), self),
                         ]

        while not check_identical_coordinates(self.entities):
            self.entities = [Rat(random.randint(1, 100), random.randint(1, 100), self),
                             Rat(random.randint(1, 100), random.randint(1, 100), self),
                             Rat(random.randint(1, 100), random.randint(1, 100), self),
                             Monster(random.randint(1, 100), random.randint(1, 100), hp=10, attack=1, game=self),
                             FireGolem(random.randint(1, 100), random.randint(1, 100), self),
                             Vampire(random.randint(1, 100), random.randint(1, 100), self),
                             ]

        self.is_ended = False
        self.player = Player(random.randint(1, 100), random.randint(1, 100), self)
        self.in_battle = False

    def _move_player(self):
        print("""Выберите направление:
        1.Север
        2.Юг
        3.Восток
        4.Запад
        5.Северо-восток
        6.Северо-запад
        7.Юго-восток
        8.Юго-запад""")
        command = int(input())
        if command == 1:
            self.player.move(Direction.north)
        elif command == 2:
            self.player.move(Direction.south)
        elif command == 3:
            self.player.move(Direction.east)
        elif command == 4:
            self.player.move(Direction.west)
        elif command == 5:
            self.player.move(Direction.north_east)
        elif command == 6:
            self.player.move(Direction.north_west)
        elif command == 7:
            self.player.move(Direction.south_east)
        elif command == 8:
            self.player.move(Direction.south_west)

    def get_command(self):
        while True:
            i = 1
            allowed_action = self.get_allowed_actions()
            for command in allowed_action:
                print(f"{i}. {command}")
                i += 1
            command = int(input())
            action = allowed_action[command - 1]
            if action == Commands.move:
                return self._move_player()
            elif action == Commands.hit:
                return self.player.do_magic(self.player.target)
            elif action == Commands.nothing:
                pass

    def show_info(self):
        if self.in_battle:
            print(f'Вы дерётесь с {self.player.target}')
            print(f'Ваше здоровье: {self.player.hp}')
            print(f'Ваша мана: {self.player.mana}')
            print(f'Здоровье {self.player.target}: {self.player.target.hp}')
            print(f'Мана {self.player.target}: {self.player.target.mana}')

        else:
            print('Ничего не происходит')
            print(f'Ваши координаты: {self.player.x_coord}, {self.player.y_coord}')
            for monster in self.entities:
                if check_distance(monster, xcoord=self.player.x_coord, ycoord=self.player.y_coord):
                    self.player.target = monster
                    print(f"рядом с вами находится {monster}")
                    self.in_battle = True


    def monster_actions(self):
        for monster in self.entities:
            monster.action()

    def get_allowed_actions(self):
        answer = []
        answer.append(Commands.nothing)
        if self.in_battle:
            answer.append(Commands.hit)
        else:
            answer.append(Commands.move)
        return answer

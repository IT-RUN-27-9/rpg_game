from src.incantation.superheal import SuperHeal
from src.incantation.fireball import Fireball
import random

def fight(target, player):
    print(f'На вас напал монстр {target.name}')
    while target.hp <= 0 or player.hp <= 0:
        print('Ваша очередь атаковать')
        print('1.Нанести удар')
        print('2.Использовать заклинание')
        print('3.Статистика боя')
        command = input()
        if command == 1:
            player.hit()
        elif command == 2:
            print('Выберите заклинание:'
                  '1. Великое Лечение'
                  '2. Огненный шар')
        elif command == 3:
            print(f'Ваш Текущий запас здоровья ({player.hp} / 500)'
                  f'Текущий запас здоровья врага ({target.hp})')
        else:
            print('Возникла ошибка,проверьте правильность написания команды')
            cast = input()
            if cast == 1:
                SuperHeal.cast(player, player)
                print(f'Вы используете "Великое Лечение"')
            elif cast == 2:
                Fireball.cast(target, player)
                print(f'Вы используете "Огненный Шар"')
            else:
                print('Возникла ошибка,проверьте правильность написания команды')
        print('Очередь противника атаковать')
        miss_chance_25 = random.randint(1, 4)
        if miss_chance_25 != 4:
            target.do_magic(target, player)
            print(f'Вас атаковал противник {target.name}')
        else:
            print(f'Противник {target.name} промахнулся')


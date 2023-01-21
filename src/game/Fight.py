
from Monster import Monster

def fight(self, target, player):
    print(f'На вас напал монстр(name)')
    while target.hp <= 0 or player.hp <= 0:
        print('Ваша очередь атаковать')
        print('1.Нанести удар')
        print('2.Использовать заклинание')
        command = input()
        if command = 1:
            hit()
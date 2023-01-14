print('Выберите команду')
print('1. Начать новую игру')
command = int(input())
if command != 1:
    raise Exception("Нет такой команды")
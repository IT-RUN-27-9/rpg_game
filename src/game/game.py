class Game:
    def __init__(self):
        self.entites = []
        self.is_ended = False

    def get_command(self):
        while True:
            print('Выберите действие')
            print('1. Ничего не делать')
            command = int(input())
            if command != 1:
                print('Неизвестная команда')
            return


    def show_info(self):
        print('Ничего не происходит')



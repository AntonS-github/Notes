
# Контроллер

from views import *


def run():
    while True:
        print("Введите команду из меню:\n'add', 'list', 'save', 'search', 'change', 'delete', 'exit'")
        command = input().lower()
        if check_command(command):
            execute_command(command)
        else:
            print('Данная команда отсутствует в меню, попробуйте снова.')


if __name__ == '__main__':
    run()
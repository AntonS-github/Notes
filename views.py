
# Обработка комманд из консоли

import sys
from models import *

COMMANDS = ['add', 'list', 'save', 'search', 'change', 'delete', 'exit']


def check_command(command):
    return command in COMMANDS


def execute_command(command):
    if command == 'exit':
        sys.exit()
    if command == 'add':
        add_note()
    if command == 'list':
        if list_notes():
            for el in list_notes():
                print(el)
        else:
            print('Журнал заметок пока что пуст\n')
    if command == 'save':
        save_to_file(input('Введите путь до журнала заметок: '))
    if command == 'search':
        print(search())
    if command == 'change':
        change()
    if command == 'delete':
        delete_note(int(input('Введите ID заметки, которую хотите удалить. '
                              'Если не знаете ID, то воспользуйтесь опцией list: ')))


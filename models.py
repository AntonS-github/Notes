
# Логика взаимосвязей с БД

from datetime import datetime
import json
from pathlib import Path

ALL_NOTES = []
ID_LIST = []
ID = None


# Структура заметки определяется классом

def note_dict(id, title, body):
    date_time = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    keys = ["id", "title", 'body', 'date_time']
    values = [id, title, body, date_time]
    return dict(zip(keys, values))


# Операции с заметками

def add_note():
    if len(ID_LIST) != 0:
        ID = max(ID_LIST)
    else:
        ID = 0
    ID = ID + 1
    ID_LIST.append(ID)
    title = input('Введите заголовок: ')
    body = input('Введите текст заметки: ')
    note = note_dict(ID, title, body)
    ALL_NOTES.append(note)
    print('Заметка создана, для сохранения в журнал записок выберите опцию "save"')


def save_to_file(path):
    global ALL_NOTES
    if path == '':
        path = Path('journal.json')
    with open(path, 'w+', encoding="UTF-8") as journal:
        json.dump(ALL_NOTES, journal)
    print("Журнал успешно обновлён\n")


def list_notes():
    path = Path('journal.json')
    with open(path, encoding="UTF-8") as file:
        file_content = file.read().strip()
        if not file_content:
            return None
        else:
            all_notes = json.loads(file_content)
    return all_notes


def delete_note(id):
    all_notes = list_notes()
    for note in all_notes:
        if note["id"] == id:
            all_notes.remove(note)
    print('Заметка успешно удалена')

def search():
    title = input("\nВведите заголовок заметки для поиска: ")
    isExist = False
    journal = list_notes()
    for i in range(len(journal)):
        if journal[i]['title'] == title:
            note = journal[i]
            return note
            isExist = True
    if not isExist:
        print('Заметки с таким заголовком не существует, используйте list, чтобы просмотреть весь журнал заметок\n')


def change():
    note = search()
    new_title = input("Введите новый заголовок (оставьте пустым, чтобы не вносить изменения): ")
    if not new_title == "":
        note['title'] = new_title
        note['date_time'] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    else:
        note['date_time'] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    new_body = input("Введите новый текст заметки (оставьте пустым, чтобы не вносить изменения): ")
    if not new_body == "":
        note['body'] = new_body
        note['date_time'] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    else:
        note['date_time'] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    print('Обновлённая заметка: \n', note)
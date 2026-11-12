from database import cursor, conn


def show_menu():
    print(
        "\n=====Взаимодействие с базой данных=====\n\n" \
        "-------Добавление---------------\n" \
        "1) Добавить пользователя\n" \
        "2) Добавить профиль пользователя\n" \
        "3) Добавить пользователя в проект\n" \
        "4) Добавить проект\n" \
        "5) Добавить задачу\n" \
        "-------Таблицы------------------\n" \
        "6) Показать таблицу пользователей\n" \
        "7) Показать таблицу профилей пользователей\n" \
        "8) Показать таблицу проектов\n" \
        "9) Показать таблицу задач\n" \
        "10) Показать таблицу участников проекта\n" \
        "-------Удаление-----------------\n" \
        "11) Удалить пользователя из проекта\n" \
        "12) Удалит задачу\n" \
        "-------Изменеие-----------------\n" \
        "13) Изменить статус задачи\n" \
        "14) Изменить описание проекта\n\n" \

        "=====Программа=====\n" \
        "0)Выйти\n"  
    )


def handle_db_error(error, option):
    conn.rollback()
    handle_error(error, option)


def handle_error(error, option):
    if not option is None:
        print(f'\nНе удалось выполнить операцию: "{option}"')
    if not error is None: 
        print(f'Ошибка: {error}')

    print("Операция не выполнена, повторите действие ещё раз")


def standard(word):
    return word.lower().capitalize().strip()

def compare(word):
    return word.lower().replace(" ", "")

def table_status_task():
    status_task = int(input(     
        "\n1) Новая\n" \
          "2) Выполняется\n" \
          "3) Завершена\n" \
        "Введите номер состояния задачи: "
    ))

    if status_task == 1:
        return 'Новая'
    if status_task == 2:
        return 'Выполняется'
    if status_task == 3:
        return 'Заверешна'
    else:
        handle_error(None, "Проверка корректности номера состояния задачи")
        return None


def null_string(word):
    if not word.replace(" ", ""):
        return "Не указанно"


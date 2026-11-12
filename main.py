from handler.main_functions import show_menu
from database import conn
from handler.addition import (
    add_user, 
    add_task, 
    add_project,
    add_user_profil_full,
    add_project_members_full
)
from handler.show_table import (
    show_project_meb,
    show_users,
    show_project,
    show_task,
    show_user_profiles
)
from handler.change import (
    change_status_task,
    change_description 
)
from handler.delete import (
    delete_user_from_project, 
    delete_task
)

while True:
    show_menu()

    action = int(input("Выберите действие: "))

    if action == 0:
        break
    elif action == 1:
        add_user()
    elif action == 2:
        add_user_profil_full()
    elif action == 3:
        add_project_members_full()
    elif action == 4:
        add_project()
    elif action == 5:
        add_task()
    elif action == 6:
        show_users()
    elif action == 7:
        show_user_profiles()
    elif action == 8:
        show_project()
    elif action == 9:
        show_task()
    elif action == 10:
        show_project_meb()
    elif action == 11:
        delete_user_from_project()
    elif action == 12:
        delete_task()
    elif action == 13:
        change_status_task()
    elif action == 14:
        change_description()
    else:
        print(
            "\n" \
            "Ошибка: действие не найденно\n" \
            "Попробуйте ещё раз"
        )
        continue


conn.close()
#    __
#   |  |
#   |  |
#   |  | 
# __|  |__
# \      /
#  \    /
#   \  /
#    \/
#
# Декопазиция - разбиение кода на более логически простые блоки
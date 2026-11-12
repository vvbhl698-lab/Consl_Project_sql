from handler.main_functions import (
    table_status_task,
    handle_db_error,
    null_string,
    standard,
    compare,
    cursor, 
    conn 
)
from handler.check_table import (
    check_projects, 
    check_users
)
from handler.show_table import (
    show_project,
    show_users,
)


def add_user():
    show_users()
    user_id = int(input("\nid пользователя должен быть уникальным\n" \
                        "Введите номер пользователя: "))
    name_user = standard(input("Введите имя пользователя: "))
    job_title = input("Введите должность этого ползователя: ").strip
    email_user = input("Введите электронную почту пользователя: ").strip()

    try:
        cursor.execute(
            "INSERT INTO " \
            "users(id, name, job_title, email) " \
            "VALUES(%s, %s, %s, %s)", 
            (user_id, name_user, job_title, email_user)
        )

        conn.commit()
    except Exception as error:
        handle_db_error(error, "Добавление пользователя")
        return

    question = int(input("\n" \
    "\n1) Да, конечно" \
    "\n2) Нет, откажусь" \
    "\nХотите создать профиль пользователя:"))

    if question != 1:
        return

    add_user_profil(user_id)


def add_user_profil(user_id):
    bio = github_username(input("Введтите био(необязательно): "))
    github_username = github_username(input("Введите название вашего GitHub(необязательно): "))
    
    experience_level = int(input("" \
    "\n1) Стажёр" \
    "\n2) Новичёк" \
    "\n3) Средний" \
    "\n4) Опытный" \
    "\n5) Профессионал" \
    "\nВведите номер описывающий уровень опыта пользователя:"   
    ))

    if not experience_level in [1, 2, 3, 4, 5]:
        handle_db_error(None, "Проверка корректности номера уровня опыта пользователя")
        return
    elif experience_level == 1:
        experience_level = "Стажёр"
    elif experience_level == 2:
        experience_level = "Новичёк"
    elif experience_level == 3:
        experience_level = "Средний"
    elif experience_level == 4:
        experience_level = "Опытный"
    elif experience_level == 5:
        experience_level = "Профессионал"

    try:
        cursor.execute(
            "INSERT INTO user_profiles (user_id, bio, experience_level, github_username) VALUES (%s, %s, %s, %s)",
            (user_id, bio, experience_level, github_username)
        )

        conn.commit()
    except Exception as error:
        handle_db_error(error, "Добавление профиля пользователя")
        return


def add_user_profil_full():
    show_users()

    user_name = standard(input("\nВведите имя пользователя: "))
    user_id = check_users(user_name)
    if user_id is None:
        return 

    add_user_profil(user_id)


def add_project():
    show_project()
    project_id = int(input("\nid проекта должен быть уникальным\n" \
                           "Введите id проекта: "))
    project_name = input("Введите название проекта: ").strip()
    description = null_string(input("Введите описание задачи(необязательно): "))

    try:
        cursor.execute(
            "INSERT INTO projects (id, project, description) VALUES (%s, %s, %s)", 
            (project_id, project_name, description)
        )

        conn.commit()
    except Exception as error:
        handle_db_error(error, "Добавление проекта")
        return


def add_project_members(user_id, project_id):
        try:
            cursor.execute(
                "INSERT INTO " \
                "project_members (user_id, project_id) " \
                "VALUES (%s, %s)",
                (user_id, project_id)
            )
        
            conn.commit()
        except Exception as error:
            handle_db_error(error, "Запись в таблицу project_members")
            return


def add_task():
    show_project()
    project = compare(input("\nВведите название проекта: "))

    project_id = check_projects(project)
    if project_id is None:
        return 
    
    task = input("Укажите задачу: ").strip()
    
    show_users()
    user_name = standard(input("\nВведите имя пользователя: "))

    user_id = check_users(user_name)
    if user_id is None:
        return 
    
    status_task = table_status_task()
    if status_task is None:
        return

    description = null_string(input("Введите описание задачи(необязательно): "))

    try:
        cursor.execute(
            "INSERT INTO " \
            "tasks (project_id, task, user_id, status, description) " \
            "VALUES (%s, %s, %s, %s, %s)", 
            (project_id, task, user_id, status_task, description)
        )

        conn.commit()
    except Exception as error:
        handle_db_error(error, "Добавление задачи")
        return

    add_project_members(user_id, project_id)


def add_project_members_full():
    show_project()
    project = compare(input("\nВведите название проекта: "))

    project_id = check_projects(project)
    if project_id is None:
        return 

    show_users()
    user_name = standard(input("\nВведите имя пользователя: "))
        
    user_id = check_users(user_name)
    if user_id is None:
        return 

    add_project_members(user_id, project_id)
    






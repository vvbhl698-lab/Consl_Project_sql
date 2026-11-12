from handler.main_functions import (
    handle_db_error,
    handle_error,
    compare,
    cursor,

)

def check_projects(project):
    project_id = None
    
    try:
        cursor.execute(
            "SELECT id, project " \
            "FROM projects;"
        )
    
        info = cursor.fetchall()
    
        for line in info:
            if compare(line[1]) == project:
                project_id = line[0]
    
        if project_id is None:
            handle_error(None, "Проект не найден")
            return None
    
    except Exception as error:
        handle_db_error(error, "Проверка указанный данных(project)")
        return None

    return project_id


def check_users(user_name):
    user_id = None

    try:
        cursor.execute(
            "SELECT id, name FROM  users;"
        )

        info = cursor.fetchall()

        for line in info:
            if line[1] == user_name:
                user_id = line[0]
                break

        if user_id is None:
            handle_error(None, "Пользовтель не найден")
            return None

    except Exception as error:
        handle_error(error, "Проверка указанный данных(users)")
        return None

    return user_id


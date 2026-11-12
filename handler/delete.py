from handler.main_functions import (
    handle_db_error,
    handle_error,
    standard,
    compare,
    cursor,
    conn
)
from handler.show_table import (
    show_users,
    show_task
)
from handler.check_table import (
    check_projects,
    check_users
)


def delete_user_from_project():
    show_users()
    user_name = standard(input("\nВведите имя пользователя: "))
        
    user_id = check_users(user_name)
    if user_id is None:
        return 

    try:
        cursor.execute(
            "DELETE FROM project_members WHERE user_id = %s",
            (user_id)
        )
        
    except Exception as error:
        handle_db_error(error, "Удалиение пользователя из проекта")
        return


def delete_task():
    
    show_task()
    project= compare(input("\nВведите назвниае проекта: "))
    task = compare(input("Введите задачу: "))
        
    project_id = check_projects(project)
    if project_id is None:
        return
        
    try:
        cursor.execute(
            "SELECT project_id, task " \
            "FROM tasks;"
        )
        
        info = cursor.fetchall()
        
        task_found = False
        for line in info:
            if line[0] == project_id and compare(line[1]) == task:
                cursor.execute(
                    "DELETE FROM tasks WHERE project_id = %s AND task = %s", 
                    (project_id, line[1])
                )
                task_found = True
                break
                
        if task_found is False:
            handle_error(None, "Задача не найдена")
            return
        else:
            conn.commit()
                
    except Exception as error:
        handle_error(error, "Проверка указанный данных")
        return
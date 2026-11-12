from handler.show_table import (
    show_project,
    show_task
)
from handler.main_functions import (
    table_status_task,
    handle_db_error,
    handle_error,
    compare,
    cursor, 
    conn
)
from handler.check_table import (
    check_projects
)

def change_status_task():
    show_task()
    project= compare(input("\nВведите назвниае проекта: "))
    task = compare(input("Введите задачу: "))

    project_id = check_projects(project)
    if project_id is None:
        return

    status_task = table_status_task()
    if status_task is None:
        return

    try:
        cursor.execute(
            "SELECT " \
                "project_id, " \
                "task " \
            "FROM tasks;"
        )

        info = cursor.fetchall()

        task_found = False
        for line in info:
            if line[0] == project_id and compare(line[1]) == task:
                cursor.execute(
                    "UPDATE tasks " \
                    "SET status = %s " \
                    "WHERE project_id = %s AND task = %s", 
                    (status_task, project_id, line[1])
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

def change_description():
    show_project()
    project = compare(input("\nВведите название проекта: "))

    project_id = check_projects(project)
    if project_id is None:
        return

    description = input("Введите описание: ")
     
    try:
        cursor.execute(
            "UPDATE projects " \
            "SET description = %s " \
            "WHERE id = %s", 
            (description, project_id)
        )

        conn.commit()
    except Exception as error:
        handle_db_error(error, "Изменение опиясания проекта")
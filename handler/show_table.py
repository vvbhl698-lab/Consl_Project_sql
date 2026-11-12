import textwrap
from handler.main_functions import (
    handle_error,
    cursor
)


def show_users():
    try:
        cursor.execute(
            "SELECT * FROM users;"
        )

        table = cursor.fetchall()


        print(
            "\n" +
            " id"       + " " * 8  + " | " + 
            "name"      + " " * 26 + " | " + 
            "job_title" + " " * 21 + " | " + 
            "email"     + " " * 25 + " | " + 
            "data"
            )
        
        print(
            '-' * 12 + "+" + 
            '-' * 32 + "+" +
            '-' * 32 + "+" + 
            '-' * 32 + "+" + 
            '-' * 32
            )

        for line in table:
            print(
                " " + 
                str(line[0]).ljust(10) + " | " +
                str(line[1]).ljust(30) + " | " +
                str(line[2]).ljust(30) + " | " +
                str(line[3]).ljust(30) + " | " +
                str(line[4]).ljust(30)
            )

    except Exception as error:
        handle_error(error, "Ввывод таблицы users")


def show_user_profiles():
    try:
        cursor.execute(
            "SELECT " \
                "user_profiles.id, " \
                "users.name, " \
                "user_profiles.bio, " \
                "user_profiles.experience_level, " \
                "user_profiles.github_username " \
            "FROM user_profiles " \
            "JOIN users " \
                "ON user_profiles.user_id = users.id;"
        )

        table = cursor.fetchall() 

        print(
            "\n" +
            " id"       + " " * 8  + " | " + 
            "name"      + " " * 26 + " | " + 
            "job_title" + " " * 21 + " | " + 
            "email"     + " " * 25 + " | " + 
            "data"
            )
        
        print(
            '-' * 12 + "+" + 
            '-' * 32 + "+" +
            '-' * 32 + "+" + 
            '-' * 32 + "+" + 
            '-' * 32
            )
            
        for line in table:
            bio_parts = textwrap.wrap(str(line[2]), width=30)
            
            for i, bio in enumerate(bio_parts): 
                # i - индекс строчки bio_parts
                # bio - сама строка
                if i == 0:
                    # для первой строки
                    print(
                        " " +
                        str(line[0]).ljust(10) + " | " +
                        str(line[1]).ljust(30) + " | " +
                        bio.ljust(30)          + " | " +
                        str(line[3]).ljust(30) + " | " +
                        str(line[4]).ljust(30)
                    )
                else:
                    # если строк больше чем одна
                    print(
                        " " +
                        "".ljust(10)  + " | " +
                        "".ljust(30)  + " | " +
                        bio.ljust(30) + " | " +
                        "".ljust(30)  + " | " +
                        "".ljust(30)
                    )

    except Exception as error:
        handle_error(error, "Вывод таблицы user_profiles")


def show_project():
    try:
        cursor.execute(
            "SELECT * FROM projects;"
        )

        table = cursor.fetchall()


        print(
            "\n" + 
            " id"         + " " * 8  + " | " + 
            "project"     + " " * 23 + " | " + 
            "description" + " " * 19 + " | " + 
            "data" 
            )
        
        print(
            '-' * 12 + "+" + 
            '-' * 32 + "+" + 
            '-' * 32 + "+" + 
            '-' * 32
            )

        for line in table:
            description_parts = textwrap.wrap(str(line[2]), width=30)
            for i, description in enumerate(description_parts): 

                if i == 0:
                    print(
                        " " + 
                        str(line[0]).ljust(10)   + " | " +
                        str(line[1]).ljust(30)   + " | " +
                        description.ljust(30)    + " | " +
                        str(line[3]).ljust(30)
                    )
                else:
                    print(
                        " " + 
                        "".ljust(10)             + " | " +
                        "".ljust(30)             + " | " +
                        description.ljust(30)    + " | " +
                        "".ljust(30)
                    )

    except Exception as error:
        handle_error(error, "Ввывод таблицы projects")


def show_task():
    try:
        cursor.execute(
            "SELECT " \
                "tasks.id, " \
                "projects.project, " \
                "tasks.task, " \
                "users.name, " \
                "tasks.status, " \
                "tasks.description, " \
                "tasks.created_at "
            "FROM tasks " \
            "JOIN projects " \
                "ON tasks.project_id = projects.id " \
            "JOIN users " \
                "ON tasks.user_id = users.id;"
        )

        table = cursor.fetchall()

        print("\n" + 
              " id"         + " " * 8  + " | " + 
              "project"     + " " * 13 + " | " + 
              "task"        + " " * 16 + " | " + 
              "name"        + " " * 16 + " | " + 
              "status"      + " " * 9  + " | " +
              "description" + " " * 19 + " | " +
              "data"        
        )
        print(
            "-" * 12 + "+" + 
            "-" * 22 + "+" + 
            "-" * 22 + "+" + 
            "-" * 22 + "+" + 
            "-" * 17 + "+" +
            "-" * 32 + "+" + 
            "-" * 32 
            )

        for line in table:
            description_parts = textwrap.wrap(str(line[5]), width=30)
            for i, description in enumerate(description_parts): 
                if i == 0:
                    print(
                        " " +
                        str(line[0]).ljust(10) + " | " +
                        str(line[1]).ljust(20) + " | " +
                        str(line[2]).ljust(20) + " | " +
                        str(line[3]).ljust(20) + " | " +
                        str(line[4]).ljust(15) + " | " + 
                        description.ljust(30)  + " | " +
                        str(line[6]).ljust(30)               
                    )
                else:
                    print(
                        " " + 
                        "".ljust(10)           + " | " +
                        "".ljust(20)           + " | " +
                        "".ljust(20)           + " | " +
                        "".ljust(20)           + " | " +
                        "".ljust(15)           + " | " + 
                        description.ljust(30)  + " | " +
                        "".ljust(30)               
                    )


    except Exception as error:
        handle_error(error, "Вывод таблицы tasks")


def show_project_meb():
    show_project()
    project_id = int(input("\nВведите номер проекта: "))

    try:
        cursor.execute(
            "SELECT " \
                "project_members.id, " \
                "users.name, " \
                "projects.project," \
                "project_members.created_at "
            "FROM project_members " \
            "JOIN users " \
                "ON project_members.user_id = users.id "
            "JOIN projects " \
                "ON project_members.project_id = projects.id "
            "WHERE project_id = %s", 
            (project_id,)
        )

        table = cursor.fetchall()

        print(
            "\n" + 
            " id"     + " " * 8  + " | " +
            "name"    + " " * 16 + " | " +
            "project" + " " * 13 + " | " + 
            "data"    + " " * 26
        )
        print(
            "-" * 12 + "+" +
            "-" * 22 + "+" +
            "-" * 22 + "+" +
            "-" * 32 
            )

        for line in table:
            print(
                " " +
                str(line[0]).ljust(10) + " | " +
                str(line[1]).ljust(20) + " | " +
                str(line[2]).ljust(20) + " | " +
                str(line[3]).ljust(30)
                )

    except Exception as error:
        handle_error(error, "Вывод таблицы project_members")
        return
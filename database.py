import psycopg
from os import getenv
from dotenv import load_dotenv

load_dotenv()

try:
    # Подключение к базе данных
    conn = psycopg.connect(
        dbname=getenv("DBNAME"),
        user=getenv("NAME"),
        password=getenv("PASSWORD"),
        host="127.0.0.1",
        port=5432
    )

except Exception as error:
    print("Ошибка: Неудалось подключиться к базе данных")
    print(f"Ошибка {error}")
    exit(1)

cursor = conn.cursor()
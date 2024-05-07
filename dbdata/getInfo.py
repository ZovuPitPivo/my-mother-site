import psycopg2
from psycopg2 import Error


async def get_main_data():
    try:
        conn = psycopg2.connect(dbname="my-mother-site",
                                user="postgres",
                                password="aza_967.",
                                host="localhost",
                                port="5432")
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM "about-page"''')
        data = cursor.fetchall()
        return data
    except (Exception, Error) as error:
        return f"Ошибка при работе с Postgres: {error}"
    finally:
        if conn:
            cursor.close()
            conn.close()
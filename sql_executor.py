import mysql.connector
from mysql.connector import Error


DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "root123",      # Change if your MySQL password is different
    "database": "HRAnalytics"
}


def get_connection():
    return mysql.connector.connect(**DB_CONFIG)


def run_query(sql):

    conn = None
    cursor = None

    try:

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(sql)

        if cursor.description:

            columns = [col[0] for col in cursor.description]

            rows = cursor.fetchall()

            return columns, rows

        else:

            conn.commit()

            return [], []

    except Error as e:

        raise Exception(f"MySQL Error: {e}")

    finally:

        if cursor is not None:
            cursor.close()

        if conn is not None and conn.is_connected():
            conn.close()
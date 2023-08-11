import pymysql
from pymysql import cursors
from django.db import connection
from back import settings


class MySQLDatabase:
    def __init__(self):
        try:
            db_info = settings.DATABASES.get("default")
            print(db_info)
            db_name = db_info["NAME"]
            self.connection = pymysql.connect(
                host=db_info["HOST"],
                port=db_info["PORT"],
                user=db_info["USER"],
                password=db_info["PASSWORD"],
                db=db_name,
                charset="utf8mb4",
                cursorclass=cursors.DictCursor,
                local_infile=True
            )
        except Exception as e:
            print("Error while __init__:", e)

    def execute_query(self, query, params=None):
        try:
            with self.connection.cursor() as cursor:
                if "SELECT" == query.strip()[:6].upper():
                    cursor.execute(query, params)
                    res = cursor.fetchall()
                elif type(params) is list:
                    res = cursor.executemany(query, params)
                else:
                    res = cursor.execute(query, params)
                self.commit()
                return res
        except pymysql.Error as e:
            print("Error while executing query:", e)
            self.rollback()
            raise

    def commit(self):
        try:
            self.connection.commit()
        except Exception as e:
            print("Error while commit:", e)

    def rollback(self):
        try:
            self.connection.rollback()
        except Exception as e:
            print("Error while rollback:", e)

    def close(self):
        try:
            if self.connection:
                self.connection.close()
                print("Connection to MySQL database closed")
        except Exception as e:
            print("Error while close:", e)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


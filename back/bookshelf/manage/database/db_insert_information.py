from .common_database import MySQLDatabase


def insert_new_book(**kwargs):
    db = MySQLDatabase()
    sql = """
    select * from book_shelf
    """
    res = db.execute_query(sql)
    print(res)
    db.close()
    # dbに接続する処理が必要
    print("insert_new_book")
    print(kwargs)


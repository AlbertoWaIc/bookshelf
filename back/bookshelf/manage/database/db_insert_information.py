from .common_database import MySQLDatabase
from datetime import datetime


def select_bookshelf():
    db = MySQLDatabase()
    sql = """
        select 
            pics_path as src,
            title,
            author,
            category,
            user_review as star,
            book_text as wrap_up_text,
            user_summary as summary
               from book_shelf where delete_flg = 0
    """
    res = db.execute_query(sql)
    print(res)
    db.close()
    return res


def insert_new_book(**kwargs):
    # 現在の日時を取得
    current_datetime = datetime.now()
    # フォーマットを指定して文字列に変換
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    db = MySQLDatabase()
    # INSERT文の作成
    sql = """INSERT INTO book_shelf 
                 (title, author, pub_date, pages, book_text, pics_path, user_summary, user_review, category, ins_date, upd_date, delete_flg) 
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    # クエリの実行
    values = (
        kwargs["title"],
        kwargs["author"],
        kwargs["pub_date"],
        kwargs["pages"],
        kwargs["book_text"],
        kwargs["pics_path"],
        kwargs["user_summary"],
        kwargs["user_review"],
        "0",
        formatted_datetime,
        formatted_datetime,
        "0",
    )
    res = db.execute_query(sql, values)
    print(res)
    db.close()


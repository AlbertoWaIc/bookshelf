from .common_database import MySQLDatabase
from datetime import datetime
import re


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

    if is_valid_year_month_format(kwargs["pub_date"]):
        kwargs["pub_date"] = get_first_day_of_month(kwargs["pub_date"])
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


def is_valid_year_month_format(year_month_str):
    # 正規表現で 'YYYY-MM' 形式かどうかを判別
    pattern = re.compile(r'^\d{4}-\d{2}$')
    return bool(pattern.match(year_month_str))


def get_first_day_of_month(year_month_str):
    # 年月の文字列を datetime オブジェクトに変換
    year_month = datetime.strptime(year_month_str, '%Y-%m')

    # 月の初日を求める
    first_day_of_month = datetime(year_month.year, year_month.month, 1)

    return first_day_of_month


def select_wordcloud_text(target):
    db = MySQLDatabase()
    # タイトル: 0,
    # 概要: 1,
    # 著者: 2,
    # 本の感想: 3,
    print(target)
    if target == "タイトル":
        element = "title"
    elif target == "概要":
        element = "book_text"
    elif target == "著者":
        element = "author"
    elif target == "本の感想":
        element = "user_summary"
    else:
        element = "*"
        
    sql = f"select {element} from book_shelf where delete_flg = 0"
    res = db.execute_query(sql)
    combined_summary = ' '.join([item[element] for item in res])
    print(combined_summary)
    db.close()
    return combined_summary
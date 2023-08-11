import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ..database import db_insert_information
from ...manage import utils


@csrf_exempt
def register_new_book(requests):
    param = json.loads(requests.body)
    book_item = param.get('book_item', [])
    user_review = param.get('user_review', 0)
    # 画面側でユーザーが感想を入力する処理が必要
    user_summary = param.get('user_summary', "")
    context = {}
    # リクエストの存在チェック
    if not book_item or len(book_item) < 1:
        context["success"] = 0
        context["error_msg"] = "書籍情報を取得できませんでした"
        return JsonResponse(context, safe=False)

    # 登録情報の存在チェックとデータ整形
    reg_info = check_book_info(book_item, user_review, user_summary)

    # dbに書籍情報を登録
    db_insert_information.insert_new_book(**reg_info)
    return JsonResponse(context, safe=False)


def check_book_info(book_item, user_review, user_summary):
    # テキストの文字数を確認
    title = book_item.get("text", "")
    title = utils.truncate_text_for_char(title)
    # 著者の情報をデータ成型
    author_list = book_item.get("author", "")
    author_item = ", ".join(author_list)
    author_item = utils.truncate_text_for_char(author_item)
    # 日付がdate型か確認する
    pub_date = book_item.get("pub_date", "")
    if type(pub_date) is str:
        pub_date = utils.string_to_date_type(pub_date)
    # テキストの文字数を確認
    text = book_item.get("text", "")
    text = utils.truncate_text_for_char(text)
    # DBに登録するデータ
    ins_item = {
        "title": title,
        "author": author_item,
        "pub_date": pub_date,
        "pages": book_item.get("pages", 0),
        "book_text": text,
        "pics_path": book_item.get("pics", ""),
        "user_summary": user_summary,
        "user_review": user_review
    }
    return ins_item

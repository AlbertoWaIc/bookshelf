import json
import xmltodict
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests

@csrf_exempt
def search_book_by_camera(requests):
    print("search_book_by_camera")

    # ここの処理は共通化したい
    param = json.loads(requests.body)
    barcode_data = param.get('barcodeData', '')
    isbn = param.get("isbn", '')

    context = {}
    book_item_init = create_context()

    try:
        # OPEN DBで検索（https://openbd.jp/）
        endpoint = "https://api.openbd.jp/v1/get"
        headers = {}
        params = {
            "isbn": barcode_data
        }
        result = send_book_requests(endpoint, params, headers)
        res = result.json()
        if res:
            book_item = input_book_info_open_db(book_item_init, res)
            context["book_info"] = book_item

        else:
            # 国立国会図書館サーチ(NDL Search)
            endpoint = 'https://iss.ndl.go.jp/api/sru'
            params = {'operation': 'searchRetrieve',
                      'query': f'isbn="{barcode_data}"',
                      'recordPacking': 'xml'}
            result = send_book_requests(endpoint, params)  # XMLファイルの処理
            xml_data = result.text  # xml読み込み
            res = xmltodict.parse(xml_data)  # xml → dict
            book_item = input_book_info_ndls(book_item_init, res, isbn)
            context["book_info"] = book_item

        context["success"] = 1

    except Exception as err:
        print("Errorが発生" + err)
        context["success"] = 0
        context["error"] = "見つかりませんでした。"
        # 英語図書に有効　優先度低
        # Open Library APIから本の情報を取得
        # url = f"http://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data"
        # response = urllib.request.urlopen(url)
        # data = json.loads(response.read().decode('utf-8'))  # HTTPレスポンスオブジェクトを文字列に変換
        # 取得した情報を表示
        #     print(data)
        #     print(data[f"ISBN:{isbn}"]["title"])
        #     print(data[f"ISBN:{isbn}"]["authors"][0]["name"])
        #     print(data[f"ISBN:{isbn}"]["publish_date"])
        #     print("--------------------------------------------------")
    print(context)
    return JsonResponse(context, safe=False)


def send_book_requests(endpoint, params, headers=None):
    # headersでエラーになったら分岐処理を入れる。
    result = requests.get(endpoint, params=params, headers=headers)
    return result


def create_context():
    return {
        "author": "",     # 著者
        "category": "",   # カテゴリ
        "isbn": "",       # ISBN
        "pics": "",       # 画像
        "pub_date": "",   # 出版日
        "publisher": "",  # 出版社
        "reviewer": "",   # レビュアー
        "title": "",      # タイトル
        "text": "",       # テキスト
    }


def input_book_info_open_db(book_item_init, res):
    book_item_init["author"] = res[0]["summary"].get("author")
    # context["category"] = res[0]["summary"].get("")
    book_item_init["isbn"] = res[0]["summary"].get("isbn")
    book_item_init["pics"] = res[0]["summary"].get("cover")
    book_item_init["pub_date"] = res[0]["summary"].get("pubdate")
    book_item_init["publisher"] = res[0]["summary"].get("publisher")
    book_item_init["reviewer"] = res[0]["hanmoto"]["reviews"][0].get("reviewer")
    book_item_init["title"] = res[0]["summary"].get("title")
    book_item_init["text"] = res[0]["onix"]["CollateralDetail"]["TextContent"][0].get("Text")
    return book_item_init


def input_book_info_ndls(book_item_init, res, isbn):
    book_item_init["author"] = res["searchRetrieveResponse"]["records"]["record"][7]["recordData"]["srw_dc:dc"]["dc:creator"]
    # context["category"] = res
    book_item_init["isbn"] = isbn
    book_item_init["pics"] = ""
    book_item_init["pub_date"] = res["searchRetrieveResponse"]["records"]["record"][0]["recordData"]["srw_dc:dc"]["dc:description"]
    book_item_init["publisher"] = res["searchRetrieveResponse"]["records"]["record"][7]["recordData"]["srw_dc:dc"]["dc:publisher"]
    book_item_init["reviewer"] = ""
    book_item_init["title"] = res["searchRetrieveResponse"]["records"]["record"][7]["recordData"]["srw_dc:dc"]["dc:title"]
    book_item_init["text"] = res["searchRetrieveResponse"]["records"]["record"][7]["recordData"]["srw_dc:dc"]["dc:subject"]
    return book_item_init

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
        print(res)
        if res:
            book_items = input_book_info_open_db(book_item_init, res)
            context["book_info"] = book_items
            print(context["book_info"])

        else:
            # 国立国会図書館サーチ(NDL Search)
            endpoint = 'https://iss.ndl.go.jp/api/sru'
            params = {'operation': 'searchRetrieve',
                      'query': f'isbn="{barcode_data}"',
                      'recordPacking': 'xml'}
            result = send_book_requests(endpoint, params)  # XMLファイルの処理
            xml_data = result.text  # xml読み込み
            res = xmltodict.parse(xml_data)  # xml → dict
            book_items = input_book_info_ndls(book_item_init, res, isbn)
            context["book_info"] = book_items

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
    return JsonResponse(context, safe=False)


def send_book_requests(endpoint, params, headers=None):
    result = requests.get(endpoint, params=params, headers=headers)
    return result


def create_context():
    return [{
        "author": "",     # 著者
        "category": "",   # カテゴリ
        "isbn": "",       # ISBN
        "pages": "",      # ページ数
        "pics": "",       # 画像
        "pub_date": "",   # 出版日
        "publisher": "",  # 出版社
        "reviewer": "",   # レビュアー
        "title": "",      # タイトル
        "text": "",       # テキスト
    }]


def input_book_info_open_db(book_item_init, res):
    book_item_init[0]["author"] = res[0]["summary"].get("author")
    # context["category"] = res[0]["summary"].get("")
    book_item_init[0]["isbn"] = res[0]["summary"].get("isbn")
    book_item_init[0]["pics"] = res[0]["summary"].get("cover")
    book_item_init[0]["pub_date"] = res[0]["summary"].get("pubdate")
    book_item_init[0]["publisher"] = res[0]["summary"].get("publisher")
    # book_item_init[0]["reviewer"] = res[0]["hanmoto"]["reviews"][0].get("reviewer")
    book_item_init[0]["title"] = res[0]["summary"].get("title")
    book_item_init[0]["text"] = res[0]["onix"]["CollateralDetail"]["TextContent"][0].get("Text")
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


def input_book_info_google_books(res):
    book_item_init = []
    for index, item in enumerate(res["items"]):
        book_item = {}
        book_item["author"] = item["volumeInfo"].get("authors", [])if "authors" in item["volumeInfo"] else ""
        book_item["category"] = item["volumeInfo"].get("categories", [])if "categories" in item["volumeInfo"] else ""
        book_item["isbn"] = item["volumeInfo"].get("industryIdentifiers", [])[0].get("identifier", "")if "industryIdentifiers" in item["volumeInfo"] else ""
        book_item["pages"] = item["volumeInfo"].get("pageCount", "")if "pageCount" in item["volumeInfo"] else ""
        book_item["pics"] = item["volumeInfo"]["imageLinks"].get("thumbnail", "")if "imageLinks" in item["volumeInfo"] else ""
        book_item["pub_date"] = item["volumeInfo"].get("publishedDate", "")if "publishedDate" in item["volumeInfo"] else ""
        book_item["title"] = item["volumeInfo"].get("title", "")if "title" in item["volumeInfo"] else ""
        book_item["text"] = item["volumeInfo"].get("description", "")if "description" in item["volumeInfo"] else ""
        book_item_init.append(book_item)
    return book_item_init


@csrf_exempt
def search_book_by_keyword(requests):
    param = json.loads(requests.body)
    keyword = param.get('keyword', '')

    context = {}
    base_url = 'https://www.googleapis.com/books/v1/volumes'
    params = {
        'q': keyword,
        'maxResults': 15
    }
    try:
        response = send_book_requests(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            book_items = input_book_info_google_books(data)
            # print(book_items)
            context["book_info"] = serialize_book_data_for_front_end(book_items)
        else:
            context["book_info"] = []
        context["success"] = 1
    except Exception as err:
        print("Errorが発生" + err)
        context["success"] = 0
        context["error"] = "見つかりませんでした。"

    return JsonResponse(context, safe=False)


def serialize_book_data_for_front_end(book_items):
    # バーコード検索、キーワード検索でkeyが統一されていなければここで統一してもいい
    result_list = []
    if book_items is None or len(book_items) < 1:
        return result_list
    for index, item in enumerate(book_items):
        print(index)
        print(item)
    return book_items

"""
ログイン関係の処理を記載
・メールアドレスの照合
・パスワードの照合
・ログイン処理（ログ取得）
"""
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login_api(requests):
    print("login_api")
    param = json.loads(requests.body)
    mail = param.get('mail', '')
    password = param.get("password", '')
    error_flg = 1
    if mail == "" or password == "":
        context = {"error": error_flg}
        return JsonResponse(context, safe=False)
    # DBと接続して値の取得
    # 一致しているものが取得できれば成功した情報を返す、失敗したフラグを返す
    context = {"success": 1}
    return JsonResponse(context, safe=False)


@csrf_exempt
def register_new_account(requests):
    print("registar_new_account")
    param = json.loads(requests.body)
    mail = param.get('mail', '')
    password = param.get("password", '')
    error_flg = 1
    if mail == "" or password == "":
        context = {"error": error_flg}
        return JsonResponse(context, safe=False)
    # DBと接続してユーザー情報を登録
    # 一致しているものが取得できれば成功した情報を返す、失敗したフラグを返す
    context = {"success": 1}
    return JsonResponse(context, safe=False)


@csrf_exempt
def check_user_mail(requests):
    print("check_user_mail")
    param = json.loads(requests.body)
    mail = param.get('mail', '')
    error_flg = 1
    if mail == "":
        context = {"error": error_flg}
        return JsonResponse(context, safe=False)
    # DBと接続してユーザーメールがあればOK
    # 一致しているものが取得できれば成功した情報を返す、失敗したフラグを返す
    context = {"success": 1,
               "user_id": 1}
    return JsonResponse(context, safe=False)


@csrf_exempt
def register_new_password(requests):
    print("register_new_password")
    param = json.loads(requests.body)
    user_id = param.get('userId', '')
    password = param.get("password", '')
    context = {}
    error_flg = 1
    if user_id == "" or password == "":
        context = {"error": error_flg}
        return JsonResponse(context, safe=False)
    # user_idからユーザーのパスワードを変更する。
    return JsonResponse(context, safe=False)

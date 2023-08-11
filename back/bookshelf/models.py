from django.db import models

# models.pyを更新したらマイグレーションファイルを作成するために次のコマンドを実行する
# python manage.py makemigrations bookshelf
# マイグレーションファイルをDBに反映させる
# python manage.py migrate bookshelf
# Create your models here.
class BookShelf(models.Model):
    id = models.AutoField(null=False, unique=True, primary_key=True)
    title = models.CharField(null=False, max_length=256)
    author = models.CharField(null=False, max_length=256)
    pub_date = models.DateField(blank=True)
    category = models.IntegerField(null=False, default=0)
    pages = models.IntegerField(default=0)
    book_text = models.CharField(max_length=256, blank=True)
    pics_path = models.CharField(max_length=256, blank=True)
    user_summary = models.TextField(blank=True)
    user_review = models.IntegerField(default=0)
    ins_date = models.DateField(auto_now=True)
    upd_date = models.DateField(auto_now_add=True)
    # reg_user = models.IntegerField(null=False)
    delete_flg = models.IntegerField(default=0)

    class Meta:
        db_table = "book_shelf"

# class UserInfo(models.Model):
#     id = models.AutoField(null=False)
#     user_name = models.CharField(max_length=50)
#     ins_date = models.DateField(auto_now=True)
#     delete_flg = models.IntegerField(default=0)
#     class Meta:
#         db_table = "user_info"

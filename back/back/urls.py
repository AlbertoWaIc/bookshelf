"""
URL configuration for back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bookshelf.manage.login import login
from bookshelf.manage.book import read_barcode, book_wordcloud

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/loginApi', login.login_api, name='login_api'),
    path('login/registerNewAccount', login.register_new_account, name='register_new_account'),
    path('login/checkUserMail', login.check_user_mail, name='check_user_mail'),
    path('login/registerNewPassword', login.register_new_password, name='register_new_password'),
    path('book/searchBookByCamera', read_barcode.search_book_by_camera, name='search_book_by_camera'),
    path('book/searchBookByKeyword', read_barcode.search_book_by_keyword, name='search_book_by_keyword'),
    path('book/createWordcloud', book_wordcloud.create_wordcloud, name='create_wordcloud'),
]

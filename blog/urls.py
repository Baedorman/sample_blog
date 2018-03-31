from django.urls import path
from . import views # 점을 찍으면 같은 폴더에 접근할 거라는 것

urlpatterns = [
    path('', views.index, name='index'),
    #view라는 파일 안에 index를 찍어서 불러온다
]

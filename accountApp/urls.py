from django.urls import path, include

from accountApp.views import hello_world

app_name = "accountApp"     # 앱 이름 생성
urlpatterns = [
    path('hello_world/', hello_world, name='hello_world')       # 주소, 사용할 뷰, 라우트에 대한 이름 지정
]
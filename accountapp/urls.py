from django.urls import include, path
from accountapp.views import hello_world

app_name = "accountapp"  # 이 앱의 이름을 정해줌 / 나중에 경로를 일일히 안쳐도 되게 해줌

urlpatterns = [
    path('hello_world/',hello_world)  # hello_world라는 주소로 접속하면 hello_world라는 view를 사용해라
]
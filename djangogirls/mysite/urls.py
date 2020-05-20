from django.contrib import admin
from django.urls import path, include

# local host로 들어오는 모든 접속 요청을 blog.urls로 전송해 추가 명령을 찾는다.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
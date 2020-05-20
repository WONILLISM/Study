from django.urls import path        # 장고 함수
from . import views     
  

urlpatterns = [
    path('', views.post_list, name='post_list'),    # 주로 들어왔을 때 views.post_list를 보여주라고 말해준다.
]
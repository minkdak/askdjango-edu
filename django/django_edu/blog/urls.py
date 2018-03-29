from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list), # ^문자열 시작 $ 문자열 끝 => 최상위 경로
                                #함수를 호출한 것이 아니라 함수 자체를 넘겨줌.
]

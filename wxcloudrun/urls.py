import views
from django.conf.urls import url

from django.urls import path
from views import SimpleLoginView

urlpatterns = (
    # 计数器接口
    url(r'^^api/count(/)?$', views.counter),

    # 获取主页
    url(r'(/)?$', views.index),
    path('login/', SimpleLoginView.as_view(), name='simple_login'),

)

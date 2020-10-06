from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.index, name='index'),
    url('<int:post_id>/', views.post, name='post'),
]


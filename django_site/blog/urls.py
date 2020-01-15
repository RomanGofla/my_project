from django.urls import path
from . import views

urlpatterns = [
    path('<slug>', views.article_detail, name='detail'),
    #re_path('(?P<slug>[\w-]+)/$', views.article_detail, name='detail'),
    path('', views.article_list, name='list'),
]
from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.article_create, name='create'),
    path('', views.article_list, name='list'),
    path('<slug>', views.article_detail, name='detail'),
]
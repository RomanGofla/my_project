from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('', include('blog.urls')),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
]

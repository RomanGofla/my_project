from django.contrib import admin
from django.urls import include, path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('index/', views.index),
    path('', include('blog.urls')),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
]


urlpatterns += staticfiles_urlpatterns()

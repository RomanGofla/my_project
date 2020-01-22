from django.contrib import admin
from django.urls import include, path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('index/', views.index),
    path('accounts/', include('accounts.urls')),
    path('', include('blog.urls')),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('um.urls')),

<<<<<<< HEAD
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 137d0f08509a2b46bb25de8a6260b8d467133386

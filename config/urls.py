from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# Forma vieja
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', home,  name="index")
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
     path('auth/',  include('autenticacion.urls')),
] 

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
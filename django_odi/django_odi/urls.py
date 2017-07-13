from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'', include('odi.urls', namespace='odi'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from photos.views import index, about, contact, trees, city, portraits, animals, gallery

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^gallery/', gallery, name='gallery'),
    url(r'^about/', about, name='about'),
    url(r'^contact/', contact, name='contact'),
    url(r'^trees/', trees, name='trees'),
    url(r'^city/', city, name='city'),
    url(r'^portraits/', portraits, name='portraits'),
    url(r'^animals/', animals, name='animals')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

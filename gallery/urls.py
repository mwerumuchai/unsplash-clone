from django.conf.urls import url, include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.new_photos,name = 'newPhotos'),
    url(r'^trending/(\d{4}-\d{2}-\d{2})/$',views.trending_photos,name = 'trendingPhotos'),
    url(r'^search/', views.search_results, name = 'search_results'),
    url(r'^tag/(\d+)', views.tags, name = 'tag'),
    url(r'^gallery/(\d+)',views.new_photos,name='gallery')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

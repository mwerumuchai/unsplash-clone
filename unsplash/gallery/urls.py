from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.welcome,name = 'welcome'),
    url('^new/$', views.new_photos,name = 'newPhotos'),
    url(r'^trending/(\d{4}-\d{2}-\d{2})/$',views.trending_photos,name = 'trendingPhotos')
]

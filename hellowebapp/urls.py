from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
   url(r'^$', 'collection.views.index', name='home'),
   url(r'^admin/', admin.site.urls),
]

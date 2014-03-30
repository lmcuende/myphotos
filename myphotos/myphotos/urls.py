from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^$','mainapp.views.home'),
    url(r'^users/$','mainapp.views.users'),
    url(r'^photos/$','mainapp.views.list_photos'),
    url(r'^about/$','mainapp.views.about'),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
)

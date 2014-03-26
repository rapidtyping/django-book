from django.conf.urls import patterns, include, url
from .views import hora_actual, hora_actual2
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^h1/', 'apps.cap4.views.hora_actual'),
    url(r'^h2/', 'apps.cap4.views.hora_actual2'),
    url(r'^h3/', 'apps.cap4.views.hora_actual3'),
    url(r'^h4/', 'apps.cap4.views.hora_actual4'),
    url(r'^h5/', 'apps.cap4.views.hora_actual5'),
    url(r'^h6/', 'apps.cap4.views.hora_actual6'),
)

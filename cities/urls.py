from django.conf.urls import patterns, url
from cities import views

urlpatterns = patterns('',
    url(r'^view_one/', 'cities.views.view_one'),
    url(r'^view_two/', 'cities.views.view_two'),
)

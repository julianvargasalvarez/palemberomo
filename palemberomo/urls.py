from django.conf.urls import patterns, include, url
from taremcalupi.views import HomeController, AlgoController

urlpatterns = patterns('',
    url(r'^$', HomeController.as_view(), name='home'),
    url(r'^algo/$', AlgoController.as_view(), name='algo'),
)

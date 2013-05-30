from django.conf.urls import patterns, include, url
from taremcalupi.views import UserCreate, UserUpdate, UserDelete, UserList

urlpatterns = patterns('',
    url(r'^$', UserList.as_view(), name='user_list'),
    url(r'user/add/$', UserCreate.as_view(), name='user_add'),
    url(r'user/(?P<pk>\d+)/$', UserUpdate.as_view(), name='user_update'),
    url(r'user/(?P<pk>\d+)/delete/$', UserDelete.as_view(), name='user_delete'),
)

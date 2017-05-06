from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^postavke/$', views.PostavkaListView.as_view(), name='postavke'),
    url(r'^postavka/(?P<pk>\d+)$', views.PostavkaDetailView.as_view(), name='postavka-detail'),
    url(r'^popisi/$', views.PopisListView.as_view(), name='popisi'),
    url(r'^popis/(?P<pk>\d+)$', views.PopisDetailView.as_view(), name='popis-detail'),
]

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^postavke/$', views.PostavkaListView.as_view(), name='postavke'),
    url(r'^postavka/(?P<pk>\d+)$', views.PostavkaDetailView.as_view(), name='postavka-detail'),
]

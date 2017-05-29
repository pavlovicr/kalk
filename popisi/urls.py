from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^postavke/$', views.PostavkaListView.as_view(), name='postavke'),
    url(r'^postavka/(?P<pk>\d+)$', views.PostavkaDetailView.as_view(), name='postavka-detail'),
    url(r'^specifikacije/$', views.SpecifikacijaListView.as_view(), name='specifikacije'),
    url(r'^specifikacija/(?P<pk>\d+)$', views.SpecifikacijaDetailView.as_view(), name='specifikacija-detail'),
    url(r'^popisne_postavke/$', views.PopisnaPostavkaListView.as_view(), name='popisne_postavke'),
    url(r'^popisna_postavka/(?P<pk>\d+)$', views.PopisnaPostavkaDetailView.as_view(), name='popisna_postavka-detail'),
    url(r'^popisi/$', views.PopisListView.as_view(), name='popisi'),
    url(r'^popis/(?P<pk>\d+)$', views.PopisDetailView.as_view(), name='popis-detail'),
    


    url(r'^popisna_postavka/nova/$', views.popisna_postavka_nova, name='popisna_postavka-nova'),

]


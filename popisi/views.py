from django.shortcuts import render
from django.views import generic
from .models import Postavka, Popis, SpecifikacijaPostavke

def index(request):
    
    stej_postavke=Postavka.objects.all().count()
    stej_popisne_postavke=Popis.objects.all().count()
   

    return render(
        request,
        'index.html',
        context={'stej_postavke':stej_postavke,'stej_popisne_postavke':stej_popisne_postavke},
    )
class PostavkaListView(generic.ListView):
    model = Postavka
   # def get_queryset(self):
    #    return Postavka.objects.filter(opis_postavke__icontains='p')
class PostavkaDetailView(generic.DetailView):
    model = Postavka

class SpecifikacijaListView(generic.ListView):
    model = SpecifikacijaPostavke
    def get_queryset(self):
        return SpecifikacijaPostavke.objects.filter(dela=4)
class SpecifikacijaDetailView(generic.DetailView):
    model = SpecifikacijaPostavke

class PopisListView(generic.ListView):
    model = Popis
   # def get_queryset(self):
    #    return Postavka.objects.filter(opis_postavke__icontains='p')
class PopisDetailView(generic.DetailView):
    model = Popis    
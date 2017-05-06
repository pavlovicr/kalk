from django.shortcuts import render
from django.views import generic
from .models import Postavka, DelPostavke,Popis

def index(request):
    
    stej_postavke=Postavka.objects.all().count()
    stej_del_postavke=DelPostavke.objects.all().count()
   

    return render(
        request,
        'index.html',
        context={'stej_postavke':stej_postavke,'stej_del_postavke':stej_del_postavke},
    )
class PostavkaListView(generic.ListView):
    model = Postavka
   # def get_queryset(self):
    #    return Postavka.objects.filter(opis_postavke__icontains='p')
class PostavkaDetailView(generic.DetailView):
    model = Postavka

class PopisListView(generic.ListView):
    model = Popis
   # def get_queryset(self):
    #    return Postavka.objects.filter(opis_postavke__icontains='p')
class PopisDetailView(generic.DetailView):
    model = Popis    
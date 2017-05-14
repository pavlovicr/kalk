from django.shortcuts import render
from django.views import generic
from popisi.models import Postavka, Popis, SpecifikacijaPostavke
from django.db.models import Count

##################################################################

from popisi.models import Postavka,Skupina,Dela,SpecifikacijaPostavke,Popis
#exec(open("./popisi/views.py").read())

#def stetje(): 
#    print('dela')
#    zap_st = 1
#    for b in Popis.objects.all():
#        b.zaporedna_stevilka = zap_st
#        b.save()
#        zap_st = zap_st + 1
#stetje()


#def koda_postavke():
#    for a in Postavka.objects.all():
#        print(a.dela.koda_del)
#koda_postavke()


#deluje vendar da samo zadnjo kodo specifikacije
#def kodapopisa():
#    for a in Popis.objects.all():
#        for b in a.specifikacija.all():  
#            c=(b.koda_specifikacije)
#            a.koda_popisne_postavke=c
#            a.save()
#kodapopisa()


def kodapopisa():
    for a in Popis.objects.all():
        for b in a.specifikacija.all():  
            c=(b.koda_specifikacije)
            a.koda_popisne_postavke=c
            a.save()
kodapopisa()




#############################################################







def index(request):
    
    stej_postavke=Postavka.objects.all().count()
    stej_popisne_postavke=Popis.objects.all().count()
    q = Popis.objects.annotate(Count('postavka'))

    return render(
        request,
        'index.html',
        context={'stej_postavke':stej_postavke,'stej_popisne_postavke':stej_popisne_postavke,'q':q},
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
        #return SpecifikacijaPostavke.objects.filter(dela=5)
        return SpecifikacijaPostavke.objects.filter(dela__opis_del='VGRAJEVANJE BETONA')
class SpecifikacijaDetailView(generic.DetailView):
    model = SpecifikacijaPostavke

class PopisListView(generic.ListView):
   
    model = Popis
   # def get_queryset(self):
    #    return Postavka.objects.filter(opis_postavke__icontains='p')
    #stetje()
class PopisDetailView(generic.DetailView):
    model = Popis    

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx



from django.shortcuts import render
from django.views import generic
from popisi.models import Postavka, Popis, SpecifikacijaPostavke,Dela,Skupina,SkupinaSpecifikacije
from django.db.models import Count

##################################################################


#exec(open("./popisi/views.py").read())

def stetje(): 
    print('dela')
    zap_st = 1
    for b in Popis.objects.all():
        b.zaporedna_stevilka = zap_st
        b.save()
        zap_st = zap_st + 1
stetje()

def skupaj():

    for a in Popis.objects.all():
        zdruzeno = '.'.join([a.postavka.koda_postavke]+[str(b.koda_specifikacije) for b in a.specifikacija.all()])
        a.koda_popisne_postavke=zdruzeno
        a.save() 
        print(a.koda_popisne_postavke)
skupaj()

#def koda_postavke():
#    for a in Postavka.objects.all():
#        print(a.dela.koda_del)
#koda_postavke()


#deluje ???
#def kodapopisa():
#	c = ""
#	for a in Popis.objects.all():
#		for b in a.specifikacija.all():
#			c+=b.koda_specifikacije
#	a.koda_popisne_postavke = c
#	a.save()
#kodapopisa()





# ta deluje odlično
#def list_zdruzevanje():
#    for a in Popis.objects.all():
#        zdruzeno = '.'.join([str(b.koda_specifikacije) for b in a.specifikacija.all()])
#        a.koda_popisne_postavke=zdruzeno
#        a.save()
#list_zdruzevanje()

#tudi ta deluje , le da je za postavko
#def list_zdruzevanje1():
#    for c in Popis.objects.all():
#        c.koda_popisne_postavke=c.postavka.koda_postavke
#        c.save()
#        print(c.koda_popisne_postavke) 
#list_zdruzevanje1()







# ta funkcija združuje list  "".join(['miha','el'])  v mihael



#class ZeroObject(object):
#    def __add__(self, other):
#    return other

#>>> sum(["hi", "there"], ZeroObject())
#'hithere'







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



from django.shortcuts import render
from django.views import generic
from popisi.models import Postavka,SpecifikacijaPostavke,Dela,Skupina,SkupinaSpecifikacijePostavke,PopisnaPostavka,Popis,SpecifikacijaManager
from django.db.models import Count

##################################################################


#exec(open("./popisi/views.py").read())

def stetje(): 
    print('dela')
    zap_st = 1
    for b in PopisnaPostavka.objects.all():
        b.zaporedna_stevilka_popisne_postavke = zap_st
        b.save()
        zap_st = zap_st + 1
stetje()

def skupaj():
    
    for a in PopisnaPostavka.objects.all():
        zdruzeno = '.'.join([a.postavka.koda_postavke]+[str(b.koda_specifikacije) for b in a.specifikacija.all()])
        a.koda_popisne_postavke=zdruzeno
        a.save() 
        print(a.koda_popisne_postavke)
skupaj()


def popisnapostavka():
    for a in Postavka.objects.all():
        print(a.skupina_specifikacije_postavke)
popisnapostavka()








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

from django.http import HttpResponseRedirect
from django.http import HttpResponse
from popisi.models import Ime
from .forms import ImeForm

def im(request):
    
    if request.method == 'POST':

        form=ImeForm(request.POST)
        return HttpResponse('<tr><th><label for="id_tvoje_ime">Tvoje ime:</label></th><td><input type="text" name="tvoje_ime" maxlength="200" required id="id_tvoje_ime" /></td></tr>'
)

#    else:
#        form = ImeForm()
#    return render(request,'popisi/ime.html',{'form':form})
def get_ime(request):

    if request.method == 'POST':
        form = ImeForm(request.POST) 
       

        if form.is_valid():
            #form.save()
            #print (request.COOKIES)
            #print (request.GET.lists())
            #print (request.body)
            a=request.POST['tvoje_ime']
            print(a)
            
            
            
            b=Postavka.objects.get(koda_postavke=a)
            for b in b.skupina_specifikacije_postavke.all():

                print(b.specifikacijapostavke_set
                     .all())





            #b=Ime.objects.get(tvoje_ime=a)
            #print(b)

            

            #print (request.GET.get('tvoje_ime'))
            #print (request.path_info)
            #print (request.encoding)
            #print (request.content_type)
            return HttpResponse('sonček je  ')
    else:
        form = ImeForm()
        print(form)
    return render(request, 'popisi/ime.html', {'form': form})
    





from .forms import PopisnaPostavkaForm

def popisna_postavka_nova(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PopisnaPostavkaForm(request.POST)
        # check whether it's valid:
        if form.is_valid(): 
            form.save()# process the data in form.cleaned_data as required 
            # ... 
            # redirect to a new URL: 

            return HttpResponseRedirect('/popisi/popisne_postavke/')
    # if a GET (or any other method) we'll create a blank form 
    else: form = PopisnaPostavkaForm()
    return render(request, 'popisi/popisna_postavka_nova.html', {'form': form})





from django.http import HttpResponse

def vaja(request):
    a=request.path
    return HttpResponse(a)


















def index(request):
    
    stej_postavke=Postavka.objects.all().count()
    stej_popisne_postavke=PopisnaPostavka.objects.all().count()
    q = PopisnaPostavka.objects.annotate(Count('postavka'))

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
#    def get_queryset(self):
 
#        return SpecifikacijaPostavke.objects.filter(skupinaspecifikacije__opis_skupine_specifikacije='odpornost proti obrabi površine')

class SpecifikacijaDetailView(generic.DetailView):
    model = SpecifikacijaPostavke

class PopisnaPostavkaListView(generic.ListView):
   
    model = PopisnaPostavka
   # def get_queryset(self):
    #    return Postavka.objects.filter(opis_postavke__icontains='p')
    #stetje()
class PopisnaPostavkaDetailView(generic.DetailView):
    model = PopisnaPostavka    

class PopisListView(generic.ListView):
   
    model = Popis
   # def get_queryset(self):
    #    return Postavka.objects.filter(opis_postavke__icontains='p')
    #stetje()
class PopisDetailView(generic.DetailView):
    model = Popis

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx



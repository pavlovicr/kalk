from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Projekt(models.Model):
    naziv_projekta = models.CharField(max_length=200, default ="naziv projekta",null=True)
    opis_projekta = models.TextField(max_length=2000,default="opis projekta ")
    datum_projekta = models.DateField()
    uporabnik = models.ForeignKey(User, null=True, blank=True)
    class Meta: 
        ordering = ['-datum_projekta']
    def __str__(self):
        return self.naziv_projekta
    def get_absolute_url(self):
        return reverse('projekt-detail', args=[str(self.id)]) 

class Podrocje(models.Model):
    koda_podrocja = models.CharField(max_length=50,null=True)
    naziv_podrocja = models.CharField(max_length=50, default ="industrijski_objekti")
    splosna_dolocila_podrocja = models.TextField(max_length=2000,default="splošna določila področja industrijske gradnje")
    class Meta: 
        ordering = ["koda_podrocja"]
    def __str__(self):
        return self.naziv_podrocja  
    def get_absolute_url(self):
        return reverse('podrocje-detail', args=[str(self.id)]) 
 
class Zvrst(models.Model):
    zaporedna_stevilka_zvrsti = models.IntegerField(null=True)
    koda_zvrsti = models.CharField(max_length=50,null=True)
    naziv_zvrsti = models.CharField(verbose_name='Naziv zvrsti',max_length=50,default='GRADBENA DELA')        
    splosna_dolocila_zvrsti = models.TextField(max_length=2000,default="splošna določila zvrsti GRADBENA DELA ")
    class Meta: 
        ordering = ["zaporedna_stevilka_zvrsti"]
    def __str__(self):
        #return self.naziv_zvrsti
        return '%s, %s, %s' % (self.zaporedna_stevilka_zvrsti, self.koda_zvrsti, self.naziv_zvrsti) 
    def get_absolute_url(self):
        return reverse('zvrst-detail', args=[str(self.id)]) 

class Skupina(models.Model):
    zaporedna_stevilka_skupine = models.IntegerField(null=True)
    koda_skupine = models.CharField(max_length=50,null=True)
    naziv_skupine = models.CharField(verbose_name='Naziv skupine',max_length=50,default='Zemeljska dela')
    splosna_dolocila_skupine = models.TextField(max_length=2000,default="splošna določila skupine ZEMELJSKA DELA ")
    zvrst = models.ForeignKey('Zvrst',on_delete=models.CASCADE)    
     
    class Meta:  
        ordering = ["zaporedna_stevilka_skupine"]
    def __str__(self):
    #    return self.naziv_skupine
        return '%s, %s, %s' % (self.zaporedna_stevilka_skupine, self.koda_skupine, self.naziv_skupine) 
    def get_absolute_url(self): 
        return reverse('skupina-detail', args=[str(self.id)]) 

class Dela(models.Model):
    zaporedna_stevilka_del = models.IntegerField(null=True) 
    koda_del = models.CharField(max_length=50,null=True)
    opis_del=models.CharField(verbose_name='Opis del',max_length=50)
    splosna_dolocila_del = models.TextField(max_length=2000,default="splošna določila za dela IZKOPI ")
    skupina = models.ForeignKey('Skupina', on_delete=models.CASCADE) 
    podrocje = models.ManyToManyField(Podrocje, default=[1,2,3,4])
    class Meta: 
        ordering = ["zaporedna_stevilka_del"]
    def __str__(self):
        return self.opis_del
        return '%s, %s, %s' % (self.zaporedna_stevilka_del, self.koda_del, self.opis_del)
    def get_absolute_url(self):
        return reverse('dela-detail', args=[str(self.id)]) 

class SpecifikacijaPostavke(models.Model):
    zaporedna_stevilka_specifikacije = models.IntegerField(null=True)
    koda_specifikacije = models.CharField(max_length=50,null=True)    
    vsebina_specifikacije = models.CharField(verbose_name='standardna vsebina specifikacije postavke',max_length=100)
    splosna_dolocila_specifikacije = models.TextField(max_length=2000,default="splošna določila specifikacije")
    info = models.TextField(max_length=2000,default="tehnične informacije")
    dela = models.ManyToManyField(Dela)
    class Meta: 
        ordering = ["zaporedna_stevilka_specifikacije"]
    def __str__(self):
        #return self.vsebina_specifikacije
        return '%s, %s, %s' % (self.zaporedna_stevilka_specifikacije,self.koda_specifikacije,self.vsebina_specifikacije)
    def get_absolute_url(self):
        return reverse('specifikacija-detail', args=[str(self.id)]) 

class Postavka(models.Model): 
    zaporedna_stevilka_postavke = models.IntegerField(null=True)
    koda_postavke = models.CharField(max_length=100,null=True)
    opis_postavke = models.CharField(max_length=100)
    enota_mere = models.CharField(max_length=10)
    dela = models.ForeignKey('Dela', on_delete=models.SET_NULL, null=True)
    specifikacija = models.ManyToManyField(SpecifikacijaPostavke)
    splosna_dolocila_postavke = models.TextField(max_length=1000, default="splošna določila postavke")
    class Meta: 
        ordering = ["zaporedna_stevilka_postavke"]
    def __str__(self):
        return '%s, %s, %s, %s' % (self.zaporedna_stevilka_postavke,self.koda_postavke,self.opis_postavke, self.enota_mere)
    def get_absolute_url(self):
        return reverse('postavka-detail', args=[str(self.id)])    


class Objekt(models.Model):
    naziv_objekta = models.CharField(max_length=50,null=True)
    neto_povrsina_objekta=models.DecimalField(max_digits=20,decimal_places=2,default=('0.00'))
    bruto_povrsina_objekta=models.DecimalField(max_digits=20,decimal_places=2,default=('0.00'))
    opis_objekta = models.TextField(max_length=2000,default="opis objekta ")
    podrocje = models.ForeignKey('Podrocje',on_delete=models.CASCADE,default=1)
    projekt = models.ForeignKey('Projekt',on_delete=models.CASCADE)
    class Meta: 
        ordering = ["naziv_objekta"]
    def __str__(self):
        return self.naziv_objekta
    def get_absolute_url(self):
        return reverse('objekt-detail', args=[str(self.id)]) 

x=1

class Popis(models.Model):
    koda_popisne_postavke = models.CharField(max_length=100,null=True)
    zaporedna_stevilka = models.IntegerField(null=True)
    postavka = models.ForeignKey('Postavka')
    specifikacija = models.ManyToManyField(SpecifikacijaPostavke,verbose_name='standardne specifikacije postavke')     
    specifikacija_uporabnika = models.TextField(max_length=2000,verbose_name='dodatne specifikacije postavke',null=True )
    objekt = models.ForeignKey('Objekt',on_delete=models.CASCADE, default=x)
    class Meta: 
            ordering = ["zaporedna_stevilka"]
    def __str__(self):
#        return self.zaporedna_stevilka
        return '%s, %s, %s' % (self.zaporedna_stevilka, self.postavka, self.specifikacija,)
    def get_absolute_url(self):
        return reverse('popis-detail', args=[str(self.id)])    


################FUNKCIJEFUNKCIJEFUNKCIJE##############################################################################

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import When, F, Q
class Projekt(models.Model):

    I='Industrijski objekti'
    T='Trgovski objekti'
    P='Pisarniški objekti'
    D='Družbeni objekti,šole,vrtci,domovi'
    S='Stanovanja'
    C='Ceste'
    podrocje = (
        ('I', 'Industrijski objekti'),
        ('T', 'Trgovski objekti'),
        ('P', 'Pisarniški objekti'),
        ('D', 'Družbeni objekti,šole,vrtci,domovi'),
        ('S', 'Stanovanja'),
        ('C', 'Ceste'),
    )
    stevilka_projekta = models.AutoField(primary_key=True)
    koda_projekta = models.CharField(max_length=50)
    podrocje = models.CharField(choices=podrocje,default=I,verbose_name='Področje',max_length=50)
    naziv_projekta = models.CharField(max_length=200, default ="naziv projekta")
    opis_projekta = models.TextField(max_length=2000,default="opis projekta ")
    datum_projekta = models.DateField()
    uporabnik = models.ForeignKey(User, null=True, blank=True)
    
    class Meta: 
        ordering = ["-stevilka_projekta"]
    def __str__(self):
        return self.naziv_projekta
    def get_absolute_url(self):
        return reverse('projekt-detail', args=[str(self.id)]) 

class Objekt(models.Model):
    
    naziv_objekta = models.CharField(max_length=50)
    neto_povrsina_objekta=models.DecimalField(max_digits=20,decimal_places=2,default=('0.00'))
    bruto_povrsina_objekta=models.DecimalField(max_digits=20,decimal_places=2,default=('0.00'))
    opis_objekta = models.TextField(max_length=2000,default="opis objekta ")
    projekt = models.ForeignKey('Projekt',on_delete=models.CASCADE)
 
    class Meta: 
        ordering = ["naziv_objekta"]
    def __str__(self):
        return self.naziv_objekta
    def get_absolute_url(self):
        return reverse('objekt-detail', args=[str(self.id)]) 

class Zvrst(models.Model):
    G='Gradbena dela'
    O='Obrtniška dela'
    S='Strojne instalacije'
    E='Elektro instalacije'
    Z='Zunanja ureditev'
    zvrst = (
        ('G', 'Gradbena dela'),
        ('O', 'Obrtniška dela'),
        ('S', 'Strojne instalacije'),
        ('E', 'Elektro instalacije'),
        ('Z', 'Zunanja ureditev'),
    )
    zvrst = models.CharField(choices=zvrst,default=G,verbose_name='Zvrst',max_length=50)        
    splosna_dolocila_zvrsti = models.TextField(max_length=2000,default="splošna določila zvrsti ")
 
    class Meta: 
        ordering = ["zvrst"]
    def __str__(self):
        return self.zvrst
    def get_absolute_url(self):
        return reverse('zvrst-detail', args=[str(self.id)]) 

class Skupina(models.Model):
#    Z='Zemeljska dela'
#    B='Betonska dela'
#    Zi='Zidarska dela'
#    T='Tesarska dela'
#    K='Kanalizacija'
#    Kr='Krovska dela'
#    Kl='Kleparska dela'
#    Kj='Ključavničarska dela'
#    M='Mizarska dela'
#    S='Slikopleskarska dela'
#    St='Steklarska dela'
#    Ke='Keramičarska dela'
#    Tl='Tlakarska dela'
    
    skupina = (
    ('ZE','Zemeljska dela'),
    ('BT','Betonska dela'),
    ('ZD','Zidarska dela'),
    ('TS','Tesarska dela'),
    ('KN','Kanalizacija'),
    ('KR','Krovska dela'),
    ('KL','Kleparska dela'),
    ('KJ','Ključavničarska dela'),
    ('AL','Aluminij dela'),
    ('MZ','Mizarska dela'),
    ('MK','Mavčnokartonska dela '),
    ('SL','Slikopleskarska dela'),
    ('ST','Steklarska dela'),
    ('KR','Keramičarska dela'),
    ('TL','Tlakarska dela'),
    ('FA','Fasaderska dela'),

    )
    skupina = models.CharField(choices=skupina,default='Zem',verbose_name='Skupina',max_length=50)
    splosna_dolocila_skupine = models.TextField(max_length=2000,default="splošna določila skupine ")
    zvrst = models.ForeignKey('Zvrst',on_delete=models.CASCADE)    
    class Meta: 
        ordering = ["skupina"]
    def __str__(self):
        return self.skupina
    def get_absolute_url(self):
        return reverse('skupina-detail', args=[str(self.id)]) 

class Dela(models.Model):
    koda_del = models.CharField(max_length=50)
    opis_del=models.CharField(verbose_name='Opis del',max_length=50)
    splosna_dolocila_del = models.TextField(max_length=2000,default="splošna določila del ")
    objekt = models.ForeignKey('Objekt',on_delete=models.CASCADE)
    skupina = models.ForeignKey('Skupina',null=True, on_delete=models.CASCADE) 
    class Meta: 
        ordering = ["opis_del"]
    def __str__(self):
        return self.opis_del
    def get_absolute_url(self):
        return reverse('dela-detail', args=[str(self.id)]) 

  
class SpecifikacijaPostavke(models.Model):
 
    vsebina_specifikacije = models.CharField(max_length=100)
    
    def __str__(self):
        return self.vsebina_specifikacije
    def get_absolute_url(self):
        return reverse('specifikacija_postavke-detail', args=[str(self.id)]) 




class Postavka(models.Model):
    
    koda_postavke = models.CharField(max_length=100)
    opis_postavke = models.CharField(max_length=100, help_text="")
    specifikacija = models.ManyToManyField(SpecifikacijaPostavke)
    enota_mere = models.CharField(max_length=10)
    dela = models.ForeignKey('Dela', on_delete=models.SET_NULL, null=True)
    splosna_dolocila_postavke = models.TextField(max_length=1000, default="miha")
     
    
    class Meta: 
        ordering = ["opis_postavke"]
    def __str__(self):
        return '%s, %s' % (self.opis_postavke, self.enota_mere)
    def get_absolute_url(self):
        return reverse('postavka-detail', args=[str(self.id)])    

class DelPostavke(models.Model):
 
    koda_dela_postavke = models.CharField(max_length=50)
    opis_dela_postavke = models.CharField(max_length=100)
    splosna_dolocila_dela_postavke = models.TextField(max_length=1000,help_text="",null=True)
    postavka = models.ManyToManyField(Postavka) 
    class Meta: 
        ordering = ["opis_dela_postavke"]
    def __str__(self):
        return self.opis_dela_postavke
    def get_absolute_url(self):
        return reverse('del_postavke-detail', args=[str(self.id)]) 
      
class Popis(models.Model):
    
    id = models.AutoField(primary_key=True)
    zaporedna_stevilka = models.IntegerField(null=True)
    postavka = models.ForeignKey('Postavka', on_delete=models.SET_NULL, null=True)
    del_postavke = models.ManyToManyField(DelPostavke)     
    class Meta: 
        ordering = ["zaporedna_stevilka"]
    def __str__(self):
#        return self.zaporedna_stevilka
        return '%s, %s, %s' % (self.zaporedna_stevilka, self.postavka, self.del_postavke,)
    def get_absolute_url(self):
        return reverse('popis-detail', args=[str(self.id)])    

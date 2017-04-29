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
    zvrst = models.CharField(choices=zvrst,default='G',verbose_name='Zvrst',max_length=50)        
    splosna_dolocila_zvrsti = models.TextField(max_length=2000,default="splošna določila zvrsti ")
 
    class Meta: 
        ordering = ["zvrst"]
    def __str__(self):
        return self.zvrst
    def get_absolute_url(self):
        return reverse('zvrst-detail', args=[str(self.id)]) 

class Skupina(models.Model):
    Z='Zemeljska dela'
    B='Betonska dela'
    Zi='Zidarska dela'
    T='Tesarska dela'
    K='Kanalizacija'
    Kr='Krovska dela'
    Kl='Kleparska dela'
    Kj='Ključavničarska dela'
    M='Mizarska dela'
    S='Slikopleskarska dela'
    St='Steklarska dela'
    Ke='Keramičarska dela'
    Tl='Tlakarska dela'
    
    skupina = (
    ('Z','Zemeljska dela'),
    ('B','Betonska dela'),
    ('Zi','Zidarska dela'),
    ('T','Tesarska dela'),
    ('K','Kanalizacija'),
    ('Kr','Krovska dela'),
    ('Kl','Kleparska dela'),
    ('Kj','Ključavničarska dela'),
    ('M','Mizarska dela'),
    ('S','Slikopleskarska dela'),
    ('St','Steklarska dela'),
    ('Ke','Keramičarska dela'),
    ('Tl','Tlakarska dela'),
    )
    skupina = models.CharField(choices=skupina,default=Z,verbose_name='Skupina',max_length=50)
    splosna_dolocila_skupine = models.TextField(max_length=2000,default="splošna določila skupine ")
    
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
 
    class Meta: 
        ordering = ["opis_del"]
    def __str__(self):
        return self.opis_del
    def get_absolute_url(self):
        return reverse('dela-detail', args=[str(self.id)]) 

        
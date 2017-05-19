from django.contrib import admin
from .models import Projekt,Popis,Dela,Skupina,Zvrst,Postavka,SpecifikacijaPostavke,Podrocje,SkupinaSpecifikacijePostavke,PopisnaPostavka


admin.site.register(Projekt)
admin.site.register(Popis)
admin.site.register(Zvrst)
admin.site.register(Skupina)
admin.site.register(Dela)
admin.site.register(Postavka)
admin.site.register(PopisnaPostavka)
admin.site.register(SpecifikacijaPostavke)
admin.site.register(Podrocje)
admin.site.register(SkupinaSpecifikacijePostavke)

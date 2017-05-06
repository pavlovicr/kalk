from django.contrib import admin
from .models import Projekt, Objekt,Dela,Skupina,Zvrst,Postavka,Popis,SpecifikacijaPostavke

admin.site.register(Projekt)
admin.site.register(Objekt)
admin.site.register(Zvrst)
admin.site.register(Skupina)
admin.site.register(Dela)
admin.site.register(Postavka)
admin.site.register(Popis)
admin.site.register(SpecifikacijaPostavke)



from django.contrib import admin
from .models import Projekt, Objekt,Dela,Skupina,Zvrst,DelPostavke,Postavka,Popis

admin.site.register(Projekt)
admin.site.register(Objekt)
admin.site.register(Zvrst)
admin.site.register(Skupina)
admin.site.register(Dela)
admin.site.register(DelPostavke)
admin.site.register(Postavka)
admin.site.register(Popis)



# Register your models here.

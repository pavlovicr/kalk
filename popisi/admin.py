from django.contrib import admin
from .models import Projekt, Objekt,Dela,Skupina,Zvrst

admin.site.register(Projekt)
admin.site.register(Objekt)
admin.site.register(Zvrst)
admin.site.register(Skupina)
admin.site.register(Dela)
# Register your models here.

from django.contrib import admin
from .models import Projekt,Popis,Dela,Skupina,Zvrst,Postavka,SpecifikacijaPostavke,Podrocje,SkupinaSpecifikacijePostavke,PopisnaPostavka




class PopisnaPostavkaAdmin(admin.ModelAdmin):
    list_display = ('zaporedna_stevilka_popisne_postavke','koda_popisne_postavke','popis')
    list_filter = ('koda_popisne_postavke',)
    fields = ['zaporedna_stevilka_popisne_postavke', 'koda_popisne_postavke', ('postavka','specifikacija','specifikacija_uporabnika','popis',)]



class SpecifikacijaPostavkeInline(admin.TabularInline):
	model = SpecifikacijaPostavke


@admin.register(SkupinaSpecifikacijePostavke) 
class SkupinaSpecifikacijePostavkeAdmin(admin.ModelAdmin):
    list_display = ('koda_skupine_specifikacije','opis_skupine_specifikacije',)
    fields = ['opis_skupine_specifikacije','dela',] 
    list_filter = ('dela',)
    inlines = [SpecifikacijaPostavkeInline]    



@admin.register(SpecifikacijaPostavke)
class SpecifikacijaPostavkeAdmin(admin.ModelAdmin):
    
    list_display = ('koda_specifikacije','vsebina_specifikacije','skupinaspecifikacije',)
    list_filter = ('koda_specifikacije', 'skupinaspecifikacije')
    
    fieldsets = (
        (None, {
            'fields': ('koda_specifikacije','vsebina_specifikacije','skupinaspecifikacije')
        }),

    )

    




admin.site.register(Projekt)
admin.site.register(Popis)
admin.site.register(Podrocje)
admin.site.register(Zvrst)
admin.site.register(Skupina)
admin.site.register(Dela)
admin.site.register(Postavka)
admin.site.register(PopisnaPostavka,PopisnaPostavkaAdmin)
#admin.site.register(SpecifikacijaPostavke)
#admin.site.register(SkupinaSpecifikacijePostavke)




from django import forms


from .models import PopisnaPostavka

class PopisnaPostavkaForm(forms.ModelForm):

    class Meta:
        model = PopisnaPostavka
        fields = ('zaporedna_stevilka_popisne_postavke','postavka','specifikacija','specifikacija_uporabnika','popis',)




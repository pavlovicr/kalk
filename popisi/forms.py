from django import forms
from .models import Ime

class ImeForm(forms.ModelForm):
    

    def __init__(self, *args, **kwargs):
        super(ImeForm, self).__init__(*args, **kwargs)
        
        


    class Meta:
        model = Ime
        fields = ('tvoje_ime',)
 #       widgets = {
 #       	'tvoje_ime': forms.CheckboxSelectMultiple
 #       }





data={'koda_popisne_postavke':'oh','zaporedna_stevilka_popisne_postavke':20,'postavka':4,'specifikacija':[8,9,10],'specifikacija_uporabnika':'hojladri','popis':2}


from .models import PopisnaPostavka,SpecifikacijaPostavke,Postavka,SkupinaSpecifikacijePostavke

class PopisnaPostavkaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PopisnaPostavkaForm, self).__init__(*args, **kwargs)
        
    

        self.fields['specifikacija'].queryset = SpecifikacijaPostavke.objects.all()
        self.fields['specifikacija'].label_from_instance = lambda obj: "%s" % (obj.koda_specifikacije)

        
        
#        self.fields['postavka'].queryset = Postavka.objects.all() 
 #       [postavka for postavka in self.fields['postavka'].queryset]
  #      print(postavka)    

   #     self.fields['postavka'].label_from_instance = lambda obj: "%s" % (obj.skupina_specifikacije_postavke)

    class Meta:
        model = PopisnaPostavka
        fields = ('zaporedna_stevilka_popisne_postavke','specifikacija','postavka','specifikacija_uporabnika','popis',)
        widgets = {
    #    	'postavka': forms.CheckboxSelectMultiple
            'specifikacija': forms.CheckboxSelectMultiple            
        }
        


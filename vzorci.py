
the_world_is_flat=True

def hec():
    if the_world_is_flat: print("vaja dela mojstra")
    else :print("pazi, da te ne pregazi")
hec()     

def koda():
	for a in Postavka.object.all():
	    a.koda_postavke
	    y=a.koda_postavke
return y            
#exec(open("./popisi/utils.py").read(


#default=kodapopisa()
from popisi.models import Postavka,Skupina,Dela,SpecifikacijaPostavke
#exec(open("./popisi/utils.py").read())

def stetje(): 
    print('dela')
    zap_st = 1
    for b in PopisnaPostavka.objects.all():
        b.zaporedna_stevilka = zap_st
        b.save()
        zap_st = zap_st + 1
    return('dela') 
stetje()


class GroupCreateForm(forms.ModelForm):

locations = forms.ModelMultipleChoiceField(label='',widget=forms.CheckboxSelectMultiple(attrs={'class': 'styled', "style":"margin:10px;"}), queryset=None)      
group_name = forms.CharField(label='', required=True ,widget=forms.TextInput(attrs={'rows': '1', 'class': 'form-control', 'placeholder': 'Geben Sie den Gruppen Namen an'}))

def __init__(self, user, *args, **kwargs):
    super(GroupCreateForm, self).__init__(*args, **kwargs)
    self.fields['locations'].queryset = LocationData.objects.all().filter(email=user.email)

class Meta: 
    model = GroupManagement
    fields = ['group_name', 'locations']
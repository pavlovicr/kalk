from popisi.models import Postavka,Skupina,Dela,SpecifikacijaPostavke,Popis
#exec(open("./popisi/utils.py").read())

def stetje(): 
    print('dela')
    zap_st = 1
    for b in Popis.objects.all():
        b.zaporedna_stevilka = zap_st
        b.save()
        zap_st = zap_st + 1
    return('dela') 
#stetje()


#def koda_postavke():
#    for a in Postavka.objects.all():
#        print(a.dela.koda_del)
#koda_postavke()


#def kodapopisa():
#    for a in Popis.objects.all():
#        for b in a.specifikacija.all():  
#            print(b.koda_specifikacije)
#kodapopisa()



#exec(open("./popisi/utils.py").read())        

#print(stetje()+koda()) 5,6,7
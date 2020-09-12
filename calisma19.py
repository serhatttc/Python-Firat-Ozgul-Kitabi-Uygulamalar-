# -*- coding: utf-8 -*-
#                           ------ NESNE TABANLI PROGRAMLAMA  ------(DEVAM)--

#            ----  Sınıf Metotları  ----
import çalışan

ahmet = çalışan.Çalışan("Ahmet")
mehmet = çalışan.Çalışan("Mehmet")

çalışan.personelSayisi()
# bu yaptığımız fonk. sınıf dışındayken 
#%% tekrardan fonk. sınıf içine alalım
# bu fonk. örnek adıyla değilde sınıf adıyla erişmek için şu kod aklımıza geldi.
# from çalışan import Çalışan
# Çalışan.personelSayisi()
#  ancak bu kod bize hata verir.çünkü burada biz bu komutu vererek bir 
# sınıf metoduna erişmeye çalışıyoruz.ama kodlarımızın içinde sınıf metodu yok.
# bir metoda sınıf adı ile erişebilmek için ilgili metodu bir sınıf
# metodu olarak tanımlamamız gerek.

#%%   ----  @classmethod Bezeyicisi Ve cls  ----
#class Sınıf():
#    sinifNiteligi = 0
#    
#    def __init__(self,param1,param2):
#        self.param1 = param1
#        self.param2 = param2
#        self.ornekNiteligi = 0
#    
#    def ornekMetodu(self):
#        self.ornekNiteligi += 1
#        return self.ornekNiteligi
#    
#    def sinifMetodu(cls):
#        cls.sinifNiteligi += 1
#        return cls.sinifNiteligi
# python açısından örnek ve sınıf metotları arasında fark bulunmaz.python ikisini de
# örnek metodu olarak algılar.sınıf metodu oluşturmak için cls gereklidir ama yeterli değildir.
# bunu için birkaç ekleme daha yapmalıyız. @ classmethod eklemsi yapıcaz.
# python da başında @ olan ögelere bezeyici(decorator) denir.şimdi bunu Çalışan'a uygulayalım.

#class Çalışan(): # öncelikle sınıfı tanımlıyoruz.
#    personel = [] # personel adlı sınıf niteliği ekliyoruz.
#    
#    def __init__(self,isim):
#        self.isim = isim # isim parametresini sınıfın başka bölgelerinde de kullanmak için yaptık.
#        self.kabiliyetleri = []
#        self.personelEkle()
#    
#    @classmethod
#    def personelSayisi(cls):
#        print(len(cls.personel))
#    
#    
#    def personelEkle(self):
#        self.personel.append(self.isim)
#        print("{} adlı kişi personele eklendi.".format(self.isim))
#    
#    @classmethod    
#    def personeliGoruntule(cls):
#        print("Personel Listesi : ")
#        for kisi in cls.personel:
#            print(kisi)
#            
#    def kabiliyetEkle(self,kabiliyet):
#        self.kabiliyetleri.append(kabiliyet)
#            
#    def kabiliyetleriGoruntule(self):
#        print("{} adlı kişinin kabiliyetleri: ".format(self.isim))
#        for kabiliyet in self.kabiliyetleri:
#            print(kabiliyet)

# personelsayısı ile personeligoruntule fonk. sınıf metodu yaptık.çünkü ikiside tek tek
# örneklerden ziyade sınıfın genelini ilgilendiriyor.

# artık sınıfı şu şekilde kullanabiliriz.    
from çalışan import Çalışan
Çalışan.personelSayisi()
# artık sadece sınıf adını kullanarak bu fonksiyona erişebildik.bu da bize
# personel sayısını 0 olduğu durumunu görüntüleyebilme imkanı veriyor.
# ayrıca bu sınıf metodu sınıfın içinde yer aldığı için seçmeli içe aktarımlarda
# sınıfın öteki ögeleriyle birlikte bu metotta aktarılacak.  

# personele üye ekleyelim.
ahmet = Çalışan("Ahmet")
mehmet = Çalışan("Mehmet")
Çalışan.personelSayisi()
# yani sınıfın herhangi bir örneğine bağlı olmayan bir işlem yapan ama anlamsal
# olarak sınıfla ilişkili olduğu için sınıfın dışında bırakmak istemediğimiz
#  fonksiyonları birer sınıf metodu olarak tanımlayabiliriz.    
    
#%%         ----  Alternatif İnşacılar  ----  
    
#liste = [("111111111","greenberg","sana gül bahçesi","metis"),
#         ("222222222","evren","postmodern kız sevdim","ithaki"),
#         ("333333333","nietzsche","buyurdu zerdüşt","cem")]   
#--------------------------------------------------------------------
# liste içinde demetler var ve demetlerin içinde bir kitabın ISBN numarası
# yazarı,kitap adı ve yayınevi var. 
# amacımız bu listeden çeşitli ölçütlere göre sorgulama yapabilen program yazmak.
#-------------------------------------------------------------------------  
#def sorgula(ölçüt=None,değer=None):
#    for li in liste:
#        if not ölçüt and not değer:
#            print(*li,sep=", ")
#        
#        elif ölçüt == "isbn":
#            if değer == li[0]:
#                print(*li,sep=", ")
#    
#        elif ölçüt == "yazar":
#            if değer == li[1]:
#                print(*li,sep=", ")
#    
#        elif ölçüt == "eser":
#            if değer == li[2]:
#                print(*li,sep=", ")
#            
#            elif ölçüt == "yayınevi":
#                if değer == li[3]:
#                    print(*li,sep=", ")
#--------------------------------------------------------------------------                    
# nurada önce kitep listemizi tanımladık.daha sonra sorgula() fonk. yazdık.Bu fonk.
# 2 parametre verdik ve onların değerlerini None olarak belirledik böylece fonksiyonu
# argüman vermeden de çalıştırabilicez.
            
# gelelim bu fonksiyonu nasıl kuracağımıza.şimdi bunu klist.py adlı dosyaya kaydedelim.    
# şimdi modülü içe aktaralım.
import klist
klist.sorgula()# öncelikle klist modülü içindeki sorgula fonk. argümazsız çağıralım.    
# gördüğünüz gibi listedeki bütün bilgileri verdi.
print("-"*55)    
klist.sorgula("isbn","111111111")# şimdi ISBN numarasına göre sorgu yaptık.
#-------------------------------------------------------------------------
# yukarıdaki programı kısaca şöyle de yazabilirdik.

#def sorgula(ölçüt=None,değer=None):
#    d = {"isbn"    :[li for li in liste if değer==li[0]],
#         "yazar"   :[li for li in liste if değer==li[1]],
#         "eser"    :[li for li in liste if değer==li[2]],
#         "yayınevi":[li for li in liste if değer==li[3]]}
#    for öge in d.get(ölçüt,liste):
#        print(*öge,sep=", ")

# burada if-else cümleciklerini birer liste üretecine dönüştürüp d adlı 
# sözlüğün anahtarı olarak belirledik.artık sorgulama işlemlerini sözlük içinden yapıcaz.
#---------------------------------------------------------------------------
# şöylede yapabiliriz.

#def bul(değer,sıra):
#    return [li for li in liste if değer == li[sıra]]
#def sorgula(ölçüt=None,değer=None):
#    d = {"isbn"    :bul(değer,0),
#         "yazar"   :bul(değer,1),
#         "eser"    :bul(değer,2),
#         "yayınevi":bul(değer,3)}
#    for öge in d.get(ölçüt,liste):
#        print(*öge,sep=", ")
#-------------------------------------------------------
# burada bütün liste üreteçlerini tek bir bul() fonk. içinde oluşturarak, sorgula()
# fonk. içindeki d sözlüğüne gönderdik.
#%%
import klist
klist.sorgula()
print("-"*55)
klist.sorgula("yazar","nietzsche")
#%%
# mesela bu kodları sınıf yapısı içinde de ifade edebiliriz.
#----------------------------------------------------------------------------
#class Sorgu():
#    def __init__(self):
#        self.liste = [("111111111","greenberg","sana gül bahçesi","metis"),
#                      ("222222222","evren","postmodern kız sevdim","ithaki"),
#                      ("333333333","nietzsche","buyurdu zerdüşt","cem")]
#    
#    def bul(self,değer,sıra):
#        return [li for li in self.liste if değer == li[sıra]]
#    
#    def sorgula(self,ölçüt=None,değer=None):
#        d = {"isbn"    :self.bul(değer,0),
#             "yazar"   :self.bul(değer,1),
#             "eser"    :self.bul(değer,2),
#             "yayınevi":self.bul(değer,3)}
#        
#        for öge in d.get(ölçüt,self.liste):
#            print(*öge,sep=", ")
# --------------------------------------------------------------------------    
# burada kitap listesini bir örnek niteliği olarak tanımlamak suretiyle 
# sınıfın heryerinden kullanılabilir hale getirdik.

# bu sınıfı bu şekilde kullanabiliriz.

import klist
sorgu = klist.Sorgu()
sorgu.sorgula()
print("-"*55)
sorgu.sorgula("yazar","evren") 
#%%    gelelim yukarıdaki kodların yazımının son haline.
#------------------------------------------------------------------------- 
#class Sorgu():
#    def __init__(self,değer=None,sıra=None):
#        self.liste = [("111111111","greenberg","sana gül bahçesi","metis"),
#                      ("222222222","evren","postmodern kız sevdim","ithaki"),
#                      ("333333333","nietzsche","buyurdu zerdüşt","cem")]
#        
#        if not değer and not sıra:
#            l = self.liste
#        else:
#            l = [li for li in self.liste if değer == li[sıra]]
#        for i in l:
#            print(*i,sep=", ")
#    
#    @classmethod
#    def isbnden(cls,isbn):
#        cls(isbn,0)
#    
#    @classmethod
#    def yazardan(cls,yazar):
#        cls(yazar,1)
#        
#    @classmethod
#    def eserden(cls,eser):
#        cls(eser,2)
#        
#    @classmethod
#    def yayınevinden(cls,yayınevi):
#        cls(yayınevi,3)
#----------------------------------------------------------------------------
# yukarıdaki sınıfı şu şekilde kulllanabiliriz.
# önce modülümüzü içe aktaralım.
from klist import Sorgu
# ISBN numarasına göre sorgu gerçekleştirelim.
Sorgu.isbnden("111111111")
print("-"*55)
# bir de yazara göre sorgulayalım.
Sorgu.yazardan("evren")
print("-"*55)
# şimdi de bütün listeyi alalım.
hepsi = Sorgu()
# gördüğünüz gibi sınıfı parametresiz olarak verdiğimizde bütün verileri elde ediyoruz.
#%% Mesela.
#------------------------------------------------------------------------
#class Giriş():
#    def __init__(self,mesaj="Müşteri numaranız:"):
#        cevap = input(mesaj)
#        print("Hoşgeldiniz.")
#---------------------------------------------------------------------
# burada tanımladığımız Giriş sınıfı bir müşteri numarası ile sisteme giriş imkanı sağlıyor.
# kodları sistem.py dosyasına kaydettik.
from sistem import Giriş
Giriş()       
# eğer biz aynı zamanda bir parola ve TCno ile giriş imkanı sağlamak istersek
# başka yöntemlerin yanısıra sınıf metotlarından da yararlanabiliriz.
#--------------------------------------------------------------------
#    @classmethod
#    def paroladan(cls):
#        mesaj = "Lütfen parolanızı giriniz."
#        cls(mesaj)
#        
#    @classmethod
#    def tcknden(cls):
#        mesaj = "TC No giriniz."
#        cls(mesaj)
#-----------------------------------------------------------------------
# yukarıdaki dınıfı bu şekilde de inşa edebiliyoruz.
#%%
from sistem import Giriş
Giriş.paroladan()
Giriş()
Giriş.tcknden()
# sınıf metotları içinde kullandığımız cls(mesaj) satırları Giriş() adlı sınıfı
# başka parametrelerle de çağırmamızı sağlıyor.
# bu sınıfın ön tanımlı değeri Müşteri numarası.
#%%      ----  Statik Metotlar  ----
# Eğer bir sınıf içindeki herhangi bir fonksiyonda örnek ya da sınıf niteliklerinin 
# hiçbirine erişmeniz gerekmiyorsa statik metotları kullanabilirsiniz.
#%%      ----  @staticmethod Bezeyicisi  ----
# matematik işlemleri yapmamızı sağlayan bir sınıf tanımlayalım.
#-------------------------------------------------------------------------
#class Mat():
#    
#    @staticmethod
#    def pi():
#        return 22/7
#    
#    @staticmethod
#    def karekök(sayı):
#        return sayı**0.5
#------------------------------------------------------------------------
# burda 2 adet statik metodumuz var pi() ve karekök().        
# statik metotları hem örnekler hem de sınıf adları üzerinden kullanabiliriz.   
# Mat sınıfını mat.py adlı dosyaya kaydediyoruz.ve modülü çağıralım.
from mat import Mat
m = Mat()
m.pi()# örnek üzerinden kullandık.
m.karekök(33)# örnek üzerinden kullandık.
Mat.pi()# sınıf üzerinden kullandık.
Mat.karekök(121)# sınıf üzerinden kullandık.
# statik metotları özellikle sınıf adları üzerinden kullanılabilmesi bu tür
# metotları epey kullanışlı hale getirir.Böylece sınıf örneklemek zorunda 
# kalmadan sınıf içindeki statik metotlara erişebiliriz.













   


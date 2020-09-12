# -*- coding: utf-8 -*-
#                            ------ NESNE TABANLI PROGRAMLAMA -----(DEVAMI)---

#                    -----  Nesneler  -----

# sınıflar nesene üretmemizi sağlayan veri tipleridir.
# şimdi ufak bir nesne üretelim.

#class Sınıf():
#    pass
#sınıf = Sınıf() # bu komut ile nesne üretmiş olduk.Nesnemizin adı da sınıf.

# yani sınıf örneği Sınıf() adlı sınıfın bütün nitelik ve metotlarını içinde 
# barındıran bir nesnedir.
# mesela yukarıdaki kodların sınıf.py adlı bir dosyada bulunduğunu varsayalım.

import sınıf
snf = sınıf.Sınıf()
# bu şekilde kodları içeren modülü içe aktarmış ve modül içindeki Sınıf() adlı
# sınıfı snf adı ile örneklemiş olduk.
print(dir(sınıf))
# biz boş bir sınıf tanımlamış olsakta snf nesnesi öntanımlı olarak bazı
# nitelik ve mototlara sahip.Python'da yukardaki gibi birtakım nitelik ve
# metotlara sahip olan ögelere nesne denir.

#%% şimdi bu sınıfın içine kendimiz birtakım nitelik ve metotlar tanımlamayı deneyelim. 

#class Sınıf():
#    sınıfNiteliği = "sınıf niteliği"
#    
#    def __init__(self):
#        self.örnekNiteliği = "örnek niteliği"
#        
#    def örnekMetodu(self):
#        print("örnek metodu")
#        
#    @classmethod
#    def sınıfMetodu(cls):
#        print("sınıf metodu")
#        
#    @staticmethod
#    def statikMetot():
#        print("statik metot")

# şimdi nesne içeriğini kontrol edelim.
import sınıf
snf = sınıf.Sınıf()
print(dir(snf))
# görüğümüz gibi bizim eklediğimiz nitelik ve metotlar snf adlı nesnenin içine eklenmiş.

#%%            ----  Basit Bir Oyun  ----

# oyunumuzun kodları şöyle.
#----------------------------------------------------------------------------
#import sys
#import random
#import time
#
#class Oyuncu():
#    def __init__(self,isim,can=5,enerji=100):
#        self.isim=isim
#        self.darbe=0
#        self.can=can
#        self.enerji=enerji
#        
#    def mevcutDurumuGörüntüle(self):
#        print("darbe:",self.darbe)
#        print("can:",self.can)
#        print("enerji:",self.enerji)
#        
#    def saldır(self,rakip):
#        print("Bir saldırı gerçekleştirdiniz.")
#        print("saldırı sürüyor bekleyiniz.")
#        
#        for i in range(10):
#            time.sleep(.3)
#            print(".",end="",flush=True)
#            
#        sonuç = self.sardırıSonucunuHesapla()
#        
#        if sonuç == 0:
#            print("\nSONUÇ:Kazanan taraf yok.")
#        if sonuç == 1:
#            print("\nSONUÇ:Rakibinizi darbelediniz.")
#            self.darbele(rakip)
#        if sonuç == 2:
#            print("\nSONUÇ:Rakibinizden darbe aldınız.")
#            self.darbele(self)
#        
#    def saldırıSonucunuHesapla(self):
#        return random.randint(0,2)
#    
#    def kaç(self):
#        print("Kaçılıyor...")
#        for i in range(10):
#            time.sleep(0.3)
#            print("\n",flush=True)
#        
#        print("Rakibiniz sizi yakaladı.")
#        
#    def darbele(self,darbelenen):
#        darbelenen.darbe += 1
#        darbelenen.enerji -= 1
#        if (darbelenen.darbe % 5) == 0:
#            darbelenen.can -= 1
#        if darbelenen.can < 1:
#            darbelenen.enerji = 0
#            print("{} oyunu kazandı.".format(self.isim))
#            self.oyundanÇık()
#    
#    def oyundanÇık(self):
#        print("Oyundan çıkılıyor...")
#        sys.exit()
#        
#######################################
#        
## Oyuncular
#siz = Oyuncu("Ahmet")
#rakip = Oyuncu("Mehmet")
#
## Oyun başlangıcı
#while True:
#    print("Şu anda rakibinizle karşı karşıyasınız.",
#          "Yapmak istediğiniz hamle:",
#          "Saldır: s",
#          "Kaç:  k",
#          "Çık:  q",sep="\n")
#    
#    hamle = input("\n> ")
#    if hamle == "s":
#        siz.saldır(rakip)
#        
#        print("Rakibinizin durumu.")
#        rakip.mevcutDurumuGörüntüle()
#        
#        print("Sizin durumunuz.")
#        siz.mevcutDurumuGörüntüle()
#        
#    if hamle == "k":
#        siz.kaç()
#        
#    if hamle == "q":
#        siz.oyundanÇık()
#--------------------------------------------------------------------------
# bir nesnenin hangi niteliklere sahip olacağını belirleyen veri tipine sınıf(class),
# o sınıfın ortaya çıkardığı ürüne ise nesne(object) denir.

#%%            ----  Herşey Bir Nesnedir  ----
"serhat"
type("serhat")
dir("serhat")
# "serhat" karakter dizisi str adlı sınıfın bütün özelliklerini taşıyan bir nesnedir.
type(["elma","armut"])
dir(["elma","armut"])
# ["elma","armut"] listesi list adlı sınıfın bütün özelliklerini taşıyan bir nesnedir.

#%%        ----  Birinci Sınıf Ögeler  ----
#**** bir nesnenin birinci sınıf olabilmesi için aşağıdaki şartlar sağlanmalı.
# mesela şöyle basit bir sınıf tanımlayalım
class Deneme():
    def __init__(self):
        self.değer=0
    def metot(self):
        self.metotDeğeri = 1
#**** bu sınıfın birinci sınıf nesne olabilmesi için başka bir fonksiyona veya
# başka bir sınıfa parametre olarak atanabilmesi gerekiyor.
print(Deneme())
# print() fonk. parametre olarak sınıfı atadık.
#**** yine birinci sınıf nesnelerin bir fonksiyondan dödürülebilmesi gerekiyor.
def fonksiyon():
    return Deneme()
print(fonksiyon())
# bu da oldu.
#**** son olarak bir nesnenin birinci sınıf olabilmesi için bir değişkene atanabilmeli.
değişken = Deneme()


















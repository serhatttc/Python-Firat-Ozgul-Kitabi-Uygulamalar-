# -*- coding: utf-8 -*-
#                            ------ NESNE TABANLI PROGRAMLAMA  ----(DEVAMI)---

#                   ----  Miras Alma  ----

# miras alma kavramı kodların tekrar tekrar kullanılabilmesi felsefesine katkı sunan özelliktir.
# diyelim ki bir oyun oynuyorsunuz.bu oyunun içinde askerler,krallar,kreliçeler
# bunu gibi oyuncu türleri bulunuyor.bunları ve kabiliyetlerini şöyle tanımlayalım.
class Asker():
    def __init__(self,isim,rütbe):
        self.isim = isim
        self.rütbe = rütbe
        self.güç = 100
        
    def hareketEt(self):
        .
        .
        .
    def puanKazan(self):
        .
        .
        .
    def puanKaybet(self):
        .
        .
        .
class İşçi():
    .
    .
    .
class Yönetici():
    .
    .
    .
# aynılarını bunlarada yazdık ve işlem tamam değere bakma değer ekleme biliyoruz zaten.
# ancak bu işlem uzun yani aynı şeylerş tekrar tekrar yazdık,Pythonvari hale getirelim.
#%%         ----  Taban Sınıflar  ----(base class)

# yukarıda verdiğimiz örneği tekrar önümüze alalım.    
# gelin şimdi bütün sınıflarda ortak olan nitelik ve metotları tek bir sınıf altında toplayalım.
class Oyuncu():
    def __init__(self,isim,rütbe):
        self.isim = isim
        self.rütbe = rütbe
        self.güç = 100
        
    def hareketEt(self):
        print("hareket ediliyor.")
        
    def puanKazan(self):
        print("puan kazanıldı.")
        
    def puanKaybet(self):
        print("puan kaybedildi.")
# işte burda Oyuncu() adlı sınıf taban sınıf olarak adlandırılır.
# taban sınıf, birkaç farklı sınıfta ortak olarak yer alan metot ve nitelikleri barındıran 
# bir sınıf türüdür.
#%%            ----  Alt Sınıflar  ----(subclass)
# bir taban sınıftan türeyen bütün sınıflar o taban sınıfının alt sınıfıdır.
# mesela yukarıdaki taban sınıfa bir alt sınıf üretelim
class Oyuncu():
    def __init__(self,isim,rütbe):
        self.isim = isim
        self.rütbe = rütbe
        self.güç = 100
        
    def hareketEt(self):
        print("hareket ediliyor.")
        
    def puanKazan(self):
        print("puan kazanıldı.")
        
    def puanKaybet(self):
        print("puan kaybedildi.")
class Asker(Oyuncu):# böyle yazarak Asker() sınıfı, Oyuncu() sınıfının alt sınıfı olmuş oluyor.
    pass
# Asker() adlı sınıf;1) Oyuncu() adlı sınıfı miras almış// 2) sınıfın bütün metot 
# ve niteliklerini devralmış// 3) sınıftan türemiş oluyor.
# bu sayede Oyuncu() sınıfında tanımlanan bütün metot ve niteliklere
# Asker() sınıfından da erişebiliyoruz.
# gelin birkaç alt sınıf daha ekleyelim.
class İşçi(Oyuncu):
    pass
class Yönetici(Oyuncu):
    pass

asker1 = Asker("Serhat","İstihkamcı")
işçi1 = İşçi("Ali","Tamirci")
asker1.hareketEt()

#%%             ----  Miras Alma Türleri  ----

# miras almada tek seçenek bütün metot ve nitelikleri olduğu gibi alt sınıfa
# aktarmak değildir.
# miras alınan metot ve niteliklerin alt sınıflar içinde nasıl tanımlanacağını,
# değiştirişebileceğini ve alt sınıflara nasıl yeni metot ve nitelikler ekleneceğine,
# örneklerle bakalım.

# şöyle bir kodumuz vardı.
#---------------------------------
#class Asker(Oyuncu):
#    pass
#--------------------------------
# şimdi biz bu sınıfa diğer sınıflardan farklı olarak memleket niteliği tanımlamak istiyorum.
class Asker(Oyuncu):
    memleket = "Bilecik"
    
    def örnekMetodu(self):
        pass
        
    @classmethod
    def sınıfMetodu(cls):
        pass
        
    @staticmethod
    def statikMetot(self):
        pass
# bu şekil herşeyi ekleyebiliriz.
# eğer alt sınıfa eklenen nitelik ve metot taban sınıfta zaten varsa, alt sınıfa
# eklenen nitelik ve metotlar taban sınıftaki nitelik ve metotların yerine geçecektir.

# mesela şimdi de taban sınıfta self.güç = 100 olarak kalsın istiyoruz ama 
# alt sınıflarda bunu değiştirmek istiyoruz.
# işte tam bu nokta da imdadımıza yeni bir fonksiyon yetişecek.
#%%             ----  super()  ----

# kodu şu şekilde yeniliyoruz.
class Oyuncu():
    def __init__(self,isim,rütbe):
        self.isim = isim
        self.rütbe = rütbe
        self.güç = 0
        
    def hareketEt(self):
        print("hareket ediliyor.")
        
    def puanKazan(self):
        print("puan kazanıldı.")
        
    def puanKaybet(self):
        print("puan kaybedildi.")
                           # isimli argüman olsa (**kwgars) yazardık.
class Asker(Oyuncu):        #  () içini şöylede yazabilirdik.
    def __init__(self,isim,rütbe): # (self,*args) 
        super().__init__(isim,rütbe) # (*args) 
        self.güç = 100
# Asker() sınıfında güç 100 olarak değiştirdik ve taban sınıfını etkilemedi.
#------------------------------
#  super().__init__(isim,rütbe)
#------------------------------
# bu satırda super() fonk. miras alınan üst(taban) sınıfın __init__() metodu
# içindeki kodların, miras alan alt sınıfın __init__() metodu içine aktarır.
asker = Asker("Serhat","Er")
asker.isim
asker.güç
o = Oyuncu("ali","ast")
o.güç
# super() fonk. Python'a sonradan eklenmiş bir dildir.Önceden onun yerine 
# taban sınıfın adı kullanılıyordu || Oyuncu().__init__(self,isim,rütbe) ||  gibi.
# bunda self. eklemek zorunda kaldık.
#%%
# super() fonksiyonunu sadece __init__() fonk. kullanmak zorunda değiliz.
# başka fonksiyonlar içinde de kullanabiliriz.
#--------------------------------------------------
def hareketEt(self):
    super().hareketEt()    
    print("hedefe ulaşıldı.")
#-------------------------------------------------
# işte burda super() sayesinde print() içindeki yazıyı değiştirdik.
#%%           ----  object Sınıfı  ----

# python 3.x 'ten onceki sürümlerde yeni tip sınıfları tanımlarken
class Sınıf(object):
    pass
# yapmalıyız yoksa  @property gibi yeni bir özelliktir bunu Python 2.x sürümlerinde
# kullanabilmek için böyle yapacağız.





















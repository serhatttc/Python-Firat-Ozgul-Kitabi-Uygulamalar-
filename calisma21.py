# -*- coding: utf-8 -*-
#                           -----  NESNE TABANLI PROGRAMLAMA  -----(DEVAMI)---

#                  ----  Sınıf Üyeleri  ----

# Python'da bir sınıf içinde bulunan nitelikler,metotlar,fonksiyonlar ve buna
# benzer veri tipleri o sınıfın ütelerini oluşturur.

#%%          ----  Aleni Üyeler  ----

# Eğer bir sınıf üyesi dışarıya açıksa yani bu üyeye sınıf dışından normal
# yöntemlerle erişilebiliyorsa bu tür üyelere 'aleni üyeler' denir.

# diyelim ki elimizde şöyle bir sınıf var.
#------------------------------------------------------------------------------
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
#-----------------------------------------------------------------------------
# bu kodların sınıf.py dosyasında yer aldığını varsayarsak şöyle birşey yazabiliriz.

import sınıf # modülü içe aktardık.
s = sınıf.Sınıf()# bu sınıfı s örneğine atadık.
dir(s)# bu sınıfın içeriğini sorguladık.

# biz bu sınıfın içindeki ögelere normal yollardan da erişme imkanına sahibiz.
s.statikMetot()
s.sınıfMetodu()
s.sınıfNiteliği
# işte içindeki bütün bu ögeler 'aleni üyeler'dir.

#%%             ----  Gizli Üyeler  ----

# ancak bazen bütün sınıf üyelerinin dışarıya açık olmasını istemeyebiliriz.
# bunun için onları dışa kapatarak 'gizli üye' haline getirebiliriz.
# Gizli üyelere normal yöntemlerle dışarıdan ulaşamayız.

# şimdi yukarıdaki sınıf örneğine şu değişikliği yapalım.
#---------------------------------------------------------------------------
#class Sınıf():
#    __gizli = "gizli"
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
#---------------------------------------------------------------------------
# burada '__gizli' adlı gizli bir sınıf niteliği tanımladık.

# işte Python'da '__gizli' gibi başında 2 adet alt çizgi olup ama sonunda
# alt çizgi bulunmayan ögeler 'gizli üye'dir.

import sinif
s = sinif.Sınıf()
s.__gizli# örnek adı üzerinden ulaşmayı denedik.
# gizli üyelere bu yaptığımız yöntemle ulaşamadık.
sinif.Sınıf.__gizli# sınıf adı üzerinden ulaşmayı denedik.
# gizli üyelere bu yaptığımız yöntemle de ulaşamadık.

# bir üyenin gizli olabilmesi için başında en az 2 adet '__' olmalı,sonunda
# en fazla 1 adet '_' olmalı.
# gizli üyeler sadece sınıf dışına kapalıdır.Sınıf içinden rahatlıkla erişebiliriz.

# şöyle yapalaım.sınıf içinde şöyle bir fonksşiyonumuz olsun.
#-------------------------------------------
#def örnekMetodu(self):
#    print(self.__gizli)
#    print("örnke metodu")

# import sinif
# s = sinif.Sınıf()  
# s.örnekMetodu()  # bu 'gizli' ve 'örnek metodu' çıktısı verir.
#-------------------------------------------
# sınıfımızı içe aktardık örnekledik ve örnek metodu üzerinden gizli üye olan
# __gizli'ye de erişmiş oluyoruz.

#%%          ----  İsim Bulandırma  ----

# python da ne kadar gizli öge var desekte erişilemeyen öge yoktur.Gerçek anlamda
# dışa kapalı sınıf üyeleri bulunmadığı gibi bu üyelere bir şekilde erişme imkanımız var.

# şimdi yukarda yaptığımız örnek sınıfımıza bakalım.

import sinif
s = sinif.Sınıf()
s._Sınıf__gizli # böyle yazarak gizli üye olan '__gizli' sınıf niteliğine eriştik.

#%%          ----  Yarı-Gizli Üyeler  ----

# şu şekil oluşturuluyor.
class Falanca():
    _yarıGizli = "yarı-gizli"
# bu niteliğe sınıf içinden veya dışından ulaşmamızı engelleyen bir mekanizma yoktur.
# ama biz sınıf içinde bu tek alt çizgiyi görünce sınıfın iç işleyişine 
# ilişkin bir ayrıntı olduğunu ve bunu dışarıdan değiştirmememiz gerektiğini anlarız.
    
#%%        ----  @property Bezeyicisi  ----

# yarı-gizli ögelerin kullanıldığı bir örnek verelim.
# diyelim ki şöyle bir kod yazdık.
#------------------------------------------------------------------------------   
#class Çalışan(): # öncelikle sınıfı tanımlıyoruz.
#    personel = [] # personel adlı sınıf niteliği ekliyoruz.
#    
#    def __init__(self,isim):
#        self.isim = isim# isim parametresini sınıfın başka bölgelerinde de kullanmak için yaptık.
#        self.personelEkle()
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
#------------------------------------------------------------------------------    
# burdaki metotları şöyle kullanıyoruz.
from calisan import Çalışan
c1 = Çalışan("Ahmet")
c2 = Çalışan("Mehmet")
    
Çalışan.personeliGoruntule() 
#%%    
# peki eğer kodlarımızı kullananlar personel listesindeki bir kişinin ismini 
# sonradan değiştirmek isterse ne yapacak??   
# kodlarımız içinde isim değişikliği yapılmasını sağlayan özel bir metot yok.
# dolayısıyla kodlarımızı kullananlar doğrudan isim adlı örnek değişkenine
# erişerek isim değişikliğini şu şekil yapabilir.

c1.isim = "Serhat" # değişikliği yaptık.
print(c1.isim) # teyit ettik ve oldu.
# yalnız bu deişiklik personel listesine yansımadı gelin isterseniz bakalım.
Çalışan.personeliGoruntule()   
# görüğümüz gibi Ahmet ismi hala orada duruyor bunu gidermek için personel
# listesinede müdahale edilmesi gerekir.
kişi = Çalışan.personel.index("Ahmet")
Çalışan.personel[kişi] = "Serhat"  
    
Çalışan.personeliGoruntule()    
#%%    
# fakat bir isim değiştimek için bu kadar uğraşmak gereksiz.Pratik bir metot sunalım.    
# bu sınıfa isimDegistir() adlı bir sınıf metodu ekleyelim.    
#----------------------------------------------------------------------------
#class Çalışan(): # öncelikle sınıfı tanımlıyoruz.
#    personel = [] # personel adlı sınıf niteliği ekliyoruz.
#    
#    def __init__(self,isim):
#        self.isim = isim# isim parametresini sınıfın başka bölgelerinde de kullanmak için yaptık.
#        self.personelEkle()
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
#    def isimDegistir(self,yeniİsim):
#        kişi = self.personel.index(self.isim)
#        self.personel[kişi] = yeniİsim
#        print("yeni isim :",yeniİsim)
#-----------------------------------------------------------------------------            
# kullanıcılar personel listesine önceden ekledikleri kişileri kolayca değiştirebilecek.    
from calisan import Çalışan
c1 = Çalışan("Ahmet")
c2 = Çalışan("Mehmet")
c3 = Çalışan("Serdar")
Çalışan.personeliGoruntule()   
    
c2.isimDegistir("Serhat")    
Çalışan.personeliGoruntule()
    
#%% acaba personle listesindeki bir ismi yaknızca şöyle bir komut vererek değiştiremez miyiz??
# c1.isim = "Serap"    
# elbette değiştirebliriz. ama @property adlı bir araçtan yararlanıcaz.   
#---------------------------------------------------------------------------    
#class Çalışan(): # öncelikle sınıfı tanımlıyoruz.
#    _personel = [] # personel adlı sınıf niteliği ekliyoruz.
#    
#    def __init__(self,isim):
#        self._isim = isim# isim parametresini sınıfın başka bölgelerinde de kullanmak için yaptık.
#        self._personelEkle()
#        
#    def personelEkle(self):
#        self._personel.append(self._isim)
#        print("{} adlı kişi personele eklendi.".format(self._isim))
#        
#    @classmethod    
#    def personeliGoruntule(cls):
#        print("Personel Listesi : ")
#        for kisi in cls._personel:
#            print(kisi)
#            
#    @property
#    def isim(self):
#        return self._isim
#    
#    @isim.setter
#    def isim(self,yeniİsim):
#        kişi = self._personel.index(self._isim)
#        self._personel[kişi] = yeniİsim
#        print("yeni isim :",yeniİsim)    
#------------------------------------------------------------------------------    
# kodları böyle yazığımızda,
# c1.isim = "Serap"
# herhangi bir çalışanın ismini böyle değiştirebilicez.
# üstelik bu kod değişikliğin personel listesine de yansımasını sağlıyor.

#%%          ----  Metottan Niteliğe  ----

# öncelikle @property bezeyicisini tanıyalım.
# @ property bezeyicisinin yaptığı en temel iş bir metodu, nitelik gibi
# kullanılabilir hale getirmektir.
# basit bir örnek verelim.

class Program():
    def __init__(self):
        pass
    def versiyon(self):
        return '0.1'

# burada versiyon() adlı bir örnek metodu tanımladık.Bu programı şöyle kullanıyoruz.
program = Program()
program.versiyon()
#%% şimdi programımızda şu değişikliği yapalım.
class Program():
    def __init__(self):
        pass
    @property
    def versiyon(self):
        return '0.1'
# burada versiyon() adlı metodu @property bezeyicisi ile bezedik.Böylecce bu 
# metodu bir 'nitelik' haline getirmiş olduk.
# artık bunu şöyle kullanabiliriz.
program = Program()
program.versiyon
# bu fonksiyonu niteliğe dönüştürdüğümüz için parantezsiz kullandığımıza dikkat edin.
#%% peki neden bir metodu niteliğe dönüştürmek istiyor olabiliriz.
# şöyle bir program yazdığımızı düşünün.
class Program():
    def __init__(self):
        self.data = 0
# yazdığımız bu programı kullananlar sınıf içindeki data niteliğine şu şekide erişiyor.
p = Program()
p.data
# hatta duruma göre bu niteliği şu şekilde değişikliğe uğratıyor.
p.data = 1
p.data
#%% günün birinde 'data' kelimesi yerine 'veri' kelimesi kullanmak daha uygun 
# olduğunu düşünerek 'data' kelimesini 'veri' olarak değiştirdiğimizi varsayalım.
# ancak böyle yaparsak eskiden beri bu programı kullananların oluşturdukları 
# programı kullanılamaz hale getirmiş oluruz.
# bunu düzeltmek için @property bezeyicisini kullanalım.
class Program():
    def __init__(self):
        self.veri = 0
    @property
    def data(self):
        return self.veri
# böylelikle self.veri ile self.data birbirine bağlamış olduk.
# self.veri üzerinde yapılan değişiklikler self.data niteliğine de yansır.
p = Program()
p.data
p.veri
p.veri = 5
p.data
#%%         ----  Salt Okunur Nitelikler  ----
# yukarıdaki programı temel alarak şöyle birşey deneyelim
p.data =6
# gördüğünüz gibi data niteliği üzerinden değişiklik yapamıyoruz.Dolayısıyla
# kullananların değiştirmesini istemediğiniz 'salt okunur' nitelikler oluşturmak
# için @property bezeyicisinden yararlanabiliriz.

#%%        ----  Veri Doğrulaması  ----

# @property bezeyicisinin 3 görevi vardır; 1) Değer döndürmek// 2) Değer atamak,
# 3) Değer silmek 
# yukarıdaki örnekte değer döndürmeyi görmüştük.Şimdi değer atamaya bakalım.

# elimizde şöyle bir kod olduğunu varsayalım
class Program():
    def __init__(self):
        self.sayı = 0
# daha sonra bir sebepten ötürü self.sayı niteliğine erişimi kısıtlayıp bu nitelik
# üzerinden değişiklik yapılamaz hale getirmek için @property'den yararlanalım.
# öncelikle self.sayı niteliğine erişimi kısıtladığımızı belli etmek için self._sayı
# yaptık.hemde sayı() fon. ile karışmasın diye önlem aldık.
class Program():
    def __init__(self):
        self._sayı = 0
    @property
    def sayı(self):
        return self._sayı
#%% bu şekilde sayı niteliğini salt okunur hale getirdik.eğer amacımız değişkeni 
# salt okunur hale getirmek değilse bir setter parametresi kullanabiliriz.
class Program():
    def __init__(self):
        self._sayı = 0
    @property
    def sayı(self):
        return self._sayı
    @sayı.setter
    def sayı(self,yeniDeğer):
        self._sayı = yeniDeğer
        return self._sayı        

p = Program()
p.sayı
p.sayı = 5
p.sayı
# .setter bezeyicisi ile sayı niteliği üzerinde değişiklik yapabiliyoruz. 
#%% .setter bezeyicisini doğrulama işlemleri yapmak içinde kullanabiliriz.
class Program():
    def __init__(self):
        self._sayı = 0
    @property
    def sayı(self):
        return self._sayı
    @sayı.setter
    def sayı(self,yeniDeğer):
        if yeniDeğer % 2 == 0:
            self._sayı = yeniDeğer
        else:
            print("çift değil.")
            
        return self.sayı
# buna göre eğer self.sayı niteliğine girilen sayı çift ise değişiklik kabul ediliyor.
# çift değil ise "çift değil" hatası veriyoruz.
p = Program()
p.sayı = 2
p.sayı = 5 # 5 tek olduğu için kabul etmedi.Ekleyemedik.
p.sayı
# bu arada .setter dışında .deleter adlı özel bir @poperty bezeyicisi daha bulunur.
#%% bunu da bir değeri silmek için kullanıyoruz.
class Program():
    def __init__(self):
        self._sayı = 0
    @property
    def sayı(self):
        return self._sayı
    @sayı.setter
    def sayı(self,yeniDeğer):
        if yeniDeğer % 2 == 0:
            self._sayı = yeniDeğer
        else:
            print("çift değil.")
            
        return self.sayı
    
    @sayı.deleter
    def sayı(self):
        del self._sayı
# @property bezeyicisini kullanarak 3 ayrı metot tanımladık.
# ilgili niteliğe nasıl ulaşacağımızı gösteren bir metot:@property ile
# ilgili niteliği nasıl ayarlayacağımızı gösteren bir metot:.setter ile
# ilgili niteliği nasıl sileceğimizi gösteren bir metot:.deleter ile beziyoruz.










# -*- coding: utf-8 -*-

#def personelSayisi():# bu metot sınıf niteliği olan personele erişerek
    #print(len(Çalışan.personel)) # bunun uzunluğunu ekrana basıyor.

# bu fonk. sınıftan ayırıp modül düzeyinde çalışan bir fonk. haline getirdik.Artık
# bu fonk. Çalışan sınıfının hiçbir örneğine bağlı değil.Dolayısıyla bu fonk. Çalışan sınıfı
# için bir örnek çıkarmak zorunda kalmadan kullanabiliyoruz.
# bu da bize personel sayısının 0 olma durumunu göstermemize imkan veriyor.

#class Çalışan(): # öncelikle sınıfı tanımlıyoruz.
#    personel = [] # personel adlı sınıf niteliği ekliyoruz.
#    
#    def __init__(self,isim):
#        self.isim = isim# isim parametresini sınıfın başka bölgelerinde de kullanmak için yaptık.
#        self.kabiliyetleri = []
#        self.personelEkle()# bu üçü örnek nitelikleri.
#    
#    def personelSayisi(self):
#        print(len(self.personel))
#    
#    
#    def personelEkle(self):# örnek methodu olan bu fonk. tanımladık.
#        self.personel.append(self.isim)
#        print("{} adlı kişi personele eklendi.".format(self.isim))
#        
#    def personeliGoruntule(self):# örnek metodu
#        print("Personel Listesi : ")
#        for kisi in self.personel:
#            print(kisi)
#            
#    def kabiliyetEkle(self,kabiliyet):# örnek metodu
#        self.kabiliyetleri.append(kabiliyet)
#            
#    def kabiliyetleriGoruntule(self):# örnek metodu
#        print("{} adlı kişinin kabiliyetleri: ".format(self.isim))
#        for kabiliyet in self.kabiliyetleri:
#            print(kabiliyet)

# örnek metotları bir sınıfın örnekleri vasıtasıyla çağırılabilen fonksiyonlardır.
# örnek methodlarına sınıf dışından örnek isimleri ile(ahmet,mehmet) sınıf içinden 
# ise örnek isimlerini temsil eden self kelimesiyle erişebiliyoruz.            
# şimdi bu sınıfa personel sayısını gösteren örnek metodu daha tanımlayalım.          
    
class Çalışan(): # öncelikle sınıfı tanımlıyoruz.
    personel = [] # personel adlı sınıf niteliği ekliyoruz.
    
    def __init__(self,isim):
        self.isim = isim# isim parametresini sınıfın başka bölgelerinde de kullanmak için yaptık.
        self.kabiliyetleri = []
        self.personelEkle()
    
    @classmethod
    def personelSayisi(cls):
        print(len(cls.personel))
    
    
    def personelEkle(self):
        self.personel.append(self.isim)
        print("{} adlı kişi personele eklendi.".format(self.isim))
    
    @classmethod    
    def personeliGoruntule(cls):
        print("Personel Listesi : ")
        for kisi in cls.personel:
            print(kisi)
            
    def kabiliyetEkle(self,kabiliyet):
        self.kabiliyetleri.append(kabiliyet)
            
    def kabiliyetleriGoruntule(self):
        print("{} adlı kişinin kabiliyetleri: ".format(self.isim))
        for kabiliyet in self.kabiliyetleri:
            print(kabiliyet)


















        
            
# -*- coding: utf-8 -*-
#                          -------  NESNE TABANLI PROGRAMLAMA (OOP)  -------

#                 --- SINIFLAR ---

class harfSayaci:
    def __init__(self):
        self.sesliHarfler = "aeıioöuü"
        self.sayac = 0
    
    def kelimeSor(self):
        return input("Kelime girin :")
    
    def seslidir(self,harf):
        return harf in self.sesliHarfler
    
    def artir(self):
        for harf in self.kelime:
            if self.seslidir(harf):
                self.sayac += 1
        return self.sayac
    
    def ekranaBas(self):
        mesaj = "{} kelimesinde {} sesli harf var."
        sesliHarfSayisi = self.artir()
        print(mesaj.format(self.kelime,sesliHarfSayisi))
    
    def calistir(self):
        self.kelime = self.kelimeSor()
        self.ekranaBas()
    
if __name__ == "__main__":
    sayac = harfSayaci()
    sayac.calistir()
    
#%%                ---- Sınıf Tanımlamak  ----
class Çalışan: # bu boş bir sınıf tanımıdır.Çalışan(): yapıpta tanımlayabilirdik.
    pass
#%%               ----  Sınıf Nitelikleri  ----   
class Çalışan():
    kabiliyetleri = []
    unvani = "işçi"
# kabiliyetleri ve unvani adlı iki değişken tanımladık.
# Teknik dilde bu değişkenlere sınıf niteliği(class attribute) denir.
    maasi = 1500
    memleketi = " "
    dogumTarihi = " "

print(Çalışan.unvani)
print(Çalışan.kabiliyetleri)
print(Çalışan.memleketi)
# eğer istersek bu sınıfa yeni niteliklerde ekleyebiliriz.
Çalışan.isim = "serhat"
#%%              ----  Sınıfların Örneklenmesi  ---- 
class Çalışan():
    kabiliyetleri = []
    unvani = "işçi"
    maasi = 1500
    memleketi = " "
    dogumTarihi = " "

serhat = Çalışan() # burada sınıfımızı serhat adlı bir değişkene atadık.
# bu işleme teknik dilde örnekleme (instantiation) denir.
# bu şekilde sınıfı kullanışlı hale getirdik.

# başka bir sınıf daha oluşturalım.
class Asker():
    rutbesi = "Er"
    standartTechizat = ["G3","kasatura","el bombası","süngü"]
    gücü = 60
    birligi = ""
# şimdi bu sınıfa serdar adlı bir referans noktası oluşturalım.
serdar = Asker()
# biz bu şekilde bu sınıfın bütün niteliklerini barındıran üye meydana getirmiş oluyoruz.
# biz sınıfı örnekleyip(instantiation) serdar adlı bir örneğe(instance) atamış olduk.
# serdar, Asker adlı sınıfın örneği olmuş oluyor.
# bir sınıftan istediğimiz kadar örnek çıkarabiliriz.
ahmet = Asker()
nimet = Asker()
# bu sınıf örneklerini kullanarak sınıfın niteliklerine(attribute) erişebiliriz.
ahmet.rutbesi
# biz sınıfı hiç örneklemeden direkt sınıf adıylada niteliklere ulaşabiliriz.
Asker.rutbesi

#%%   gelin şimdi ufak tefek uygulamalar yapalım.
# sınıfımız şu olsun.
#class Asker():
#    rutbesi = "Er"
#    standartTechizat = ["G3","kasatura","el bombası","süngü"]
#    gücü = 60
#    birligi = ""
# bu sınıfı asker.py adlı dosyaya kaydettik ve burda asker.py dosyasını modül gibi içe aktaralım. 
import asker # modülü içe aktardık.
print(dir(asker))# erişim sağladığımızı teyit ettik.İçeriğine ulaştık.
# şimdi bu sınıfı örnekleyerek kullanılabilir hale getirelim.
bilecik = asker.Asker()
# hadi bir de bilecik örneğinin(instance) içeriğine bakalım.
print("-"*50)
print(dir(bilecik))
# gördüğünüz gibi sınıf içindeki bütün nitelikler bu listenin içinde var.
# bu niteliklerden 'standartTechizat' olanı kullanıp teçhizatı belirledik.
bilecik.standartTechizat = "Deagle"
#%% bir uygulama daha elimizde şöyle bir sınıf olsun.
class Çalışan():
    kabiliyetleri = []
    unvani = "işçi"
    maasi = 1500
    memleketi = " "
    dogumTarihi = " "
# Çalışan sınıfı içindeki niteliklere erişmek için birkaç tane örnek çıkaralım.
serhat = Çalışan()
ahmet = Çalışan()
nimet = Çalışan()
serhat.maasi
# böylelikle 3 farklı örneği oluşturmuş olduk.
# bu örneklerle sınıf niteliklerinde değişiklikler yapabiliyoruz.
serhat.kabiliyetleri.append("prezantabl")
# bu değişikliğin eklendiğini teyit edelim.
serhat.kabiliyetleri# eklenmiş.
# şimdi Çalışan sınıfının bir başka örneğini oluşturalım.
ali = Çalışan()
ali.kabiliyetleri# bu da ahmetle aynı oldu || ['prezantabl']  ||  çıktısı.

#%%                    ----  Örnek Nitelikleri  ----
# burada yukarda her örneğe eklenen ['prezantabl'] gibi çıktının sadece istediğimize
# eklenmesini sağlayacağız.
#%%     ----  __init Fonksiyonu Ve self  ----  

# örnek niteliklerini tanımlamak için bu ikiliden yararlanırız.
# bu şekilde kullanabiliriz.
class Çalışan():
    def __init__(self):# '__init__'in ilk parametresi 'self' olmak zorunda.
        self.kabiliyetleri = []
# sınıf nitelikleri sınıf çağırılmadan çalışmaya başlar, ama örnek nitelikleri çağırılır.
        print(self.kabiliyetleri)
# bu kodları çalıştırdığımızda herhengi bir çıktı almayız.Bu kodların çıktı 
# verebilmesi için sınıfı mutlaka örneklemeliyiz.
serhat = Çalışan()
print(serhat.kabiliyetleri)
# işte self kelimesi yukardaki kodda yer alan serhat kelimesini temsil ediyor.
# bu kodu yazabilmemizi sağlayan self'tir.
#%% şimdi aynı kodları bir de şöyle yazalım.
class Çalışan():
    kabiliyetleri = [] # sınıf niteliği
    
    def __init__(self):
        self.kabiliyetleri = [] # örnek niteliği

serhat = Çalışan()
serhat.kabiliyetleri # bu çıktı ilk olarak örnek niteliğini verir.
# eğer biz sınıf niteliğin erişmek istersek sınıf örneğini değil sınıf adını kullanacaz.
Çalışan.kabiliyetleri # bu sınıf niteliğini verir.

# örnek nitelikleri sadece fonksiyon içinde tanımlanabilir.

# self kelimesi ancak ve ancak içinde geçtiği fonksiyonun parametre listesinde
# ilk sırada kullanıldığında anlam kazanır.

#%%    ---  Örnek Metotlar ----

#class Çalışan():
#    personel = []
#    
#    def __init__(self,isim):
#        self.isim = isim
#        self.kabiliyetleri = []
#        self.personelEkle()
#        
#    def personelEkle(self):
#        self.personel.append(self.isim)
#        print("{} adlı kişi personele eklendi.".format(self.isim))
#        
#    def personeliGoruntule(self):
#        print("Personel Listesi : ")
#        for kisi in self.personel:
#            print(kisi)
#            
#        def kabiliyetEkle(self,kabiliyet):
#            self.kabiliyetleri.append(kabiliyet)
#            
#        def kabiliyetleriGoruntule(self):
#            print("{} adlı kişinin kabiliyetleri: ".format(self.isim))
#            for kabiliyet in self.kabiliyetleri:
#                print(kabiliyet)

# bu kodları yazıp çalışan.py adlı dosyaya kaydettik.
# şimdi onu buraya modül olarak içe aktarıcaz.
import çalışan
# daha sonra sınıfımızın iki farklı örneğini çıkaralım.
c1 = çalışan.Çalışan("Ahmet")
c2 = çalışan.Çalışan("Mehmet")
c1.isim # Ahmet çıktısı verdi.
c2.isim# Mehmet çıktısı verdi.
# bu nitelikleri değiştirebiliriz de.
c1.isim = "Serhat"
c1.personel[0] = "Serhat"
# ilk çalışanın ismini Serhat olarak değiştirdik.
c1.personel

c1.kabiliyetEkle("prezantabl")
c1.kabiliyetEkle("konuşkan")
c1.kabiliyetleriGoruntule()

c2.kabiliyetEkle("girişken")
c2.kabiliyetleriGoruntule()

# gördüğünüz gibi bir sınıf örneğine eklediğimiz kabiliyet diğer sınıf örneğini etkilemiyor.
# bu örnek niteliklerinin sınıf niteliklerinden büyük bir farkıdır.

# sınıf örneklerimizin herhengi biri üzerinden personel listesine de ulaşabiliriz.
c1.personeliGoruntule()








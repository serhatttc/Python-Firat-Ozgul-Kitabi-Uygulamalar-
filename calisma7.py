# -*- coding: utf-8 -*-
                # •       KARAKTER DİZİLERİ
nesne = "python"
print(len(nesne))
print(nesne[0])
print(nesne[1])
print(nesne[2])
print(nesne[3])
print(nesne[4])
print(nesne[5])
print(nesne[-1]) #. bu da tersten okumamızı sağlar.
print(nesne[-2])
print(nesne[-3])
print(nesne[-4])
print(nesne[-5])
print(nesne[-6])

# eğer karakter dizisinin uzunluğunu aşan bir sayı verirsek.'IndexError' türünde
#  bir hata verecek
for i in range(6): # bu şekilde de yazılabilir.
    print(nesne[i])
# uzunluğunu bilmediğimiz karakter dizileri için len() ve range() den yararlanırız.
#%%
nesne = "jashbfjasdgasfjasdjfkshfjaksfşjkasdşaskfsafaksdşajg"
print(len(nesne))
for i in range(51):
    print(nesne[i])
# böyle de yazılabilir.
for karakter in range(len(nesne)):
    print(nesne[karakter])
#%%
name = input("isminiz : ") 
for i in range(len(name)):
    print("isminizin {}. harfi : {}".format(i+1,name[i]))   
#%%         KARAKTER DİZİLERİNİ DİLİMLEMEK
site = "www.google.com"
print(site[4:10])# alınacak ilk ögenin sırası:alınacak son ögenin sırasının 1 fazlası.
#%%
site1 = "www.google.com" 
site2 = "www.yahoo.com"
site3 = "www.youtube.com"    
for isim in (site1,site2,site3):
    print("site : ",isim[4:-4]+"...")# ilk 4 ve son 4 karakterler hariç dedik.
 #  [ilk sayı:ikinci sayı] ilk sayıyı yazmazsak python onu 0 olarak algılar.   
 #  ikinci sayıyı yazmazsak sonuna kadar alır.
#%%                 KARAKTER DİZİLERİNİ TERS ÇEVİRMEK
sentence = "Herkes öldürü sevdiğini."
print(sentence[::-1]) # tersten yazmamızı sağladı.
#%%
print(reversed("herkes öldürür sevdiğini."))
#for i in reversed("herkes öldürür sevdiğini."):
#    print(i,end="")# normaşde alt alta sıralar end="" yapınca düzelir.
print(*reversed("herkes öldürür sevdiğini.") ,sep="") # bu da aynısı.
#%%         KARAKTER DİZİLERİNİ ALFABE SIRALARINA DİZMEK
print(sorted("serhat")) 
print(*sorted("serhat"))
print(*sorted("serhat"),sep="")
# bu türkçe harfleri düzgün sıralamaz onun için aşağıdaki olayı yapmalıyız.
import locale
locale.setlocale(locale.LC_ALL,"Turkish_Turkey.1254")
print(sorted("çiçek",key=locale.strxfrm))
# buraya kadar olan sıkıntı da 'i' harfi 'ı' harfinden önce geliyor ama bizim 
# alfabade öyle değil bunu düzeltmek için aşağıdakini yapıcaz.
hafler = "abcçdefgğhıijklmnoöprsştuüvyz"
cevrim = {i:hafler.index(i) for i in hafler}
print(sorted("asdgasiı",key=cevrim.get))
#%%         KARAKTER DİZİLERİ ÜZERİNDE DEĞİŞİKLİK YAPMAK
meyve = "elma"
print("E"+meyve[1:])   

site1 = "www.google.com"
site2 = "www.yahoo.com"
site3 = "www.youtube.com" 

for i in (site1,site2,site3):
    print("http://",i,sep="")
    
karDiz = "serhat"
print(karDiz[:3]+"H"+karDiz[4:])
#%% sesli ve sessiz harfleri birbirinden ayıran program
sesliHarfler = "aeioüuıiö"
sessizHarfler = "bcçdfgğhjklmnprsştvyz"

sesliler = ""
sessizler = ""

kelime = input("kelime giriniz : ")

for i in kelime:
    if i in sesliHarfler:
        sesliler +=i
    else:
        sessizler +=i
print("sesli hafler : ",sesliler)
print("sessiz hafler : ",sessizler)
#%%

print(dir(str))    
for i in dir(""):
    if "_" not in i[0]:
        print(i)
#%%
sayac = 0
for i in dir(""):
    if "_" not in i[0]:
        sayac +=1
        print(i)
print("Toplam {} adet metodla ilgileniyoruz.".format(sayac))
#%%

print(*enumerate("serhat"),sep="\n")
#  Bunların ikisi aynı şeyler.
for i in enumerate("serhat"):
    print(i)
#%%
for sira,metot in enumerate(dir(""),1):# saymaya 0'dan değil 1'den başla dedim.
    print(metot,sira)
#%%
print(help()) # enter'a basıp yada 'quit' yazıp çıkabiliriz.
#%%
trHarfler = "İüğçöş"  
a = 0
while a<len(trHarfler):
    print(trHarfler[a],sep="\n")
    a +=1
# bunun aynısını for dögüsü ile de yazabiliriz.
trHarfler = "İüğçöş"
for trHarf in trHarfler:
    print(trHarf)
#%%
import sys
major = sys.version_info[0]
minor = sys.version_info[1]
micro = sys.version_info[2]   
print(major,minor,micro,sep=".")

print(sys.version_info)
#%%                 KARAKTER DİZİLERİNİN METOTLARI    
name = "serhat" 
print(name.replace("e","E"))# 'e'yi 'E'ye çevirdik.
# karakterDizisi.metot(parametre) gösterimi böyledir.Bu yönteme
# notalı gösterim (dot notation)  
#%%                        replace
city = "memleket"
print(city.replace("e","")) # bütün e'leri etkiledi.
print(city.replace("e","",2)) # sadece ilk 2 e harfini etkiledi.
#%%                            split
name = "Eskişehir Büyükşehir Belediyesi"
print(name.split())
for i in name.split():# normalde boşluk gördüğü yerden ayır demek.
    print(i)
isim = "Eskişehir Büyükşehir Belediyesi"
for i in isim.split():
    print(i[0],end=".\n")
karDiz = "serhat,serdar,serap,ahmet,nimet"
karDiz = karDiz.split(",")# ',' gördüğün yerden ayır demek.
print(karDiz)
for i in karDiz:
    print(i)
sentence = "Türkiye Büyük Millet Meclisi"
print(sentence.split(" ",1))# 1 kere böl demek.
import sys
surum = sys.version
print(surum.split())
#%%                        rsplit
# bölme işlemini yapmaya tersten başlıyor.
name = "serhat,serdar,serap,ahmet,nimet"
print(name.rsplit(",",1))
#%%                     splitlines
text = """Python, nesne yönelimli, yorumlamalı, birimsel (modüler) ve 
etkileşimli yüksek seviyeli bir programlama dilidir.[4]
Girintilere dayalı basit sözdizimi, dilin öğrenilmesini ve 
akılda kalmasını kolaylaştırır. Bu da ona söz diziminin ayrıntıları 
ile vakit yitirmeden programlama yapılmaya başlanabilen bir dil olma 
özelliği kazandırır.Modüler yapısı, sınıf dizgesini (sistem) ve 
her türlü veri alanı girişini destekler. Hemen hemen her türlü 
platformda çalışabilir. (Unix , Linux, Mac, Windows, Amiga, Symbian). 
Python ile sistem programlama, kullanıcı arabirimi programlama, 
ağ programlama, web programlama, uygulama ve veritabanı yazılımı 
programlama gibi birçok alanda yazılım geliştirebilirsiniz. Büyük 
yazılımların hızlı bir şekilde prototiplerinin üretilmesi ve denenmesi 
gerektiği durumlarda da C ya da C++ gibi dillere tercih edilir."""
print(text.splitlines())# satırlardan ayırır.
#%%                                 lower
name = "SeRhAt"
print(name.lower())
#  lower 'I've'İ'de sıkıntı çıkarır.Onu da böyle düzelttik.
iller = "ISPARTA,ADIYAMAN,BİLECİK"
iller = iller.replace("I","ı").replace("İ","i").lower()
print(iller)
#%%                                 upper
name = "serhat"
print(name.upper())
# lower daki 'i' sıkıntısı burda da var aynı şekilde çözüyoruz.
iller = "bilecik,izmir,istanbul"
iller = iller.replace("i","İ").upper()
print(iller)
#%%                                islower
name = "serhat"
print(name.islower()) # hepsi küçük harf mi? sorusu sorduk.||True  çıktısı verdi.
isim = "SErhat"
print(isim.islower())
#%%                               isupper
name = "serhAT"
print(name.isupper()) # hepsi büyük harf mi? sorusu sorduk.||False  çıktısı verdi.
isim = "SERHAT"
print(isim.isupper())
#%%                            endswith
name = "serhat"
print(name.endswith("t"))# dizinin sonu bununla mı bitiyor diye sorduk.
print(name.endswith("hat"))
#%%                              startswith
name = "serhat"
print(name.startswith("s")) # dizinin başı bununla mı başlıyor diye dorduk.
print(name.startswith("ser"))
#%%                             capitalize
a = "serhat çağlar"
print(a.capitalize())
#%%                                title
a = "python programlama dili"
print(a.title())
#%%                              swapcase
name = "SerhaT"
print(name.swapcase())
#%%                            strip
a = "serhat çağlar"
print(a.strip("s"))
#%%                          lstrip
a = "kazak"
print(a.strip("k"))
b = "kazak"
print(b.lstrip("k"))
#%%                           rstrip
a = "kazak"
print(a.rstrip("k"))
#%%                             join
a = "Beşiktaş Jimnastik Kulübü"
bolunmus = a.split()
print(bolunmus)
print(" ".join(bolunmus))
#%%                            count
a = "herkes öldürür sevdiğini ama herkes öldürdü diye ölmez."
print(a.count("ü"))
b = "adana"
print(b.count("a",1))# burdaki 1 saymaya kaçıncı sıradan başlıcağını söylüyor.
c = "python programlama dili"
print(c.count("a",15,17)) # 15. ve 17. sıra arasındaki a harflerini saydırdık.
#%%                              index
a = "python"
print(a.index('t'))
b = "adana"
print(b.index("a",3))# 3 parametresi keçıncı sıradan başlaması gerektiğini söylüyor.
c = "adana"
print(c.index("a",1,3))# burdaki 1 ve 3 parametreleri aralık belirtiyor.
#%%                           rindex
a = "adana"
print(a.rindex("a"))
#%%                            center
for metot in dir(""):
    print(metot.center(15))# 15 parametresi karakter dizisinin ne kadar
#  yer kaplıcağını gösterir. ne kadar ortalanacağını.
#%%                           rjust ||  ljust
for i in dir(""):
    print(i.rjust(30))
a = "serhat"
print(a.ljust(10,".")) # 10 karakterlik alanın içine 6 karakterlik 'serhat' 
#  geriye kalan 4 karaktere '.' geliyor.
#%%                                 zfill
a = "12"
print(a.zfill(5))# 5 karakterlik alanın 2 karakterini '12' kalan 3 karaktere '0' gelir.
#%%                      partition  ||  rpartition
a = "bilecik"
print(a.partition("l"))

b = "serhat"
print(b.rpartition("a"))# sağdan sola okur.
#%%                            encode
print("çilek".encode("cp1254"))
#%%                         expandtabs
a = "elma\tbir\tmeyvedir"
print(a.expandtabs(10))# toplam boşluk sayısı 10 oluyor.
#%%      str.maketrans,translate
kaynak = "şçöğüıŞÇÖĞÜİ" # kaynaktaki harfler hedefteki harflerle tek tek değişti.
hedef = "scoguiSCOGUI"
ceviriTablosu = str.maketrans(kaynak,hedef)
metin = "Bildiğiniz gibi internet üzerinde bazen Türkçe karakterleri kullanamıyoruz."
print(metin.translate(ceviriTablosu))

qKlavye = "qwertyuıopğüasdfghjklşizxcvbnmöç."# q klavye de yazılan anlamsız cümleyi
fKlavye = "fgğıodrnhpqwuieaütkmlyşxjövcçzsb.,"# f kalvyeye çeviriyoruz anlamlı halde.

name = "Cem Yılmaz" # Cem Yılmaz isminin C ve Y harflerini önce c ve y yaptık sonra
kaynak = "CY"      # e,ı,a sesli harflerini ve boşluk karakterlerinin çıkardık.
hedef = "cy"       # en sonda yazdırdık.
silinecek = "eıa "

ceviriTablosu = str.maketrans(kaynak,hedef,silinecek)
print(name.translate(ceviriTablosu))
#%%                     chr fonksiyonu
print(chr(79))
#%%                         isalpha
name = "serhat"
print(name.isalpha())
isim = "s3rh4t"
print(isim.isalpha())
#%%                       isdigit
name = "123456"
print(name.isdigit())
isim = "123456s"
print(isim.isdigit())
#%%                        isalnum
name = "serhat123"
print(name.isalnum())
isim = "serhat<"
print(isim.isalnum())
#%%                       isdecimal
a = "123"
print(a.isdecimal())
b = "123.3"
print(b.isdecimal())
#%%                 isprintable
a = "a"
print(a.isprintable())
b = "a\nb"
print(b.isprintable())















































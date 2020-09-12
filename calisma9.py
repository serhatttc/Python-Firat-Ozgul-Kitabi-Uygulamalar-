# -*- coding: utf-8 -*-
#                  LİSTELER VE DEMETLER
liste = ["serhat","serdar","serap",22,11]
print(type(liste))
print(liste)
#%%
liste = ["serhat","serdar",["ahmet","nimet"],"murat",22,11]
for oge in liste:
    print("{} adlı ögenin veri tipi : {}".format(oge,type(oge)))
# yani liste içinde liste oluşturabiliyoruz.
#%%
languages = ["Türkçe","İngilizce","İspanyolca","Rusça"]
print(len(languages))
#%%
numbers = [[0,10],[6,60],[12,54],[67,99]]
for i in numbers:
    print(*range(*i))
    print(i)
#%%                 list()  fonksiyonu
# karakter dizilerini liste haline getirir.
alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
print(list(alfabe))
#%%
for i in range(10):
    print(i)
print(*range(10))
print(list(range(10)))
#%%                  LİSTELERİN ÖGELERİNE ERİŞMEK
meyveler = ["elma","armut","muz","kivi"]
for meyve in meyveler:
    print(meyve)
print(meyveler[0])

for ogeSirasi in range(len(meyveler)):
    print("{}. {}".format(ogeSirasi,meyveler[ogeSirasi]))

for sira,oge in enumerate(meyveler,1):
    print("{}. {}".format(sira,oge))

print(meyveler[::-1]) # listeyi ters cevirmek için kullandık.
#%%
liste = ["serhat","serdar",["ahmet","nimet"],"murat",22,11]
print(liste[2][0])
print(liste[0][2])
print(len(liste))
print(liste[len(liste)-3])# sondan 3. ögeyi bulduk.
#%%                    LİSTELERİN ÖGELERİNİ DEĞİŞTİRMEK
colors = ["siyah","kırmızı","sarı","beyaz"]
print(colors)
colors[0] = "pembe"
print(colors)
print(len(colors))
#%%               Listeye Öge Eklemek
liste = [1,2,3,4]
print(liste)
print(liste+[8])
#%%              Listeleri Birleştirmek
derlenenDiller = ["C","C++","C#","Java"]
yorumlananDiller = ["Python","Perl","Ruby"]
diller = derlenenDiller + yorumlananDiller
print(diller)
print(*range(10))
#%% 
sayilar = 0
for i in range(10): # 10 tane sayının ortalamasını aldık.
    sayilar += int(input("not : "))
print(sayilar/10)
#%%
alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
print(list(alfabe))
# bu yaptığımızın eş değeri aşağıdakidir.
liste = []
alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
for harf in alfabe:
    liste += harf
print(liste)
#%%                    Listeden Öge Çıkarmak
liste = [1,2,3,4,5]
del liste [2] # 2. sıradaki ögeyi sildik.
print(liste)
#%%           Listeleri Silmek
liste = [7,8,6,5]
del liste
print(liste) # 'liste' is not defined.
#%%           Listeleri Kopyalamak
liste1 = ["elma","armut","kivi"]
liste2 = liste1[:] # kopyaladık
liste1[0] = "muz" # liste1'i değiştirdik ama liste2 değişmedi.
print(liste1)
print(liste2) 
#%%
liste1 = ["serhat","serdar","serap"]
liste2 = list(liste1) # kopyaladık.
print(liste2)
liste2[0] = "ezgi" # liste2'yi değiştirdik ama liste1 değişmedi.
print(liste1)
print(liste2)
#%%                  Liste Üreteçleri(List Comprehensions)
# Bunların görevleri liste üretmektir.
liste = [i for i in range(1000)]# 0'dan 1000'e kadar olan sayıları tek satırda
                                 # liste haline getirdik.
print(liste)
# yukardaki kodu böylede yazabiliriz.
liste1 = []
for i in range(1000):
    liste1 += [i]
print(liste1)
# bunun aynısı şu şekil
liste2 = list(range(1000))
print(liste2)
#%% 0 ile 1000 arasındaki çift sayıları listelemek.
liste = [i for i in range(1000) if i %2==0]
print(liste)
# bunun aynısını şöyle de yapabiliriz.
liste1 = []
for i in range(1000):
    if i%2==0:
        liste1 += [i]
print(liste1)
#%%       bu listenin bütün ögelerini tek bir listeye atıcaz.
liste = [[1,2],[4,5],[8,9],[3,7]]
tumu = []
for i in liste:
    for z in i:
        tumu += [z]
print(tumu)
# bunun aynısını şu şekilde de yapabiliriz.
liste1 = [[1,2],[4,5],[8,9],[3,7]]
tumu1 = [z1 for i1 in liste1 for z1 in i1]
print(tumu1)
#%%   liste2 içindeki sayıların liste1 içindeki üçlü listelerden
#   hangisiyle birebir eşleştiğini bulmak.
liste1 = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],
           [16,17,18],[19,20,21],[22,23,24]]
liste2 = [1,88,97,55,88,25,34,64,21,22,6,9,100,24,7,14,45,99,20,66,233,
          77,121,90,58,11,69,23]
for i in liste1:#liste1 adlı listedeki herbir ögeye i adını verelim.
    ortak = [z for z in i if z in liste2]# i içindeki, liste2'de de yer alan
    # herbir ögeye de z adını verelim ve bunları ortak adlı listede toplayalım.
    if len(ortak) == len(i):# eğer ortak adlı listenin uzunluğu i değişkeninin 
        # uzunluğuyla  aynıysa
        print(i)# i'yi ekrana basalım ve ortak kümeyi bulalım.
# 360-367 ARASI X O X OYUNU KODU --------------------------

#%%                        DEMETLER
demet = ("serhat","serdar",1,2)
print(type(demet))# TUPLE
dmt = "serhat","serdar",1,2
print(type(dmt))# TUPLE
a = "abcdefg"
print(tuple(a))
#%%
# tek karakterli demet yazmak için
demet = ("serhat",)# ',' koyulmalı.
print(type(demet))# TUPLE
dmt = "serhat",
print(type(dmt))# TUPLE
#%%   demetlerin ögelerine erişmek için listeler ve karakter dizleri gibi yaparız.
demet = ("elma","armut","kiraz")
print(demet[0])
print(demet[-1])
print(demet[0:2])
#%% demetlerde karakter dizileri gibi değiştirilemez veri tipleridir.listeden farklıdır.
demet = ("ahmet","nimet","serdar")
demet = demet + ("serhat",) # bu veriyi ekledik.
print(demet)
#%%                          LİSTELERİN METOTLARI
print(dir(list))# bütün metotlar burda.
print(dir([]))# aynı çıktıyı verir.

print([i for i in dir(list) if not "_" in i])# bizim işimize yarayanlar bunlar.
#%%                  append
liste = ["serhat",2,"serdar",1]
liste.append("serap")
print(liste)
# bir listeye tek tek öge yerleştirceksek append daha uygun.
#%%                 extend
# ama bir listeye başka bir liste ekleyeceksek extend daha uygun.
li1 = [1,2,3]
li2 = [7,8,9]
li1.extend(li2) # append'de böyle ekleyemeyiz.
print(li1)
print(li2)
#%%               insert
liste = ["serhat","serdar","serap"]
liste.insert(2,"aysu")# listenin 2. sırasına bunu ekle dedim.
print(liste) 
#%%               remove
liste = ["serhat",1,2,80]
liste.remove(80)# tek parametre ile kullanılır.
print(liste)
#%%                reverse
liste = ["elma","armut","kiraz"]
print(liste[::-1]) # dilimleme işlemiyel terstten okuttuk.
li1 = ["serhat","serdar","serap"]
li1.reverse()# bunun sayesinde terstten okuttuk.
print(li1)
#%%                 pop
liste = ["elma","armut","çilek"]
liste.pop()#parametre vermezsek son ögeyi siler.
print(liste)
liste.pop(0)# 0. sıradaki ögeyi sildirdik.
print(liste)
#%%                 sort
liste = [10,1,-1,5,9,3]
liste.sort() # küçükten büyüğe doğru sıraladı. 
print(liste)
liste.sort(reverse=True)# burda da tam tersine göre sıraladık.
print(liste)
#%%                 index
liste = ["serhat","serdar","serap","ahmet","nimet",1]
print(liste.index("serdar")) # kaçıncı sırada olduğunu söyler.
print(liste.index(1))
#%%                count
liste = [1,2,8,5,"serhat",1,1,"serhat"]
print(liste.count("serhat")) # serhat ögesinin kaz kez geçtiğini söylüyor.
print(liste.count(1)) # 1 ögesinin kaç kez geçtiğini söylüyor.
#%%                  copy
liste1 = ["serhat","serdar","serap"]
liste2 = liste1.copy()# liste1'i liste2'ye kopyaladık.
print(liste2)
#%%                 clear
liste = ["serhat","serdar","serap"]
liste.clear()
print(liste)
#%%                         DEMETLERİN METOTLARI
print(dir(tuple))# tüm metotlar burda yer alır.
# bizi ilgilendiren sadece iki metot vardır.
#%%               index
demet = ("elma","armut","çilek",1)
print(demet.index(1)) # bize hangi sırada olduğunu söyledi.
print(demet.index("armut"))
#%%               count
demet = (1,2,8,5,"serhat",1,1,"serhat")
print(demet.count("serhat"))
print(demet.count(1))
#%%                   SAYMA SİSTEMLERİ
#   Onlu Sayma Sistemleri
print((0*(10**0))+(8*(10**1))+(9*(10**2))+(1*(10**3)))# 1980
# Sekizli Sayı Sistemi
# Onaltılı Sayı Sistemi
#%%                         İKİLİ SAYI SİSTEMİ(BİNARY)
# sayıları gösteren iki farklı simge vardır.'0' ve '1'
#%%
#                    SAYMA SİSTEMLERİNİ BİRBİRİNE DÖNÜŞTÜRME

#                          Fonksiyon Kullanarak
#            bin
print(bin(5))# bin() sayının ikili sistemdeki karşılığını verir.'0b'
print(bin(5)[2:])
#%%          hex
print(hex(10))# sayının onaltılı sistemdeki karşılığını verir.'0x'
#%%        oct
print(oct(11))# sayının sekizli sistemdeki karşılığını gösterir.'0o'
#%%       int()
print(int("a",16))# herhangi bir sayıyı onluk sistemdeki karşılığına dönüştürebiliriz.
# ilk parametre karakter dizisi olmalı,ikinci parametre hangi sayı sisteminde old.

#%%                     Biçimlendirme Yoluyla
#              b
print("{:b}".format(5)) # bin() ile aynı işi yapar.İkili sistemdeki karşılığı.
#%%            x
print("{:x}".format(10)) # onaltılı sistemdeki karşılığı.hex() ile aynıdır.
#%%            o
print("{:o}".format(11))# oct() ile aynıdır.Sekizli sistemdeki karşılığını verir. 
#%%
















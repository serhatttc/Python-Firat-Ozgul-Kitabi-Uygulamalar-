# -*- coding: utf-8 -*-

import sys
print(sys.version)
print(sys.version_info) # Kullanılan python hakkında bilgi verir.||3.7.4 sürüm
print(sys.version_info.major)# 3
print(sys.version_info.minor)# 7
print(sys.version_info.micro)# 4
#%%              SÜRÜME GÖRE İŞLEM YAPAN PROGRAM

import sys # ilk olarak modülü içe aktarıyoruz.İçindeki araçları kullanmak
           #  için bunu yapmak şart.
_2x_text = """
Python'un 2.x sürümlerinden birini kullanıyorsunuz.
Programı çalıştırmak için 3.x sürümlerinden birini kullanın."""
# Python 2'de bu text yazmaz.Bir hata verir. bunu yazmasını istiyorsak.
# -*- coding: utf-8 -*- yapmalıyız ki Türkçe'yi desteklesin.Sonra 
# text'e u""" diye başlayalım ki Türkçe harfleri düzgün okusun.
_3x_text = "Programa Hoşgeldiniz."

if sys.version_info.major < 3:
    print(_2x_text)
else:
    print(_3x_text)
#%%
tuttugumSayi = 23

bilBakalim = int(input("Sayıyı tahmin et : "))

if bilBakalim == tuttugumSayi:
    print("Tebriik.")
else:
    print("Yanlışş.")
#   Program sadece 1 kere çalışıyor.sonra tekrar çalıştırmak gerekiyor.
#   bunun için loops yani (döngüler) kullanabiliriz.
#%%                      LOOPS (DÖNGÜLER)

a = 1
while a == 1:# a değişkeninin değeri 1 olduğu surece demek.
    print("Patron çıldırdı.")  # a = 1 old. sürece bunu yazdır demek.
    # bu döngü sonsuz çalışır.Çünkü 'a' hep 1.
#%%
a = 1
while a < 10:    # a'nın değeri 10'dan küçük old. sürece demek.
    print("PC çıldırdı.")
#   Bu da sonsuz döngüye girdi.Çünkü 'a' hep 1.
#%%
a = 1
while a < 10:
    a += 1   # a'yı 1 arttırdık her döngüde 10'a gelene kadar.
    print("PC çıldırdı.")
    print(a)
#%%
giris = "topla carp çıkar böl"
print(giris)
anahtar = 1
while anahtar == 1:
    soru = input("İşlem numarasını gir(Çıkmak için q) : ")
    
    if soru == "q":
        print("Çıkılıyor.")  # SAYFA 184
        anahtar = 0
    elif
    elif
#%%  bu şekildede yapabiliriz.
giris = "topla carp çıkar böl"
print(giris)

while True:  # aksi olmadığı halde çalışmaya devam et demek.
    soru = input("İşlem numarasını gir(Çıkmak için q) : ")
    
    if soru == "q":
        print("Çıkılıyor.")
        break
    elif
    elif
#%%
tekrar = 1

while tekrar <= 3:
    tekrar += 1
    print("NASILSIN")
    print(tekrar)
#%%
tekrar = 1 

while tekrar <= 3:
    print("tekrar",tekrar)
    tekrar+=1
    input("NASILSIN")
    print("bool değeri : ",bool(tekrar<=3))
#%% 1'den 100'e kadar olan çift sayılar.
a = 0
while a<100:
    a +=1
    if a % 2 == 0:
        print(a)
#%%
trHarfler = "işğçüö"
for harf in trHarfler:
    print(harf)
sayilar = "123456"
for i in sayilar:
    if int(i) > 3:
        print(i)
#%%
trHarfler = "işöüğç"

parola = input("Parola giriniz : ")

for karakter in parola:
    if karakter in trHarfler:
        print("Türkçe harf kullanılamaz.")
    else:
        print("sıkıntı yok")
#%%
while True:
    parola=input("Parola gir.")
    if not parola:
        print("BOŞ OLMAZ.")
    elif len(parola)>8 or len(parola)<3:
        print("8 den uzun 3 ten kısa olmaz.")
    else:
        print("Yeni parolanız : ",parola)
        break
#%%
izinliKarakterler = "0123456789+-/*="

while True:
    veri=input("işlem : ")
    if veri == "q":
        print("çıkılıyor.")
        break
    for s in veri:
        if s not in izinliKarakterler:
            print("napıyon")
            quit()
    hesap = eval(veri)  # eval fonk. kontrollü bir halde yazdık.
    print(hesap)
#%%
for i in range(0,10): # belli aralıktaki sayıları göstermek için kullanılır.
    print(i)
for a in range(10): # ikiside aynı
    print(a)
#%%
for i in range(3):
    print(i)
    parola = input("PAROLA : ")
    if i ==2:
        print("3 kere yanlış girdin.")
    elif not parola:
        print("boş bırakma")
    elif len(parola) in range(3,9):
        print("parolanız : ",parola)
        break
    else:
        print("8 den uzun 3 ten kısa olmaz.")
#%%
for i in range(1,101,2): # 3. parametre kaçar kaçar gitceğini söylüyor.
    print(i)
#%%
while True:
    parola = input("PAROLA : ")
    if not parola:
        pass  # Python'a hiç bişey yapmadan devam et diyoruz.
    elif len(parola) in range(3,9):
        print("parolanız : ",parola)
        break
    else:
        print("8 den uzun 3 ten kısa olmaz.")   
#%%
while True:
    s = input("Sayı girin : ")
    if s =="iptal":
        break
    if len(s)<=3: # bu duruma uyarsa continue kendinden sonrakini es geçip başa sarar.
        continue
    print("Max. 3 haneli bir sayı girebilirsiniz.")
#%%  first'te olup second'ta olmayanları bulduk.
firstText = "asdfghjklzxcvbnmöç"
secondText = "asdfghjkl"
for s in firstText: # ilk metin için bütün ögelerin üzerinden geçiyoruz.
    if not s in secondText: # bu ögeleri belli bir ölçüte göre süzüyoruz.
        print(s) # sonra yazdırıyoz.
#%%
firstText = "asdfghjklzxcvbnmöçasdfgh"
secondText = "asdfghjklasdfghzxewrtwert"        
fark=""
    
for s in secondText:# ikinci metinde 's' dediğimiz bütün ögeler için.
    if s not in firstText: # eğer 's' ilk metinde yoksa.
        if not s in fark: # eğer 's' farkta da yoksa
            fark += s   # bu ögeyi fark değişkenine ekle.
print(fark)        # yazdır.
#%%       DOSYALARIN İÇERİĞİNİ KARŞILAŞTIRMA
f1=open("names1.txt") # dosyayı açıyoruz.
f1Satirlar = f1.readlines() # satırları okuyoruz.

f2=open("names2.txt")# türkçe karakterler görünmüyorsa ,encoding="utf-8" ekliyoruz.
f2Satirlar = f2.readlines() #     o da olmazsa utf-8 yerine ,encoding="cp1254" ekliyoruz.

for i in f2Satirlar: # 2. dosya da olup 1 de olmayanlar.
    if i not in f1Satirlar: # aynı olanları ayırmak istesek not koymıcaz.
        print(i)
f1.close()
f2.close()
#%%    KARAKTERDİZİSİNDEKİ KARAKTERLERİ SAYMA
text = """
2019 yılının Aralık ayında, Çin’de birdenbire sebebi açıklanamayan 
zatürre olguları ortaya çıkmaya başladı. Yapılan araştırmalar, bu 
zatürre vakalarının daha önceden tanımlanmamış yeni bir tip coronavirüs 
(coronavirus) olduğunu ortaya çıkardı. Virüsün bu formuna, 2019 yılında
ortaya çıktığı için, Coronavirus 2019 yani COVID-19 denildi. 
Coronavirüs aslında, hayvanlarda bolca rastlanan bir virüstür. 
Son zamanlarda hastalığa neden olan virüsün kaynağının, ise Çin'in
Wuhan kentinde bulunan Huanan deniz ürünleri pazarı olduğu düşünülmektedir.
Önce hayvandan insana bulaşan virüsün insandan insana da yayılabildiği zamanla
anlaşılmıştır. """
harf=input("Sorgulamak istediğiniz harf : ")
sayi = ""
for s in text: # text içinde "s" adı verdiğimiz herbir öge için.
    if harf ==s: # eğer kullanıcıdan gelen harf "s" ile aynıysa.
        sayi+=harf # kullanıcıdan gelen bu harfi sayı değişkenine yolla.
print(len(sayi)) # hangi harften kaç tane olduğunu yazıyor.
# böyle de yazılabilir.
#harf=input("Sorgulamak istediğiniz harf : ")
#sayi = 0
#for s in text:
#    if harf ==s:
#        sayi+=1
#print(sayi)
#%%            DOSYADAKİ KARAKTERLERİ SAYMA
# yukardakinin aynısı sadece fark olarak text yerine dosyayı açıyoruz.
# en sonunda dosya.close() diyip kapatıyoruz.













    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
  
    
    
    
    
    
    
    
    
    
    
    








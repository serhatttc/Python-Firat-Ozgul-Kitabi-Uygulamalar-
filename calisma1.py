
import keyword
print(keyword.kwlist)

#%%

# aylık yol masrafı programı

gunSayisi = 22
gidisUcreti = 1.5
donusUcreti = 1.4

masraf = (gidisUcreti+donusUcreti)*gunSayisi

print(masraf)

print(gunSayisi*12)


#%%

# Çemberin alanı programı

cap = 16
yariCap = cap/2
pi = 3.14
alan = pi*yariCap**2
cevre = 2*pi*yariCap

print("Alan : "+str(alan))

print(pow(12,2,2))


#%%

# Aynı değere sahip değişkenler

ocak=mart=mayıs=temmuz=agustos=ekim=aralik=31
nisan=haziran=eylul=kasim=30
subat=28

print(mayıs)

#%%

# Mart ayındaki dogalgaz kullanımı

mart = 31

aylikKullanim = 345
faturaTutari = 287
birimFiyat = faturaTutari/aylikKullanim
gunlukKullanim = aylikKullanim/mart

print(str(birimFiyat)+" TL")
print(str(gunlukKullanim)+" m^3")

#%%

# Değişken değeri takas yapma

osman = "Proje müdürü"
mehmet = "Şef"

osman,mehmet = mehmet,osman
print(osman)

#%%

# Başka programlarda değişken takası

osman = "Proje müdürü"
mehmet = "Şef"
gecici = "Proje müdürü"
osman = mehmet
mehmet = gecici
print(mehmet)
print(osman)

#%%

print("""game over!
bitti!
son!
finish""")

#%%

print("serhat","çağlar","bilecik",1994,sep="\n")

print("serhat\nçağlar")

print("benim adım serhat","senin adın serdar",sep=",\n",end=".")

#%%

# Bir .txt dosyasına yazma işlemi

dosya = open("deneme1.txt","w") # write=yazmak
print("Herkes öldürür sevdigini.","Ama herkes öldürdü diye ölmez.",
      sep="\n",file=dosya)# normalde file=sys.stdout
dosya.close() # dosyayı kapatmış oluyoruz.

import os # şu anda bulunduğun yeri söyler.
os.getcwd()

#%%

dosya = open("deneme2.txt","w")
print("yalansın\n""dolansın",file=dosya,flush=True)

# flush=True ise dosya kapanmasa da yazar beklmez.

#%%

print(*"SERHAT",sep=".")
print(*"SERHAT")

#%%

import sys
f = open("deneme3.txt","w")
print("bir ihtimal",flush=True)

#%%

# Kaçış dizileri // escape sequence
# '\' , '\n' , '\t' , '\a' , '\r' , '\v' , '\b' , '\u' , '\U' ,'\N' , '\x' , 'r' , '\f'

print('Yarın Bilecik\'e gidicem.')
print('deniz üstü köpürür hey canım \
rinanay rina rina\
nay')

print("bir tek dileğim var\nmutlu ol yeter.")
baslik = "Pythton Programlama Dili"
print(baslik,"\n","-"*len(baslik),sep="")
print("C:\\nisan\\masraflar.txt")# Hatayı düzeltmek için \\ iki tane.

print("abc\tdef") # '\t' demek TAB tuşuna basmış gibi boşluk bırakır.
print(*"123456",sep="\t")

#print("\a")# sistemde !BİP! sesi cıkarır.

print("Merhaba\rZalim Dünya")
print("Merhaba\rDünya")#'\r' dizisi kendinden sonra yazılanları aynı satırın 
#                           başına dönüp üzerine yazmaya başlar.

print("düsey\vsekme")

print("yahoo.com\b.uk")
print("serhat",".","com")# '\b' dizisi imleci bir karakter sola kaydırır.
print("serhat","\b.","\bcom")
print("istihza\b\b\bsn")

print("\u0130")# UNICODE, her karakterin numaralandığı bir sistemdir.
print("\u0131")# Kod konumu belirtmesi yaptık.
print("\u0061")
print("C:\\users\\python\\ezel.txt") # Ya da / isaret kullanılır.

print("\U00000131") # '\u' dan farkı o 4 karakterli bu 8 karakterli.

import unicodedata
unicodedata.name("s") # UNICODE sistemindeki uzun adı verir.
print("\N{LATIN SMALL LETTER S}")
 
print("\x41")# Sayma sayılarının karakter karşılığnı verir.

#print("Kurulum dizini : C:\aylar\nisan\toplam masraf") # burda yanlış yazım olur.
print("Kurulum dizini : C:\\aylar\\nisan\\toplam masraf")# \\ , çözüm yoludur.
print(r"Kurulum dizini : C:\aylar\nisan\toplam masraf")# r koyarak hallettik.

print("Kaçış dizisi:\\")
print("Kaçış dizisi:""\\")
print("Kaçış dizisi:","\\")

f = open("deneme1.txt","w") # '\f' sayfa bitti deyip diger sayfanın başına 
print("deneme\fdeneme",file=f)  # geçmesini söyler.
f.close()    # Microsoft Word veya başka yerde aç görürsün.

print("\fırat")






















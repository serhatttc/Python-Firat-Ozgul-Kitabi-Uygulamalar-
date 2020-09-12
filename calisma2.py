# -*- coding: utf-8 -*-

tarih = "16.03.2020"
gun = "Pazartesi"
vakit = "öğleden sonra"
print(tarih,gun,vakit,"buluşalım",end=".\n")

#%%

gun = 22
gidisUcreti = 1.5
donusUcreti = 1.4

masraf = gun*(gidisUcreti+donusUcreti)

print("-"*30)
print("Çalışılan Gün Sayısı\t:",gun)
print("Gidiş Ücreti\t\t:",gidisUcreti)
print("Dönüş Ücreti\t\t:",donusUcreti)
print("-"*30)
print("Aylık Yol Masrafı\t:",masraf)

#%%

isim = "Serhat"
soyisim = "Çağlar"
sistem = "Ubuntu"
sehir = "Bilecik"

print("İsim            :",isim, "\n",
      "Soyisim         :",soyisim, "\n",
      "İşletim Sistemi :",sistem, "\n",
      "Şehir           :",sehir, "\n",
      sep="")

#%%
isim = input("İsminiz Nedir?"), # Kulanıcaıdan veri almak için kullandık.
print("Merhaba",isim, end="!\n")
#%%
yas = input("Yaşınız kaç?")
print("Demek",yas,"yaşındasınız.")
#%%
cap = input("Dairenin çapını giriniz:")
yarıCap = int(cap)/2 # Karakter dizisini tamsayıya dönüştürmek için.
pi = 3.14
alan = pi*yarıCap**2
print("Çapı",cap,"cm olan dairenin alanı",alan,"cm2 dir.")
#%%
sayi = input("Lütfen bir sayı giriniz : ")
veri = int(sayi)
print("Girdiğiniz sayının karesi : ",veri**2)
#%%
sayi = 123456
karDiz = str(sayi)
print(len(karDiz))
# İki şekilde de yapılır.
sayi = 123456
print(len(str(sayi)))
#%%
sayi = 2  # Integer (int) tamsayı
print(type(sayi))
print(float(sayi)) # Noktalı sayıya dönüştürdük.
sayi1 = "2"  # String (str) sayı değerli karakter dizisi
print(type(sayi1))
print(float(sayi1)) # Noktalı sayıya dönüştürdük.
print(complex(sayi1)) # Karmaşık sayıya dönüştürdük.
#%%
veri = input("işleminiz:")
hesap = eval(veri) # Kullanıcıdan aldığı her veriyi komut olarak algılar işleme sokar
print(hesap)
#%%
exec("a=45") # Karakter dizisi içindeki değişken tanımlama işlemi yapar. 
print(a)      # ama 'eval()' bunu yapamaz.

d1 = "mmmmmmmm"
girdi = input(d1)
exec(girdi)
d2 = "aaaaaaaa"
print(d2)
#%%
url = input("Sitenin adresini giriniz.")
print("Hata! Google Chrome",url,"sitesini bulamadı.")
# '' içinde yazmak istesek.
url = input("Sitenin adresini giriniz.")
print("Hata! Google Chrome","'"+url+"'","sitesini bulamadı.")
url = input("Sitenin adresini giriniz.")
print("Hata! Google Chrome '{}' sitesini bulamadı.".format(url))
#%%
print("{} ile {} iyi bir ikilidir.".format("Python","Django"))
text = "{} ile {} iyi bir ikilidir."
print(text.format("Python","Django")) # Kaç tane '{}'varsa o kadar veri olmalı.
#%%
                           

















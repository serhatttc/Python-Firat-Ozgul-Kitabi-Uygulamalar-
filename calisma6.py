# -*- coding: utf-8 -*-
#                           ----   HATALAR ----
print "serhat" # SyntaxError hatası, programcı tarafından farkedilir.
              # hata verir.Hemen anlaşılır.
#%%
sayi1 = input("1. sayıyı gir : ")  # bu ise "BUG" yani programcı kusurları
sayi2 = input("2. sayıyı gir : ")  # hata vermez anlaması zordur.

print(sayi1,"+",sayi2,"=",sayi1+sayi2)
#%%
sayi1 = input("1. sayı : ")# "55/asdf" ValueError.
sayi2 = input("2. sayı : ")# "55/0" ZeroDivisionError.
sayi1=int(sayi1)           # bu ikisi istisnadır.Yani"EXCEPTİON"
sayi2=int(sayi2)
print(sayi1,"/",sayi2,"=",sayi1/sayi2)
#%%                  ------ HATA YAKALAMA ----
#   'try' ve 'except' bloklarından yararlanılır.
sayi1 = input("1. sayi : ")
sayi2 = input("2. sayi : ")
try:            # hata vereceğini bildiğimiz kodları try bloğu içine aldık.
    sayi1=int(sayi1)
    sayi2=int(sayi2)
    print(sayi1,"+",sayi2,"=",sayi1+sayi2)
except ValueError: # ValueError adlı hatayı yakalamak için bunları yazdık.
    print("Lütfen sadece sayı girin.")
# burda demek istenen
# try:
#    hata verebileceğini bildiğimiz kodlar
# except HataAdı:
#    hata durumunda yapılacak işlem
#%%
sayi1 = input("1. sayi : ")
sayi2 = input("2. sayi : ")
try:           
    sayi1=int(sayi1)
    sayi2=int(sayi2)
    print(sayi1,"/",sayi2,"=",sayi1/sayi2)
except ValueError: 
    print("Lütfen sadece sayı girin.")
except ZeroDivisionError:
    print("Sayıyı 0 ile bölemezsin")
#%%,
sayi1 = input("1. sayi : ")
sayi2 = input("2. sayi : ")
try:           
    sayi1=int(sayi1)
    sayi2=int(sayi2)
    print(sayi1,"/",sayi2,"=",sayi1/sayi2)
except (ValueError,ZeroDivisionError): # türleri gruplayıp tek
    print("Hata oluştu.")        #  bir mesaj da gönderebiliriz.
#%%
while True:
    print("Çıkmak için 'q' tuşuna basın.")
    sayi1=input("1.sayı : ")
    if sayi1 == "q" and sayi2 == "q":
        print("çıkılıyor.")
        break    
    sayi2=input("2.sayı : ")    
    try:
        sayi1=int(sayi1)
        sayi2=int(sayi2)
        print(sayi1,"/",sayi2,"=",sayi1/sayi2)
    except (ValueError,ZeroDivisionError):
        print("Hata oluştu.")
#%%                     'as'
sayi1 = input("1. sayi : ")
sayi2 = input("2. sayi : ")
try:           
    sayi1=int(sayi1)
    sayi2=int(sayi2)
    print(sayi1,"/",sayi2,"=",sayi1/sayi2)
except ValueError as hata:# burda hatanın türünü yazdık açıklamasını istedik.
    print(hata)       # hatanın açıklamasını yazdırdık.
#%%                    'else'       
try:
    bolunen = int(input("1. sayı : "))
    bolen = int(input("2. sayı : "))
except ValueError:
    print("sadece sayı girin.")
else:     # else hataları gruplara ayırmamıza yaradı pek kullanılmaz.
    try:
        print(bolunen/bolen)
    except ZeroDivisionError:
        print("sayı 0'a bölünmez.")
#%%                       'finally'
# try:
#        bir takım işler
# except birHata:
#       hata alınca yapılacak işlemler
# finally:
#        hata olsa da olmasa da yapılması gerekenler|| dosya.close() || mesela.
#%% 'raise' program hata vermicek olsa bile biz hata göndermesini isteriz ve bunu kullanırız.
bolunen = int(input("Bölünen sayı : "))
if bolunen == 23:
    raise Exception("23 yazma amk.") # kendimiz istediğimiz gibi hata oluşturduk.
bolen = int(input("Bölen sayı : "))
print(bolunen/bolen)
#%%
trKarakter = "İşüğöç"
password = input("parola : ")

for i in password:
    if i in trKarakter:
        raise TypeError("Türkçe karakter kullanılamaz.")
    else:
        pass # hiç bişey yapmadan geç.
print("parola kabul edildi.")
#%%
try:
    bolunen = int(input("1. sayı : "))
    bolen = int(input("2. sayı : "))
    print(bolunen/bolen)
except ZeroDivisionError:
    print("sayı 0'a bölünmez.")
    raise # hataya ilave bilgi eklemek için kullandık.
#%%             BÜTÜN HATALARI YAKALAMAK
#try:
#    bir takım işler
#except:   bu şekide bütün hataları yakalar.
#    hata mesajı
#---------------------------------------
#try:
#    bir takım işler
#except ValueError:
#    bişeyler yaz
#except ZeroDivisionError:
#    bişeyler yaz
#except:
#    beklenmedik hata oluştu.
import sys

text2x = "2.x sürümü kullanıyosun 3.x yukle."
text3x = "hosgeldin."
try:
    if sys.version_info.major<3:
        print(text2x)
    else:
        print(text3x)
except AttributeError: # bu hata python 2.7'den düşükse çıkar.
    print(text2x)






      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        






















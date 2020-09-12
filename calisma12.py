# -*- coding: utf-8 -*-
#                          BASİT BİR İLETİŞİM MODELİ

#           8 Bitlik Bir Sistem

# ikili sayma sisteminde 0 ve 1'lerin oluşturduğu her bir basamaağ 'bit'  denir.
#  Bİnary(ikili) , digiT(rakam) kelimelerin birleşmesi ile oluşut. 'BİT'

for i in range(10):
    print(bin(i)[2:].zfill(8))
# 8 bitlik iletişim sisteminde 10'a kadar bu şekilde sayarız.
# toplam 2**8 = 256 farklı sinyal göderebiliriz.
#%%  .zfill = karakter dizilerinin sol tarafına istediğimiz kadar 0 eklettirir.
for i in range(256):
    print(bin(i)[2:].zfill(8))
# 8 bitlik bu sistemle göderebildiğimiz son sinyal yani sayı 255'tir.
# bu sistemle bundan büyük sayı göderemeyiz.
# 255. sayı = 11111111 bundan sonraki yani 256. sayı 9 bitliktir.
# 256. sayı = 100000000
print((255).bit_length())# 8 bitlik olduğunu söyledi.
print(bin(255)[2:])# 11111111 çıktısını verdi.
print((256).bit_length())# 9 bitlik olduğunu söyledi.
print(bin(256)[2:])# 100000000 çıktısını verdi.

#%%      HATA KONTROLÜ----------------SAYFA---434
# yukarıdaki sisteme hata kontrol mekanizması ekleyebilmek için sistemi 8 bitten 
# 7 bite çekeceğiz,yani iletişimimizi toplam 2**7=128 sayı ile sınırlayacağiz
# tabi 128 8. bite giriyor.bu sayıyı hata kontrol mekanizmasına tahsis edeceğiz. 
# mevcut karakterler 7 bitlik alana sığdırıldıı.Boşta kalan 8. bit veri
# aktarımının düzgün olup olmadığını denetlemek için kullanılır.
#%%      KARAKTERLERİN TEMSİLİ------------SAYFA----436-437--

#%%                     KARAKTER KODLAMA(CHARACTER ENCODİNG)
#  1 bayt = 8 bit
#             7 Bitlik Bir Sistem

#       ASCII  TABLE  -------   SAYFA--443
# ASCII 7 bitlik bir karakter sistemidir.8. bit hata kontrolü için kullanılırdı.
for i in range(128):
    if i%4==0:
        print("\n")
    print("{:<3}{:>8}\t".format(i,repr(chr(i))),sep="",end="")
# gözükmeyen ilk 32 karakter ---SAYFA---444----
#%%
"Ç".encode("cp857")# verdiği b'\x80 çıktısı onaltılı sayma düzenine göre.
print(int("80",16))# yukardakinin onlu düzendeki karşılığı.

# Genişletilmiş ASCII 8 bitlik bir sistemdir. 0-255 arası sayıları temsil eder.
# ASCII'de ve Genişletilmiş ASCII'de 1 baytlık alana toplam 256 karakter
# sığdırılabilir.
# UNICODE 1.000.000 dan fazla karakter içerir.
# UNICODE ilk ortaya çıktığında 16 bitlik bir sistemdi yani 2**16=65536,
# karakterin kodlanmasına izin veriyordu.
# Bugün ise UNICODE'nin belli bitlik bir sınırı yoktur.Bu tabloya istedğiniz 
# kadar karakter ekleyebilirsiniz.
#UNICODE , ASCII'nin aksine karakterleri doğrudan doğruya kodlamaz.UNICODE'nin
# yaptığı sey karakterleri tanımlamaktan ibarettir.
#UNICODE sisteminde her karakter tek bir kod konumuna (code point) karşılık gelir.
#Kod konumları şu formüle göre gösterilir.
# "u+sayının onaltılı değeri"

#%%      1 Karakter != 1 Bayt
for i in range(1,5):
    print("{} bayt kullanırsak toplam 2**{:<1}={:,}".format(i,i*8,(2**(i*8))))

#%%
harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
for s in harfler:
    print("{:<5}{:<15}{:<15}".format(s,str(s.encode("utf-8")),len(s.encode("utf-8"))))
#%%
print("ç".encode("utf-8"))# b'\xc3\xa7'
# bu çıktıdan python'un yazdığı karakterleri çıkarsak.kalan 'c3a7'
print(int("c3a7",16))# bunun 10lu sistemdeki karşılığı budur.
print(bin(50087))# ikili sayma sistemindeki karşılığı budur.
print((50087).bit_length())# 16 bitlik bir sayıdır,yani 2 baytlık bir sayı.
#%%
# a harfine bakalım.
print("a".encode("utf-8"))# bu çıktı direkt harfin kendiini gösteriyor.
# hangi sayıya karşılık geldiğini bulmak için aşağıdaki kodu yapıcaz.
print(ord("a"))# 97 çıktısını verdi.

#%%     Eksik Karakterler ve encode Metodu   

# 'strict' = karakter temsil edilemiyorsa hata verilir.
# 'ignore' = temsil edilemeyen karakter görmezden gelinir.
# 'replace' = temsil edilemeyen karakterin yerine '?' konulur.
# 'xmlcharrefreplace' = temsil edilemyen karakter yeine XML karşılığı konur.

#print("bu bir Türkçe kelimedir.".encode("ascii",errors="strict"))# bu hata verecek.
# errors parametresine değer vermesekte 'strict' olarak algılar.ön tanımlıdır.
print("bu bir Türkçe kelimedir.".encode("ascii",errors="ignore"))
print("bu bir Türkçe kelimedir.".encode("ascii",errors="replace"))
print("bu bir Türkçe kelimedir.".encode("ascii",errors="xmlcharrefreplace"))

#%%                    DOSYALAR VE KARAKTER KODLAMA
#            encoding
# dosyanın hangi kod çözücü ile açılacağını belirlememizi sağlar.
import locale
print(locale.getpreferredencoding())# 'cp1254' çıktısı verir.
# 'utf-8' ile kodlanmış dosyalar özellikle Türkçe karakterler düzgün gözükmeyecek.
# O yüzden dosyalarınızın hangi kod çözücü ile open() içinde belirtmeliyiz.

f = open("dosyaAdi",encoding="utf-8")# 'utf-8' belirttik.

#           errors
f = open("dosyaAdi",encoding="utf-8",errors="strict")
f = open("dosyaAdi",encoding="utf-8",errors="ignore")
f = open("dosyaAdi",encoding="utf-8",errors="replace")

#%%                    KONU İLE İLGİLİ FONKSİYONLAR

#                 repr()
# Python programlama dilinde nesneler iki farklı şekilde temsil edilir.
# 1-Python'un göreceği şekilde || 2-Kullanıcının göreceği şekilde(print())

a = "elma "# sonda bir tane boşluk bıraktık.
print("{} kilo {} kaldı.".format(23,a))
print(repr(a))# bu fonksiyon ile sondaki boşluğu görebildik.
b = """serhat
çağlar"""
print(b)
print(repr(b))# \n işlecini bize gösterdi.
print("\n")#  satır başına geçtiğini yazdırdı.
print(repr("\n"))

#%%              ascii()
# karakterlerin UNICODE kod konumlarını gösterir.
# repr()'den farkı repr() ASCII'de yer almayanlarıda göründüğü gibi gösterir.
print(repr("İ"))# 'İ' çıktısı verdi.
print(ascii("İ"))# '\u0130' çıktısı verdi.
# ascii fonksiyonu str tipinde çıktı verir, encode metodu ise bytes tipinde.

#%%             ord()
print(ord("a"))# 97 çıktısı verdi.
print(ord("ü"))# 252 çıktısı verdi.

#%%            chr()
print(chr(252))# ü çıktısı verdi
print(chr(97))# a çıktısı verdi.

#%%              BAYTLAR(BYTES) VE BAYT DİZİLERİ(BYTEARRAYS)

# 1 bit ikili sayma sisteminde herbir basamağa verilen isimdir.
# UTF-8 kod çözücüsü hem çok sayıda karakter kodlar hemde tasarruf sağlar.

bayt = b"" # burada boş bir bayt tanımladık.
print(type(bayt))# bytes çıktısı verdi.

# ikili dosyalara sadece baytları yazabiliriz.

#%%          bytes()  foksiyonu

# bayt veri tipi temel olarak ASCII karakterleri kabul eder.
# Yani ASCII tablosu dışındaki karakterleri doğrudan bayt olarak temsil edemeyiz.
# Ama ASCII dışında kalan karakterleri de bayt'a dönüştürmenin bir yolu var.
# bunun için bytes() fonk. yararlanıcaz.

b = bytes("ş","utf-8")# gördüğünüz gibi ilgili karakterin hangi kod çözücü ile 
# kodlanacağını belirterek,byt tipinde veri oluşturduk.
print(b)

c = bytes("Serhat","ascii",errors="replace")
print(c)

#%%                         Baytların Metotları

print(dir(bytes))# metotlar bunlardır.

for i in dir(bytes):# burda baytların metotları arasında olup karakter dizilerinde
    if i not in dir(str): # olmayan metotları ayırdık.
        print(i)

#%%            decode
print("İ".encode("utf-8"))# b'\xc4\xb0' çıktısı verdi.
print("İ".encode("cp1254"))# b'\xdd' çıktısı verdi.

# decode metotduyla bunun tam tersini yapıcaz.

print(b"\xc4\xb0".decode("utf-8"))# İ çıktısı verdi.
print(b"\xdd".decode("cp1254"))# İ çıktısı verdi.

print(b"\xc4\xb0".decode("cp1254"))# Ä° çıktısı verdi.
# yani cp1254 adlı kod çözücü bu baytı çözüyor ama yanlış çözüyor.

#%%           fromhex

print(bytes.fromhex("c4b0"))# b'\xc4\xb0' çıktısı verdi.'İ' harfi.

#%%            
#                          Bayt Dizileri

pdf = bytearray(b"PDF-1.7")#• biz bayt dizisi tanımladık.

#%%               Bayt Dizilerinin Metotları-----SAYFA---470--471

print(dir(bytearray))# metotlar bunlardır.
# bu veri tipi hem listelerden hem de baytlardan bir takım metotlar almıştır.



















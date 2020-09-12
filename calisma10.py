# -*- coding: utf-8 -*-
#                             ------SAYILAR------

#                         Tam Sayıların Metotları

print([i for i in dir(int) if not i.startswith("_")])# metotlar bunlar.
#%%                bit_length 
sayi = 10
print(sayi.bit_length())# kaç bit'lik yer kapladuığını söyler.
print((5).bit_length())# bu şekilde yazabiliriz.
#%%                      Noktalı Sayıların Metotları
print([i for i in dir(float) if not i.startswith("_")])# metotlar bunlar.
#%%               as_integer_ratio
sayi = 4.5
print(sayi.as_integer_ratio())# 9 ile 2'nin bölümü 4.5 verir.
#%%              is_integer
sayi = 11.5
print(sayi.is_integer())# False
print((11.0).is_integer())# True
#%%                      Karmaşık Sayıların Metotları
print([i for i in dir(complex) if not i.startswith("_")])# metotlar bunlar.
#%%             imag
c = 12+4j#                 sayının sanal kısmını verir.
print(c.imag)# 4.0 verdi.
a = 11+5.4j
print(a.imag)# 5.4 verdi.
#%%            real
a = 12+4j#                sayının gerçek kısmını verir.
print(a.real)# 12.0 verdi.
b = 11+5.4j
print(b.real)# 11.0 verdi.
#%%                       ARİTMETİK FONKSİYONLAR
#              abs()
print(abs(-9))# '9' çıktısı verir.
#%%            divmod()
print(divmod(10,2))# 10/2 işleminde sonuç:5 ve kalan:0 çıktısı verir.
#%%            max()
sayilar = [10,22,11,110,111,122,99]
print(max(sayilar))# sayilar listesi içindeki en büyük sayıyı yazdırdı.
kelime = ["serha","serdar","ahmet","nimet"]
print(max(kelime,key=len))# en uzun kelimeyi yazdırdı.
#%%            min() =  max()'un tam tersi.
#%%            sum()
sayilar = [10,20,30,11,40,50,60]
print(sum(sayilar))# sayiların toplamını verir.
print(sum(sayilar,10))# ikinci parametre toplanan sayılara eklenir.
         













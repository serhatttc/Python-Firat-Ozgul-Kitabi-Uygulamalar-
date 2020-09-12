# -*- coding: utf-8 -*-
#                            ---------İLERİ DÜZEY FONKSİYONLAR--------

#                       Lambda Fonksiyonları-----SAYFA---598---
# lambda, def gibi fonksiyon tanımlamamızı sağlar.
def fonk(param1,param2):
    return param1+param2
print(fonk(5,6))# 11
# aynı işemi lambda ile yapalım.
fonksiyon = lambda par1,par2:par1+par2
print(fonksiyon(5,6))# 11
# mesela liste içindeki sayıların karesini almak istiyoruz.
l = [5,2,3,11,9]
# şöyle yapabiliriz.
for i in l:
    print(i**2)
# şöyle yapabiliriz.
print([i**2 for i in l])
# şöyle yapabiliriz.
print(*map(lambda sayi:sayi**2,l))
# kısaca sözün özü bu..
#    lambda x: x+10
# 'x' adlı parametre alan lambda fonk. tanımla.
#  bu fonk. x parametresine 10 sayısını eklesin.
#%%  lambda birden fazla parametre alabilir.
# lambda fonksiyonu toplam 2 farklı parametre alır.
# bunlardan ilki ifade ikinci birleştirici.
birlestir = lambda ifade, birlestirici: birlestirici.join(ifade.split())
print(birlestir("Eskişehir Büyükşehir Belediyesi","-"))
# yukarıdaki örneklerin dışında lambda ile grafik arayüz çalışmalarında işe yarar.

#%%                 Özyinelemeli (Recursive) Fonksiyonlar----SAYFA--602----
def azalt(s):
    if len(s)<1:
        return s
    else:
        print(s)
        return azalt(s[1:])# burda azalt fonk. içinde yine azalt fonk. kullandık.
print(azalt("serhat"))
#%%
def sayac(baslangic,sinir):
    print(baslangic)# bu satır özyinelemeli fonk. her yinelenişinde sayı 
#  parametresinin durumunu ekrana basacak.
    if baslangic==sinir:# burası dip nokta yineleme bitince buraya gelir.
        return "bitti!"
    else:
        return sayac(baslangic+1,sinir)# burası dip noktaya ulaşıncaya kadar 
# yapılacak işlemler.Fonk. her yinelenişinde baslangic paramet. 1 arttırıyoruz. 
print(sayac(0,10))
#%%
l = [1,2,[3,4,[5,6],7],8,[9],10,11]
def duzListe(liste):
    if not isinstance(liste,list):# ilk olarak dip noktamızı tanımlıyoruz.
        return [liste]# eğer liste üzerinde ilerlerken karşımıza liste olmayan
#     bir eleman çıkarsa bu elemanı [liste] koduyla listeye dönüştürücez.
    elif not liste:# burası da 2. dip noktası.
        return []# eğer boş bir listeyle karşılaşırsak tekrar boş
#                bir liste döndürüyoruz.
    else:
        return duzListe(liste[0])+duzListe(liste[1:])# dip noktaya 
# ulaşıncaya kadar bu işlem yapılıyor.Yani listenin ilk ögesine
#   geri kalan ögeleri teker teker ekliyoruz.
print(duzListe(l))






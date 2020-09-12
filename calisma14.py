# -*- coding: utf-8 -*-
#                       --------KÜMELER VE DONDURULMUŞ KÜMELER-------

#               ------KÜMELER------

#                Küme OLuşturmak
bosKume = set()
# küme oluşturmak için set() fonk. yararlanırız.
print(type(bosKume))# <class 'set'> çıktısı verdi.
kume = set(["elma","armut","muz"])
# içinde öge olan küme de böyle oluşturulur.

#%% yukardakinin aynısını şöyle de yapabiliriz.listeden de küme oluşturulur.
liste = ["elma","armut","muz"]
meyveler = set(liste)
print(type(meyveler))
#%% karakter dizilerinden de küme oluşturulur.
karDiz = "a"
kume = set(karDiz)
print(type(kume))
#%%  demetlerden de küme oluşturulur.
demet = ("serhat","serdar","serap")
kume = set(demet)
print(type(kume))
#%%  sözlüklerden de küme oluşturulur.
sozluk = {"serhat":"çağlar","serdar":"çağlar"}
kume = set(sozluk)
print(type(kume))
print(kume)# sözlükle küme oluşturursak sadece anahtalar yazdırılır.
# ancak boş bir sözlük ile küme oluşturulamaz.
#%% ama sayılardan küme oluşturulamaz........
#%%                Kümelerin Yapısı
karDiz = "Python programlama dili"
kume = set(karDiz)
print(kume)#{'i', 't', ' ', 'p', 'l', 'm', 'd', 'a', 'o', 'n', 'P', 'h', 'y', 'r', 'g'}
# kümeler aynı ögeyi birden fazla tekrar etmez.
# çıktıda ögeleri sırası da farklı.

#%%               Küme Üreteçleri
import random
liste = [random.randint(0,10000) for i in range(1000)]
print(liste)
# bu kod 0 ie 10000 arasında 1000 tane rastgele sayı üretmemizi sağladı.
#%% şimdi amacımız liste içinde yer alan sayılardan 100'den küçük olanları bulmak.
import random
liste = [random.randint(0,10000) for i in range(1000)]
yuzdenKucuk = [i for i in liste if i <100]
print(yuzdenKucuk)
# ancak ortaya çıkan sayılardan aynısından birkaç tane olabilir.
#%% aynı sayılar olmaması için küme üreteçlerini kullanacaz.
import random
liste = [random.randint(0,10000) for i in range(1000)]
kume = {i for i in liste if i <100}
print(kume)
#%%               Kümelerin Metotları
#print(dir(set)) # metotlar bunlardır.
# bizim işimize yarayan metotları şöyle ayıralım.
for i in dir(set):
    if '__' not in i:
        print(i)# bize bunlar lazım.

#%%            clear()
# kümenin içini boşaltmak için kullanılır.
a = set("bilecik")
print(a)
for i in a:
    print(i)
a.clear()
print(a)# set() çıktısı geldi yani boş küme.
#%%            copy()
a = set("bilecik")
yedek = a.copy()
print(yedek)
#%%            add()
kume = set(["elma","armut","kiraz"])
kume.add("çilek")
print(kume)
# kümeye eleman eklemek için kullanılır.
#%% kümeye birden fazla öge eklemek istersek bunu yapabiliriz.
kume = set(["elma","armut","kiraz"])
yeni = [1,2,3]
for i in yeni:
    kume.add(i)
print(kume)# {'kiraz', 1, 2, 3, 'elma', 'armut'} çıktısı aldık.

#%% bir kümeye herhangi bir öge ekleyebilmemiz için o ögenin değiştirilemeyen
# (immutable) bir veri tipi olması gerekiyor.
#%% değiştirilemeyen veri tipleri=(demetler,sayılar,karakter dizileri)
# değiştirilebilen veri tipleri=(listeler,sözlükler,kümeler)
#%%
# önce boş bir küme oluşturalım.
kume = set()
# bu kümeye bir demet ekleyelim.
demet = (1,2,3)
kume.add(demet)
print(kume)
# sayı ekleyelim.
sayi = 45
kume.add(sayi)
print(kume)
# karakter dizisi ekleyelim.
karDiz = "serhat"
kume.add(karDiz)
print(kume)
# liste,sözlük ve küme ekleyemeyiz.

#%%            difference()
# iki kümenin farkını almamızı sağlar.
k1 = set([1,2,3,4])
k2 = set([3,5,2,11])
print(k1.difference(k2))# k1'in k2'den farkı ||  {1, 4}  çıktısı verdi.
print(k2.difference(k1))# k2'nin k1'den farkı || {11, 5}  çıktısı verdi.
# ısaca aynısını bu şekilde de yapabiliriz.
print(k1-k2)
print(k2-k1)
#%%           difference_update()
# kümenin farkını alır ve sonra diğer ögeleri silip fark olan ögeyi bırakır.
k1 = set([1,2,3]) 
k2 = set([1,3,5])
k1.difference_update(k2)
print(k1)# k1'in k2'den farkı sadece 2 ögesiydi ve diğerlerini silip sadece onu bıraktı.
print(k2)# k2 olduğu gibi kaldı.
#%%          discard()
# kümeden öge çıkarmamızı sağlayan metot.
hayvanlar = set(["kedi","köpek","ayı","kuş","yılan"])
hayvanlar.discard("kedi")# kedi ögesini çıkardık.
print(hayvanlar)
# kümede olmayan bir ögeyi silmeye kalkarsak hata vermez.
#%%          remove()
# discard() ile aynıdır.öge siler.olmayan ögeyi silmek istersek hata verir.
hayvanlar = set(["kedi","köpek","ayı","kuş","yılan"])
hayvanlar.remove("yılan")
print(hayvanlar)
#%%         intersection()
# iki kümenin kesişimini almamızı sağlar. 
k1 = set([1,2,3,4])
k2 = set([3,5,2,11])
print(k1.intersection(k2))# {2, 3}  çıktısı verdi.
# aynısını böylede yapabiliriz.
print(k1&k2)# aynı çıktıyı verdi.
#%%          intersection_update()
k1 = set([1,2,3,4])
k2 = set([3,5,2,11])
k1.intersection_update(k2)# burda {2,3} geliyor.
print(k1)# ve k1'i  {2,3} halıne güncelliyor.
print(k2)
#%%         isdisjoint()
# kesişim kümesinin boş olup olmadığını sorgular.
k1 = set([1,2,3])
k2 = set([4,5,6])
print(k1.isdisjoint(k2))# True çıktısı verdi yani kesişim boş küme.
#%%           issubset()
# bir kümenin başka bir kümenin alt kümesi olup olmadığını sorgular.
k1 = set([1,2,3,4]) 
k2 = set([1,2,3,4,11,26,22])
print(k1.issubset(k2))# k1 k2'nin alt kümesimi diye sorduk.True çıktısı verdi.
#%%           issuperset()
# bir kümenin diğer kümeyi kapsayıp kapsamadığını sorgular.
k1 = set([1,2,3,4]) 
k2 = set([1,2,3,4,11,26,22])
print(k2.issuperset(k1))# k2 k1'i kapsıyor mu diye sorduk.True çıktısı verdi.
#%%          union()
# iki kümenin birleşimini almamızı sağlar.
a = set([1,3,5,7])
b = set([2,4,6,8])
print(a.union(b))# {1, 2, 3, 4, 5, 6, 7, 8}  çıktısı verdi.
# aynısını böylede yapabiliriz.
print(a|b)# aynı çıktıyı verdi.
#%%          update()
# kümeyi güncellememizi sağlar mesela liste olan veriyi tek tek kümeye aktarır.
a = [1,2,3]
b = set(["serhat",5,"serdar",4])
b.update(a)# a listesindeki ögeleri tek tek b kümesine aktardık.
print(b)
#%%         symmetric_difference()
# iki kümede de bulunmayan ögeleri aynı anda verir.
a = set([1,2,5])
b = set([1,4,5])
print(a.symmetric_difference(b))# a ile b arasındaki farkları yaz dedim.
# {2, 4}  çıktısı verdi.
# a'da olup b'de olmayan {2},b'de olup a'da olmayan {4}
#%%         symmetric_difference_update()
# önceki update metotları gibi iki kümenin birbirinden farkını yazıp kümeyi değiştiriyor.
a = set([1,2,5])
b = set([1,4,5])
a.symmetric_difference_update(b)
print(a)# {2, 4}  çıktısı verdi.
print(b)# {1, 4, 5}  çıktısı verdi.
#%%          pop()
# küme ögelerini rastgele siler ve ekrana yazar.
b = set(["serhat",5,"serdar",4])
print(b.pop())# 'serhat' ögesini sildi ve ekrana yazdırdı.
print(b)

#%%                       Dondurulmuş Kümeler(Frozenset)
# Eğer ögeleri üzerinde değişiklik yapılamayan bir küme oluşturmak istersek 
# set() yerine frozenset() fonksiyonunu kullanabiliriz.
dondurulmus = frozenset(["serhat","serdar","ahmet","nimet"])

print(dir(frozenset))# metotları bunlardır.









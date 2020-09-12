# -*- coding: utf-8 -*-
#                             -----  NESNE TABANLI PROGRAMLAMA  ---(DEVAMI)---

#            ----  İnşa,İlklendirme Ve Sonlandırma  ----

# Python'da bir sınıfın ömrü 3 aşamadan oluşur;
# 1) İnşa(construction)|| 2) İlklendirme(initialization)|| 3) Sonlandırma(destruction)

# Python'da bir sınıfı ilklendirmek için __init__() metodundan yararlanıyoruz.
# ancak ilklendirme sınıf oluşturmanın ilk aşaması değidir.İlklendirmeden önce
# o sınıfı inşa eder inşa işleminin sorumlu metodu ise __new__() metodudur.

#%%         ----  __new__() Metodu  ----

# Python'da basit bir sınıfı şu şekilde oluşturuyoruz.

class Sınıf():
    def __init__(self):
        print("merhaba sınıf.")
# burada __init__() metodu sınıf örneklenir örneklenmez hangi işlemlerin yapılacağını gösterir.

snf = Sınıf() # merhaba sınıf. çıktısı verdi
# görüğümüz gibi __init__ metodunda tanımladığımız şekilde örneklediğimiz anda çıktıyı verdi.
#%%
# Ancak yukarıda belirtildiği gibi aslında örneklendiğinide ilk __init__ çalışmaz
# alttan alttan aslında __new__() çalışır gelin bakalım.
class Sınıf():
    def __new__(cls):
        pass
    def __init__(self):
        print("merhaba sınıf.")

snf = Sınıf()
# çıktı vermedi çünkü biz __new__ metodunun işleyişini bozduk.aslında böyledir.
#%%
class Sınıf():
    def __new__(cls,*args,**kwargs):
        return object.__new__(cls,*args,**kwargs)
    
    def __init__(self):
        print("merhaba sınıf.")

#%% aslında Python yukarıdaki sınıfı şöyle görür.
class Sınıf(object):
    ....







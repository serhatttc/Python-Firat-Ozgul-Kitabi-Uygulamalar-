# -*- coding: utf-8 -*-
#                                  -----  PAKETLER  -------SAYFA--771-- 

#                 ----  Paket Nedir?  ----

# Python'da bir dizin yapısı içinde biraraya getirilen birbiriyle bağlantılı 
# modüllere paket denir.

# Paketler de __path__ adlı nitelik vardır, modüller de yoktur.
#import os
#os.__path__
# bu hata verir çünkü os modülünde __path__ niteliği yoktur.
# gelin json paketini deneyelim
import json
json.__path__
# burda çalışır. çünkü json bir pakettir.

#%%                   ----  Paket Türleri  ----

#        ----  Standart Paketler  ----

# standart paketler python'ın kütüphanesinde bulunan paketlerdir.
# bunla bu dilin parçası olduğu için bunlara ulaşabilmek için ek bir yazılım
# indirmemize gerek yoktur.
# standart paketlere python kurulum dizini içindeki Lib klasöründen erişebiliriz.

# bu standart paketin hangi konumda olduğunu öğrenmek için ilgili paketin
# __path__ niteliğini sorgulayabiliriz.

import urllib
urllib.__path__
# eğer sorguladığınız şeyin bir __path__ niteliği yoksa o bir paket değildir.
# yukarıdaki çıktıdaki dosyaya girip baktığımızda bu paketin hangi
# modüllerden oluştuğunu görebiliriz.

#%%      ----  Üçüncü Şahıs Paketleri  ----

# bunlar python'ın içinde bulunmaz başkaları tarafından yazılmış paketlerdir.
# django,kivy,cx_freeze birer üçüncü şahıs paketleridir.

# bir sitede paketin adını öğrendikten sonra;
# pip3 install paket_adı
# komutuyla paketi yükleyebiliriz.

# django'nun son sürümünü inirdik ve şimdi kuralım.

# pip install Django==3.0.5

#%%     ----  Paketlerin İçe Aktarılması  ----

# import os   ..... os modülünü böyle içe aktardık.
# eğer os modülünün name niteliğini almak istersek şunu yaparız.
# from os import name  
# os modülündeki bütün nitelik ve metotları içe aktarmak istediğimizde şunu yaparız.
# from os import*
# bu modül içindeki metot ya da niteliği başka isimle de içe aktarabiliriz.
# from os import execv as exe

#%%     ----  import Paket  ----

# mesela urllib paketini ele alalım os modülü gibi içe aktarabiliriz.
import urllib
# ancak paketler modüller gibi hemen içeri aktarılmaz bu işi açık açık belirtmeiliyiz.
#%%      ---- import paket.modül  ----

# mesela urllib paketinden request modülünü içe aktarmak istersek şu komutu yazarız.
import urllib.request
# bu modülü yukardaki gibi içeri aktardığımızda modül içindeki nirelik ve 
# metotlara 'urllib.request' önekiyle erişebiliriz.
urllib.request.urlopen("http://www.asdfgwe.com")
#%%      ----  from paket import modül  ----

from urllib import request
# böyle içe aktarım yaparsak request modülünün içindeki nitelik ve metotlara
# ulaşmak istediğimizde sürekli urllib.request yazmak zorunda kalmayız.
# request modülünün nitelik ve metotlarına sadece 'request.' yazarak ulaşabiliriz.
request.urlopen("http://www.asdfgwe.com")
#%%   ----  from paket.modül import nitelik veya metot  ----

from urllib.request import urlopen
# bu şekilde urllilb paketi içindeki request modülünün urlopen metodunu
# doğrudan içe aktarmış oldu.dolayısıyla bu metodu dümdüz kullanabiliriz.
urlopen("http://www.asdfgwe.com")

#%%    ----  from paket.modül import*  ----

from urllib.request import*
# bu şekilde urllib paketinin içindeki request modülünün bütün nitelik ve 
# metotlarını içe aktarmış olduk.

#%%               ----  Kendi Oluşturduğumuz Paketler  ----

#           ----  Paket Oluşturmak  ----

# siparistakip adlı bir klasör oluşturduk ve içine veritabanı.py,siparis.py
# komut.py dosyaları koyduk. ve siparistakip paketini oluşturduk.

import siparistakip
dir(siparistakip)
# içinde __path__ adlı nitelik var yani bu bir paket.
# ya da paket içeriğindeki __package__ ile de buna bakabiliriz.
siparistakip.__package__
# eğer bu komutu yazdığımızda paketin adını veriyorda bu pakettir.
# ama eğer boş bir karakter dizisi çıktısı veriyorsa bu paket değildir.
import os
os.__package__
# bu zaten modül bunu biliyoruz.

#%%         ----  İçe Aktarma İşlemleri  ----

# mesela masaüstünde bir paket oluşturalım.
import paket
dir(paket)
# gördüğümüz gibi oluşturduğumuz paket Python paketinin sahip olması gereken
# bütün niteliklere sahip.

#%% şimdi paket içindeki modul1 adlı modülü içe aktaralım.

from paket import modul1
# modul1 çıktısı verdi.
#%% peki modul1 içindeki isim1 değişkenini almak istersek ne yapacaz.
from paket.modul1 import isim1
#%%
import paket.altdizin
# içe aktardık bu şekilde altdizin içindeki modğllere ve onların niteliklerinde 
# ulaşabiliriz.
paket.altdizin.altmodul1.altisim1
#%%
from paket.altdizin import altmodul1
altmodul1.altisim1
#%%
from paket.altdizin.altmodul1 import altisim1
altisim1
# mantığı kavradım gibi sırasıyla .'larla birleştirerek içe aktarıyoruz.

#%%                 ----  İçe Aktarma Mantığı  ----

#     ----  İçe Aktarma İşleminin Konumu  ----

# Python içe aktarma işlemlerini tek bir konumdan gerçekleştirir.
# yukarıda bir paket oluşturmuştuk.
# şimdi altmodul2.py dosyasının içine şunu yazalım.
# import altmodul1

# şimdi paket adlı dizinin bulunduğu klasörde etkileşimli kabuk açalım.
# ve şunu yazalım.
from paket.altdizin import altmodul2

#%%      ----  Bağıl İçe Aktarma  ----
# altmodul2.py dosyasına bunu yazıyoruz.
from . import altmodul1
# yaparsak (.) demek altmodul2.py dosyasının bulunduğu dizine atıfta bulunmak demek.
#%% mesela modul3.py dosyasını altmodul1 veya altmodul2.py dosyasında içe 
# aktaralım.bunu yazacağız.
from .. import modul3 
# (..) koymak bir üst dizine atıfta bulunmak demek
#%% mesela altaltmodul1.py dosyasının içine modul1.py dosyasını içe aktarmak istiyoruz.
from ... import modul1
# (...) koymak iki üst dizine atıfta bulunmak demektir.

#%%      ----  Paketlerin Yola Eklenmesi  ----

# sys.path'e eklenmemiş bir paketi heryerden içe aktaramayız.
# peki bir paketi sys.path listesine nasıl ekleyeceğiz
# bir paketi sys.path listesine eklerken paket adına karşılık gelen dizini değil,
# paketi içeren dizini bu listeye eklemeliyiz.

import os, sys# öncelikle gerekli modülleri içe aktardık.
kullanıcı = os.environ["HOMEPATH"]# kullanıcı dizininin nerede olduğunu tespit ettik.
masaüstü = os.path.join(kullanıcı,"Desktop")# masaüstüne giden yolu bulmak için bu komutu verdik.
sys.path.append(masaüstü)# masaüstünün yolunu sys.path'e ekledik.
# böylece masaüstünün bulunduğu dizini sys.path'e ekledik.






















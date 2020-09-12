# -*- coding: utf-8 -*-
#                                   --------MODÜLLER--------SAYFA--615---

# Modüller bazı işlevleri kolaylıklla yerine getirmemizi sağlayan birtakım
# fonksiyonları ve nitelikleri içinde barındıran araçlardır.

# Modüllerde fonksiyonlar gibi iki çeşit 1. Kendi tanımladığımız modüller,
# 2. Hazır modüller
#%%                   -----  Hazır Modüller  ------

#  >>Standart Kütüphane Modülleri
# *Doğrudan Python geliştiricileri tarafından yazılıp dile kaynaştırılmış modüller.

#  >>Üçüncü Şahıs Modülleri

#%%               -----   Modüllerin İçe Aktarılması  -----

# içe aktarmak modül içindeki fonk. ve nitelikleri kullanılabilir hale getirmektir.
import os
# bunu yaparak 'os' adlı modülü içe aktarmış olduk.
# 'os' modülünün içinde hangi fonk. ve nitelikler olduğuna bakmak için bunu yapalım.
# print(dir(os))
# 'os' kelimesi operating system(işletim sistemi) kısaltmasıdır.
print(os.name)# nt çıktısı verdi.(Windows)
# 'name' niteliğini kullanarak kodaların hangi iş. sis. çalıştığına bakabiliriz.  
if os.name != "nt":
    print("Program sadece Windows'ta kullanılabilir.")
else:
    print("Hoşgeldin Windows kullanıcısı.")

# bir modülü içe aktardıktan sonra modülü kapatana kadar tekrar içe aktarmak zorunda değiliz.

#%%               -----  Farklı İçe Aktarma Yöntemleri  -----

#  ---  import modül_ismi as farklı_isim

# bunu alatırken 'subprocess' adlı modülden yararlanıcaz.
# 'subprocess' ile Python programları içinden başka programları çalıştırabiliriz.
import subprocess
print(subprocess.call("falanca.exe"))
# 'subprocess' modülünün 'call()' fonk. ile "falanca" programını Python içinde çalıştırdık.
# 'subprocess' adı uzun olduğu için kullanırken zor gelebilir onun için değiştirelim.
import subprocess as sp
# yani yukarda yaptığımız 'import modül_ismi as farklı_isim'
# böylece artık bu modülü 'sp' yazarak kullanabiliriz.
print(sp.call("falanca.exe"))
# başka bir modülden örnek verelim.
import webbrowser as wbr
print(wbr.open("www.bilmemnesitesi.cmm"))
# 'webbrowser' modülü PC'de kurulu internet tarayıcısını kullanarak siteleri açmamızı sağlar.
# Bazı GNU/Linux dağıtımlarında site açarken "http:" yazmamız gerekebilir.

#%%  --- from modül_ismi import isim1,isim2

# os modülünü kullanırken içindeki hepsine ihtiyaç duymayız.
from os import name
print(name)# bu sayede bunu bu şekilde kullanabiliriz.
# birden fazla nitelik ve fonk. da ekleyebiliriz.
#   from os import name,listdir,getcwd    gibi.

#%% --- from modül_ismi import isim as farklı_isim

from os import listdir as ld
# bu yaptığımız demek os modülü içindeki listdir fonksiyonunun ismini ld yaptık.

#%% --- from modül_ismi import*

from sys import*
# böylelikle sys modülü içindeki bütün fonksiyonları ve nitelikleri başlarına 
# modül adı koymadan kullanabiliriz.
print(version_info)
# bu yıldızlı işlemi lokal etki alanında kullanamayız.Diğerlerini kullanabiliriz.
#  def fonk():
#      from os import*
# YAPAMAYIZ.
# bu işlemi sadece global etki alanında gerçekleştirebiliriz.

#%%               ----- Kendi Tanımladığımız Modüller -----

#   ---- Modüllerin Tanımlanması

import os # önce içe aktaralım
# os modülü içinde __file__ niteliği bulunur.Tüm modüllerde bulunur.
print(os.__file__)#  C:\Users\hp\Anaconda3\lib\os.py  ||  çıktısı verdi.
# işte buradan aldığımız çıktı os modülünün kaynak doyasının nerede olduğunu gösterir.
# çıktıda görünen os.py dosyasına bakalım ve bu bir Python programı.

# Ancak her modül Python ile yazılmamıştır.Bazıları C ile yazılmıştır.Mesela 'sys'
# modülü.Bu modül C ile yazıldığından .py uzantılı dosyası yoktur.Yani __file__
# adlı bir niteliği de yoktur.

# Yazdığımız her Python programı potansiyel bir modüldür.
#%%
## mesela bir program dosyası oluşturalım adı sozluk.py olsun.Bu programın modül adı 'sozluk'.
#sozluk = {"bilgisayar" :"computer",
#            "kitap"    :"book",
#            "slice"    :"dilim"}
#def ara(sozcuk):
#    hata = "{} kelimesi sözlükte yok!"
#    return sozluk.get(sozluk,hata.format(sozcuk))
# böylelikle ilk modülümüzü tanımlamış olduk.
#  import sozluk     yazarak modulu çağırabiliriz.

#%%  ---  Modüllerin Yolu       

# Python kendi modüllerini her dizinde çalıştırır ama bizim yazdığımız modüller
# her dizinde çalışmaz.Biz import modül_ismi komutu verdiğimizde Python bunun için
# arama işlemi başlatır tabi sabit diskin tamamında aramaz.Belli bir takım dizilerin 
# içinde arar.Bu dizinleri görmekk için sys modülünün path niteliğini kullanabiliriz.
import sys
print(sys.path)# işte bu dizilerde aramayı gerçekleştirir.Eğer modül dosyasını,
# bu dizilerin içinde bulursa içe aktarır.Bulamazsa 'ImportError' hatası verir.
# Biz yazdığımız modülü ya bu dizilerin içine koyucaz,ya da sys.path içine ekleme yapıcaz.
# sys.path bir liste çıktısı verir.Ve biz listelerde nasıl değiişiklik yapıcaz biliyoruz.
#   sys.path.append(r"C:\\sss\\eee\\ccc")
# gibi bir dosya ekledik ve artık Python burda da modül ararken arama yapacak.
# bu yaptığımız ilk yöntemdi.
#%% ikinci yöntemimizde ilgili modül dosyasını ys.path çıktısında olan 
# dizinlerden herhangi birine kopyalamaktır. 
# yaygın olarak tercih edilen konum Python kurulum dizini içindeki site-packages
# adlı dizindir.Bu dizinin yerini şöyle tespit edebiliriz.
from distutils import sysconfig
print(sysconfig.get_python_lib())
# modül dosyanızı bu çıktının içine kopyaladıktan sonra heryerden içe aktarabilirsiniz.

# sys.path ile ilgili önemli bir bilgi daha verelim.
# Python modülü ararken sys.path içindeki dizinleri soldan-sağa doğru okur.
# ve bulunca da okumayı bırakır,modülü içe aktarır. 
# yani bazı modüllere öncelik vermek istiyorsanız o dizini append() ile 
# listenin sonuna eklemek yerine, insert() ile istediğiniz yere ekleyebilirsiniz.
#    sys.path.insert(0,r"C:\\sss\\eee\\ccc")
# başa eklemiş olduk.

#%%              -----  Modüllerde Değişiklik Yapmak  -----
# daha önceden sozluk adlı bir modül oluşturmuştuk.Onu kullanalım.
import sozluk

print(dir(sozluk))#bu modül içindekileri gördük.içinde ara() fonk. ile 
# sozluk niteliği bulunuyor.
#   sozluk.ara("kitap")
# bu bize ara() fonksiyonunu kitap argümanı ile çağırma imkanı veriyor.

# Şimdi sozluk.py dosyasına ekleme yapıcaz.Eklemeyi yaptık.
# sozluk modülüne ekle() fonksiyonunu ilave ettik.Bu fonk. sözlüğe yeni kelimeler 
# eklememizi sağlayacak.

# modülü değiştirdikten sonra kendini hemen yenilemeyebilir.
# onun için ya kapatıp açıcaz ya da aşağıdakini yapıcaz.
#  import importlib
#  importlib.reload(sozluk)

sozluk.ekle("araba","car")
sozluk.ara("araba")
# şimdi modülümüze bir ekleme daha yapalım.
sozluk.sil("kitap")

#%%                -----  Üçüncü Şahıs Modülleri  -----SAYFA--634--
# Üçüncü şahıs modülleri bu dilin parçası değildir.
# Bunları kullanmak için modül geliştiricisinin koyduğu yerden PC'ye kurmalıyız.

# pip3 install django
# django adlı modülü indirmek için yaptık.pip3 demek Python 3.x sürüm demek.
# yani pip3 install modül_ismi olarak yapılır.

#%%               -------  __all__ Listesi  ------

# şimdi module1.py adlı bir dosya oluştuduk.
import module1 # içe aktardık.
print(dir(module1))# modülün içeriğine baktık.
# Modül içindeki bütün fonksiyonlar bu listede var.
#Fonksiyonlara da bu şekilde erişebiliriz.
module1.fonk1()
module1.fonk5()
#%% yukardaki içe aktarımı kapattık ve tekrardan açtık.
# bu sefer içe aktarımı bu şekil yapıcaz.
from module1 import *
# bu şekilde ismi '_' ile başlayanlar hariç bütün fonksiyonlar içe aktarılır.
# artık fonksiyonları module1 ön eki olmadan kullanabiliriz.
fonk4()
fonk5()
# ismi '_' ile başlayanları da böyle çapırabiliriz.
from module1 import __fonk7

#%% Biz yazdığımız programda yalnızca kendi blirlediğimiz isimlerin içe aktarılmasını istersek.
# Bunları yapıcaz.
#  __all__ = ["fonk1","fonk2","fonk3"]
# Şimdi module1.py dosyasının en başına bu satırı ekleyelim.
# şimdi modülü içe aktaralım.
from module1 import *
print(dir())

#%%               -----  Modüllerin Özel Nitelikleri  -----
moduller = ["os","sys","subprocess"]# istediğimiz modülleri tutan liste tanımladık.
def kesisimBul(moduller):
    kumeler = [set(dir(__import__(modul)))for modul in moduller]
    return set.intersection(*kumeler)
print(kesisimBul(moduller))
#  {'__loader__', '__doc__', '__package__', '__name__', '__spec__'}
#  __import__() fonk. modül adlarını içeren karakter dizilerini kullanarak
# herhengi bir modülü içe akratmamızı sağlar.
# bu fonk. şöyle kullanıyoruz.
#  __import__("os")   gibi
# yalnız bu kullanımda 'os' ismi kulanılamıyor.Kullanabilmek için şunu yapalım.
# os = __import__("os")

#%%             ----  __doc__ Niteliği  ----

# bir örenekle anlatalım.os.py dosyasını açalım ve ilk baştaki yeşil yazılara bakalım.
# şimdi şunu yapalım.
import os
print(os.__doc__)
# bu bize o yeşil satırları verdi.buna belge dizisi(docstring) ya da belgelendirme
# dizisi(documentation string) denir.
# bu belge dizileri üç tırnak içinde belirtilir.

#%%           ----  __name__ Niteliği  ----    SAYFA--643--
print(__name__)
#â eğer bir python programı başka bir program içinden modül olarak içe aktarılıyorsa
# __name__ niteliğinin değeri o modülün adı olur.

# eğer bir python programı doğrudan bağımsız bir program olarak çalıştırılıyorsa
# __name__ niteliğinin değeri bu defa __main__ olacak.

#%%        ----  __loader__ Niteliği  ----

# bu nitelik ilgili modülü içeri aktaran mekanizma hakkında bilgi veren araçlar sunar.
import os
yukleyici = os.__loader__
print(dir(yukleyici))

#%%         ----  __spec__ Niteliği  ----

# modülün ad ve konum bilgilerine ulaşmak için bunu kullanabiliriz.
import subprocess
adi = subprocess.__spec__.name
konumu = subprocess.__spec__.origin
print(adi)
print(konumu)

#%%          ----  __package__ Niteliği  ----
# Bu niteliği paketler konusunda göreceğiz.









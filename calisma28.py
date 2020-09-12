# -*- coding: utf-8 -*-
#                               ----  ÖNEMLİ STANDART KÜTÜPHANE MODÜLLERİ  ----

#                   ---  os Modülü  ---

#           ---  os.name  ---(nitelik)

# yazdığımız kodları hangi işletim sisteminde çalıştırdığı konusunda bilgi verir.

import os
print(os.name) # 'nt' çıktısı verdi.Kodlarımız Windows işletim sisteminde çalıştırılıyor.

# MacOs ve GNU/Linux işletim sistemlerinde ise 'posix' çıktısı verir.

#%%         ---  os.sep  ---(nitelik)

# kodlarımızın çalıştığı işletim sisteminin dizin ayracının ne olduğunu gösterir.

print(os.sep)# '\' .ıktısı verdi Windows'ta bu ayraç kullanılıyor.

# MacOs ve GNU/Linux 'ta '/' ayracı kullanılır.

liste = ["ocak","şubat","mart"]
os.sep.join(liste)# 'ocak\\şubat\\mart'  || çıktısı verdi.

#%%        ---  os.getcwd()  ---(fonksiyon)

# bize o anda içinde bulunduğumuz dizini verir.

os.getcwd()# 'C:\\Python\\KitapCalisma'   || mesela şu anda bu dizindeyiz.

#%%        ---  os.chdir()  ---(fonksiyon)

# bize bir dizinden başka bir dizine geçme imkanı verir.

os.chdir(r"C:\Users\hp\Desktop")# içine geçmek istediğimiz dizini yazıyoruz.

#%%        ---  os.listdir()  ---(fonksiyon)

# bize bir dizin içindeki dosya ve klasörleri listeleme imkanı verir.

#os.listdir(dizin_adi)

#%%        ---  os.curdir  ---

# çoğu işletim sisteminde mevcut dizini göstermek için '.' karakter dizisi kullanılır.

# 'os.curdir' o anda içinde bulunulan dizini temsil eden karakter dizisi ne
# ise onun değerini barındırır.Bu genelde '.'dır.

#os.getcwd('.') şu an bulunduğumuz dizini gösterir.

#%%        ---  os.pardir  ---

# tıpkı '.' gibi çoğu işletim sisteminde bir üst dizini göstermek için '..' kullanılır. 

#os.listdir('..') 
# bu komut bir üst dizindeki dosya ve klasörleri listeleyecektir.

#%%       ---  os.startfile()  ---(fonksiyon)

# bu fonksiyon yalnızca Windows'ta çalışır.
# bilgisayarımızda bulunan herhangi bir dosyayı ilişkilendirilmiş olduğu programla açar.

#os.startfile('deneme.txt') bunu notepad programıyla açar.
#os.startfile('denem.docx') bunu Microsoft Word ile açar.

#%%       ---  os.mkdir()  ---

# yeni dizinler oluşturabilmemizi sağlar.

#os.mkdir('yenidizin') bu şekilde şu an bulunduğum dizinde 'yenidizin' adlı bir 
# dizin oluşturur.

# başka bir dizinde yenidizin oluşturmak istiyorsak oranın tam yolunu girmemiz gerek.

#%%        ---  os.makedirs()  ---

# 'mkdir'le aynı gibidir ama farkı olarak 'mkdir' tek bir dizin oluşturabilir.
# 'makedirs' ise alt ve üst dizinlerle birlikte yani birden fazla dizin oluşturabilir.

#%%      ---  os.rename()  ---

# bu fonksiyonla dizilerin adlarını değiştirebiliriz.

os.rename("dizinin_simdiki_adi","dizinin_yeni_adi")

#%%      ---  os.replace()  ---

# 'rename' ile aynı çalışır.

#%%      ---  os.remove()  ---

# bu fonksiyon bilgisayarımızdaki dosyaları silmemizi sağlar.

os.remove("dosya_adi")

#%%       ---  os.rmdir()  ---

# bu fonksiyon içi boş bir dizini silmek için kullanılır.

# bu dizinin içinde başka bir dizin veya dosya varsa hata verir.

#%%      ---  os.removedirs()  ---

# bu fonksiyon içi boş ana dizin yollarını silmemizi sağlar.

os.removedirs(r"anadizin/dizin1/dizin2/dizin3/dizin4")

# yani burda bütün dizinlerin içi boşsa hepsini tek tek siler.(anadizin,dizin4 dahil.)

#%%       ---  os.stat()  ---

# bu fonksiyonla dosyalar hakkında bilgi alabiliriz.dosyanın boyutu,oluşturma tarihi,
# değiştirilme tarihi,erişilme tarihini sorgulayabiliriz.

dosya = os.stat("dosya_adi")
dosya.st_atime#son erişilme tarihi
dosya.st_ctime# oluşturulma tariihi(windows'ta)
dosya.st_mtime# değiştirilme tarihi
dosya.st_size# boyutu

#%%       ---  os.system()  ---

# bu fonksiyon Python içinde sistem komutlarını veya başka programları çalıştırabilmemizi sağlar.

os.system("notepad.exe")

#%%         ---  os.urandom()  ---

# bu fonksiyon rastgele bayt dizileri elde etmek için kullanılır.

os.urandom(12)
# bu komut 12 bayttan oluşan rastgele bir dizi oluşturur.

#%%         ---  os.walk()  -------SAYFA----856---
import os

os.listdir('.')

#%%        ---  os.environ()  ---

# kullandığımız işletim sistemindeki çevre değişkenleri hakkında bilgi edinmemizi sağlar.
import os

for k,v in os.environ.items():
    print(k.ljust(10),v)
    
os.environ("USERNAME")

#%%                        ---  os.path()  ---

# bu nitelik içinde pek çok fonk. ve nitelik barındırır bakalım şimdi hepsine.

#%%        ---  os.path.abspath()  ---

# bir doyanın tam yolunun ne olduğunu söyler.

os.path.abspath("asker.py")
#  'C:\\Python\\KitapCalisma\\asker.py'   çıktısı verdi.

#%%       ---  os.path.dirname()  ---

# bir doya yolunun dizin kısmını verir.

os.path.dirname(r"C:\Python\KitapCalisma")
#  'C:\\Python'   çıktısı verdi.

#%%       ---  os.path.exists()  ---

# bir doya veya dizinin var olup olmadığını kontrol eder.

os.path.exists(r'C:\\Python\\KitapCalisma\\asker.py')
#  True   çıktısı verdi.

#%%       ---  os.path.expanduser()  ---

# bilgisayardaki kullanıcıya ait dizinin adresini verir.

os.path.expanduser('~')

#os.path.expanduser('~isim')

# bu kodla da windows'ta belirli bir kullanıcı ismi ve dizini oluştureabiliriz.

#%%       ---  os.path.isdir()  ---

# kendisine parametre olarak verilen ögenin dizin olup olmadığını sorgular. 

os.path.isdir(r"C:\Python\KitapCalisma")
# True  çıktısı verdi.

#%%       ---  os.path.isfile()  ---

# kendisine parametre olarak verilen ögenin dosya olup olmadığını sorgular.

os.path.isfile(r'C:\\Python\\KitapCalisma\\asker.py')
# True  çıktısı verdi.yani bu bir dosya.

#%%      ---  os.path.join()  ---

# kendisine verilen parametrelerden ilgili işletim sistemine uygun yol adresleri oluşturur.

os.path.join("dizin1","dizin2","dizin3")
# 'dizin1\\dizin2\\dizin3'   çıktısı verdi.

#%%        ---  os.path.split()  ---

# bir yol adresinin son kısmını baş kısmından ayırır.
import os

os.path.split(r"C:\Python\KitapCalisma")
# ('C:\\Python', 'KitapCalisma')    bu şekil.

#%%       ---  os.path.splitext()  ---

# dosya adı ile uzantısını birbirinden ayırmak için kullanılır.

os.path.splitext('asker.py')
#  ('asker', '.py')    bu şekil bir çıktı verir.

#%%                     ----  sys Modülü  ----

# Python sürümü ile ilgili bilgi edinmemizi ve çeşitli işlemler yapabilmemizi sağlar.

#%%         ---  sys.exit()  ---

# programımızın işleyişini durdurabilir, kapatmaya zorlayabiliriz.

import sys

sayi = int(input("sayı gir :"))

if sayi == 11:
    print("BİLECİK")
else:
    print("Yanlış yol...")
    print("çıkılıyor...")
    sys.exit()

#%%        ---  sys.argv  ---------SAYFA----866-

# yazdığımız program çalıştırılırken kullanılan parametreleri bir liste halinde tutar.

#%%      ---  sys.executable  ---
    
# eğer yazdığımız programda programınızın çalıştığı sistemdeki Python'ın
# çalıştırılabilir dosyanın adını ve yolunu öğrenmeniz gerekirse bunu kullanırız.

sys.executable
# 'C:\\Users\\hp\\Anaconda3\\pythonw.exe'    çıktısı verdi.

#%%      ---  sys.getwindowsversion()  ---

# kullanılan windows sürümüne ilişkin bilgi verir.

sys.getwindowsversion()

#%%     ---  sys.platform  ---

# kodlarımızın çalıştığı işletim sistemi hakkında bilgi verir.

sys.platform
# 'win32'   çıktısı verdi.

#%%     ---  sys.prefix  ---

# Python'ın hangi dizinde kurulduğunu gösterir.

sys.prefix
# 'C:\\Users\\hp\\Anaconda3'    çıktısı verdi.

#%%     ---  sys.ps1  ---

# etkileşimli kabuktaki '>>>' işaretini tutar.

sys.ps1

#%%       ---  sys.ps2  ---

# etkileşimli kabukta Python'ın bizden girdiğimiz kodların devamını beklediğini
# göstermek için '...' işaretini kullanır.

#%%     ---  sys.version  ---

# kullandığımız Python sürümüne ilişkin ayrıntılı bilgi verir.

sys.version
# '3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 64 bit (AMD64)]'   çıktısı.

#%%     ---  sys.version_info  ---

# kullandığımız Python sürümüne ilişkin bilgi verir.

sys.version_info

# sys.version_info(major=3, minor=7, micro=4, releaselevel='final', serial=0)  çıktısı.

#%%     ---  sys.winver  ---

# Python'ın büyük sürüm numarası ile küçük sürüm numarasını verir.

sys.winver
#  '3.7'  çıktısı verdi.

#%%      ---  sys.stdout  ---

# standart çıktı konumu
# standart çıktı konumunun neresi olacağını gösterir.
f = open("cıktılar.txt","w")
sys.stdout = f
sys.stdout("zalim dünya")
# bu yazıyı 'çıktılar.txt' dosyasına yazdıracak.

#%%      ---  sys.stderr  ---

# standart hata konumu
# önceki bölümdeki örnekte yazıyı 'çıktılar.txt' ye yazdırmıştık,bu nitelikle de
# ortaya çıkan hata kodlarını dosyaya yazar.

f = open("hatalar.txt","w")
sys.stderr = f
sys.stderr.write(1/10)

#%%      ---  sys.stdin  ---

# standart girdi konumu
# verileri kullanıcıdan input() yerine sys.stdin ile de alabiliriz.


#%%               ----  random Modülü  ----

# belirli aralıklarda rasrgele sayılar üretmemizi sağlar.

#%%      ---  random()  ---(fonksiyon)

# bununla 0.0 ile 1.0 arasında rastgele kayan noktalı sayı üretebiliriz.

import random
random.random()

#%%     ---  uniform()  ---

# belirli aralıkta rastgele kayan noktalı sayı üretebiliriz.

random.uniform(1,11)

#%%       ---  randint() ---

# belirli aralıklarda reastgele tam sayı üretmemizi sağlar.

random.randint(1,11)

#%%       ---  choice()  ---

# dizi niteliği taşıyan veri tiplerinden rastgele ögeler seçebiliriz.

liste = ["serhat","serdar","serap","ezgi","murat","nimet","hikmet"]
random.choice(liste)

#%%      ---  shuffle()  ---

# dizi niteliği taşıyan veri tiplerindeki ögeleri karıştırabiliriz.

l = list(range(10))
random.shuffle(l)
print(l)

#%%     ---  randrange()  ---

# belirli aralıklarda tam sayı üretmemizi sağlar.

random.randrange(1,10)
# 1 ile 10 içinde değildir.
# ama randint()'te 1 ile 10 içinde olur.

#%%              ----  datetime Modülü  ----

# zaman,saat ve tarihlerle ilgili işlem yapmamızı sağlar.
# 3 sınıftan oluşur.||datetime||time||date
# date||tarihle ilgili işlemler yapmamızı sağlar.
# time||zamanla ilgili işlemler yapmamızı sağlar.
# datetime||time ve date birleşimi ve +fonk. ve nitelikler.

#%%       ---  now() --(datetime sınıfı)--

# bize içindeki bulunduğumuuz andaki saat,tarih ve zaman bilgilerini verir.

import datetime

an = datetime.datetime.now()
# bu fonk. datetime.datetime adlı özel bir sınıf nesnesi verir.
print(an)
an.year
an.month
an.day
an.hour
an.minute
an.second
an.microsecond

#%%     ---  today() --(datetime sınıfı)--

# yularıdaki now() ile aynıdır.

#%%    ---  ctime() --(datetime sınıfı)--

# içinde bulunduğumuz ana ilişkin saat,tarih,zaman ile ilgili okunaklı 
# karakter dizisi verir.

# bu fonk. parametre olarak datetime.datetime özel sınıfını vermemiz lazım.

an = datetime.datetime.now()
tarih = datetime.datetime.ctime(an)
print(tarih)
# Sun Apr 12 21:21:05 2020     çıktısı verdi.

#%%     ---  strftime() --(datetime sınıfı)

# tarih ve zaman bilgilerini ihtiyaçlarımız doğrultusunda biçimlendirmemizi sağlar.

import datetime

an = datetime.datetime.now()
tarih = datetime.datetime.strftime(an,'%c')
print(tarih)

datetime.datetime.strftime(an,'%Y')# YIL
datetime.datetime.strftime(an,'%X')# SAAT
datetime.datetime.strftime(an,'%d')# GÜN
datetime.datetime.strftime(an,'%A')# GÜN(yazılı)
datetime.datetime.strftime(an,'%B')# AY(yazılı)
datetime.datetime.strftime(an,'%m')# AY

#%%      ---  strptime() --(datetime sınıfı)--

# elimizde şöyle bir karakter dizisi var.
t = '24 Temmuz 1996'
# bunu gün ay yıl olarak ayırmak istiyoruz.
gün,ay,yıl = t.split()
print(gün)
print(ay)
print(yıl)
# ama şöyle bir sey olursa ne yapıcaz.
a = '24 Temmuz 1996 saat 11:11:11'

z = datetime.datetime.strptime(a,'%d %B %Y saat %H:%M:%S')

#%%     ---  fromtimestamp() --(datetime sınıf)--

# bir zaman damgasını anlamlı bir tarih bilgisine dönüştürmek için kullanılır.

import os

zamanDamgası = os.stat("asker.py").st_mtime 
tarih = datetime.datetime.fromtimestamp(zamanDamgası)
print(tarih)
# bu şekilde artık datetime.datetime nesnesi elde ettikten sonra istediğimiz gibi değiştirebilriz.
datetime.datetime.strftime(tarih,'%c')

#%%    ---  timestamp() --(date sınıfı)--

# datetime.datetime nesnelerinden bir zaman damgası oluşturmak için kullanılır.
tarih = datetime.datetime.now()
zamanDamgası = datetime.datetime.timestamp(tarih)
zamanDamgası

#%%               ---  Tarihlerle İlgili Aritmetik İşlemler  ---

#       ---  Belirli Bir Tarihi Kaydetmek  ---

# mesela eski bir tarihi datetime sınıfı olarak kadetmek istiyoruz.

import datetime

tarih = datetime.datetime(2016,7,24,11,30,15)

# #bu sınıf datetime.datetime nesnelerinin bütün özelliklerini taşır.
tarih.year
tarih.day

#%%    ---  İki Tarih Arasındaki Farkı Bulmak  ---

# bugünden itibaren önümüzdeki yıl doğum günüme ne kadar kaldı.

bugün = datetime.datetime.today()
doğum = datetime.datetime(2021,7,24)
fark = doğum - bugün
fark # datetime.timedelta(days=465, seconds=38373, microseconds=957070)  çıktısı.

fark.days
fark.seconds
fark.microseconds

#%%     ---  İleri Bir Tarih Bulmak  ---

# mesela 200 gün sonra hangi tarihte olacağımızı bulmak istiyoruz.

bugün = datetime.datetime.today()
fark = datetime.timedelta(days=200)
gelecek = bugün + fark
gelecek
# tarihi anlamlı bir karakter dizisine dönüştürelim.
gelecek.strftime('%c') #  'Fri Sep 27 14:27:34 2019'   çıktısı verdi.

#%%     ---  Geçmiş Bir Tarihi Bulmak  ---

# mesela 200 gün önceki tarihi bulmak istiyoruz.

bugün = datetime.datetime.today()
fark = datetime.timedelta(days=200)
gecmis = bugün - fark
gecmis
# tarihi anlamlı bir karakter dizisine dönüştürelim.
gecmis.strftime('%c')


#%%                  ----  time Modülü  ----

# daha çok saatle ilgili işlemler yapmak için kullanılır.

import time

#%%       ---  gmtime()  ---

# Programlama dillerinde 'zamanın başlangıcı'(EPOCH) diye bir kavram vardır.

# kullandığımız işleitm sisteminin hangi tarihi 'zamanın başlangıcı' olarak 
# kabul ettiğini bulmak için kullanılır.

time.gmtime(0)
epoch = time.gmtime(0)
epoch.tm_mon

#%%     ---  time()  ---

# zamanın başlangıcından şu ana kadar geçen toplam saniye miktarını verir.

time.time()

#%%    ---  localtime()  ---

# anlık tarih ve zaman bilgisini verir.

time.localtime()

#%%    ---  asctime()  ---

time.asctime(time.localtime())

#%%    ---  strftime()  ---

# tarih-saat bilgisi içieren karakter dizilerini manipüle edebilmemizi sağlar.

time.strftime('%c')

#%%    ---  strptime()  ---

t = '27 Mayıs 1980'
tarih = time.strptime(t,'%d %B %Y')
tarih

#%%    ---  sleep()  ---

# bu fonksiyonla kodlarımızın işleyişini belli sürelerle kesintiye uğratabiliriz.
for i in range(10):
    time.sleep(1)
    print(i)
# 1 saniye aralıklarla sayıları yazdıracak.Saniyeyi değiştirebliriz.










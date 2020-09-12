# -*- coding: utf-8 -*-
#                             -----  Squlite İLE VERİTABANI PROGRAMLAMA  -----
#                                        * (Database Programming) *

#          ---  Yeni Bir Veritabanı Oluşturmak  ----

#import sqlite3
#vt = sqlite3.connect("veritabanı_adı")
#vt = sqlite3.connect("deneme.sqlite")
# eğer yazdığımız isimde bir veritabanı yoksa bu ada sahip bir veritabanı oluşturulacak.
# tabi isteseydik bağlanmak için tam dosya yolu da verebilirdik.
#vt = sqlite3.connect(r"C:/users/serhat/aef/deneme.sqlite") 

# bu komutlarla sabit disk üzerinde Sqlite veritabanı dosyası oluşturmuş oluyoruz.
# istersekgeçici veriyabanı da oluşturabiliriz.
#vt = sqlite3.connect(":memory:")
# oluşturduğumuz geçici veritabanı sabit disk üzerinde değil RAM üzerinde çalışır.
# veritabanını kapattığımız anda bu geçici veritabanı silinir.

# eğer istersek RAM üzerinde değil de sabit disk üzerinde de geçici veritabanı oluşturabiliriz.
# bunun içinde şöyle bir komut girebiliriz.
#vt = sqlite3.connect("")
# "" boş karakter dizisi kullandık.

#%%     ---  Varolan Bir Veritabanı İle Bağlantı Kurmak  ---

#import sqlite3
#
#vt = sqlite3.connect("chinook.db")

#%%                ---  İmleç Oluşturma  ---

# veritabanı üzerinde işlem yapabilmek için imleç oluşturmamız gerek.
# imleç oluşturmak için cursor() adlı bir metottan faydalanıcaz.

#im = vt.cursor()

# imleci oluşturduktan sonra önümüz iyice açılıyor.böylece oluşturduğumuz im 
# nesnesinin execute() metodunu kullanarak SQL komutlarını çalıştırabilicez.

#%%               ---  Tablo Oluşturma  ---
# modülü içe aktaralım.
import sqlite3
# yeni bir veritabanı dosyası oluşturalım.
vt = sqlite3.connect(r"C:\Users\hp\Desktop\SqliteCreate\veritabani.sqlite")
# veritabanında işlem yapabilmek için imlecimizi oluşturalım.
im = vt.cursor()
# oluşturduğumuz imlecin execute() metodu ile veritabanı içinde tablo oluşturalım.
im.execute("CREATE TABLE adres_defteri (isim,soyisim)")

# burada yaptığımız 'adres_defteri' adlı bir tablo oluşturup,bu tabloya
# 'isim' ve 'soyisim' adlı iki sütun oluşturmak.

# CREATE TABLE bir SQL komutudur.
# eğer tablo adı ve sütun başlıklarında birden fazla kelimeden oluşan 
# etiketler kullanacaksak bunları ya birbirine bitiştirip yazalım ya da
# tırnak içine alalım.

# bu arada bu kodları ikinci kez çalıştırdığımızda bir hata mesajı alırız.
# OperationalError: table adres_defteri already exists -------------
# hata mesajı budur.
#%%            ---  Şartlı Tablo Oluşturma  ----

# yukarıda kodları ikinci kez çalıştırdığımızda hata mesajı aldık.
# burdaki sorun 'veritabani.sqlite' dosyasının içinde 'adres_defteri' adlı
# tablonun zaten bulunuyor olmasıdır.
# bir veritabanı üzerinde aynı ada sahip iki tane tablo oluşturamayız.
# bu hatayı önlemek için kullanacağımız bir SQL komutu vardır.
# CREATE TABLE IF NOT  EXISTS
# Örneğimizi buna göre tekrar yazalım.

import sqlite3

vt = sqlite3.connect(r"C:\Users\hp\Desktop\SqliteCreate\vt.sqlite")

im = vt.cursor()

sorgu = "CREATE TABLE IF NOT EXISTS personel (isim,soyisim,memleket)"

im.execute(sorgu)

# bu kodları istediğimiz kadar çalıştıralım hata vermez.
# eğer veritabanında 'adres_defteri' adlı tablo yoksa oluşturur, varsa da
# sesini çıkarmadan yoluna devam eder.

#%%           ---  Tabloya Veri Girme  ---

import sqlite3

vt = sqlite3.connect(r"C:\Users\hp\Desktop\SqliteCreate\vt.sqlite")
im = vt.cursor()
tabloYap = """CREATE TABLE IF NOT EXISTS personel (isim,soyisim,memleket)"""
degerGir = """INSERT INTO personel VALUES ('Serhat','Çağlar','BİLECİK')"""

im.execute(tabloYap)
im.execute(degerGir)

# INSERT INTO içine yerleştir demek.

#%%            ---  Verilerin Veritabanına İşlenmesi  ---

# girdiğimiz verileri veritabanına işlemek için commit() metodundan yararlanıcaz.

import sqlite3

vt = sqlite3.connect(r"C:\Users\hp\Desktop\SqliteCreate\vt.sqlite")
im = vt.cursor()
tabloYap = """CREATE TABLE IF NOT EXISTS personel ('isim','soyisim','memleket')"""
degerGir = """INSERT INTO personel VALUES ('Serhat','Çağlar','BİLECİK')"""

im.execute(tabloYap)
im.execute(degerGir)

vt.commit() # tablonun içini bu metot sayesinde doldurduk.
vt.close() # veritabanını bu metot sayesinde kapattık.

#%% eğer veritabanımızın otomatik olarak kapanmasını garantilemek istiyorsak
# 'with' sözcüğünü kullanabiliriz. 
import sqlite3

with sqlite3.connect(r"C:\Users\hp\Desktop\SqliteCreate\vt.sqlite") as vt:
    im = vt.cursor()
    tabloYap = """CREATE TABLE IF NOT EXISTS personel ('isim','soyisim','memleket')"""
    degerGir = """INSERT INTO personel VALUES ('Serhat','Çağlar','BİLECİK')"""

    im.execute(tabloYap)
    im.execute(degerGir)

    vt.commit() # tablonun içini bu metot sayesinde doldurduk.
  
# bu şekilde with sözcüğünü kullanarak bir veritabanı bağlantısı açtığımızda
# bütün işler bittikten sonra Python bizim için bağlantıyı sonlandırır.

#%%             ---  Parametreli Sorgular  ---
    
# şun ana kadarki örneklerde veritabanına girilecek verileri tek tek elle giriyorduk.

# ancak çoğu durumda veritabanına girilecek veriler harici kaynaklardan gelir.

import sqlite3

with sqlite3.connect(r"C:\Users\hp\Desktop\SqliteCreate\vt.sqlite") as vt:
    im = vt.cursor()
    
    veriler = [("Serdar","Çağlar","BİLECİK"),
               ("Ahmet","Çağlar","BİLLECİK"),
               ("Nimet","Çağlar","BİLECİK"),
               ("Ezgi","Çağlar","BİLECİK")]
    im.execute("""CREATE TABLE IF NOT EXISTS personel ('isim','soyisim','memleket')""")
    for veri in veriler:
        im.execute("""INSERT INTO personel VALUES (?,?,?)""",veri)
        
    vt.commit()
    
#%%           ---  Tablodaki Verileri Seçmek  ---
import sqlite3

vt = sqlite3.connect("vt.sqlite")
im = vt.cursor()

im.execute("""CREATE TABLE IF NOT EXISTS faturalar ('fatura','miktar',
                'ilk_ödeme_tarihi','son_ödeme_tarihi') """) 
im.execute("""INSERT INTO faturalar VALUES ('Elektrik',45,'23 Ocak 2020','30 Ocak 2020')""")   
    
vt.commit()    

# şimdi veritabanından nasıl veri alacağımıza bakalım.

im.execute("""SELECT * FROM faturalar""")    
# faturalar adlı tablodaki bütün ögeleri seç dedik.     
# '*' hepsini anlamına gelir.  
    
#%%                   ---  Seçilen Verileri Almak  ---

#         ---  fetchall() Metodu  ---   

# yukarıdaki programa şu komutu ekleyelim.   
#veriler = im.fetchall()
# fetchall() metoduyla aldığımız bütün verileri, veriler adlı değişkene atadık.
#print(veriler)    
# şimdi de çıktısını alabiliriz.    
    
# eğer veritabanı dosyasına verilerin sadece bir kez yazılmasını istiyorsak ne yapıcaz.   
# bunu şöyle halledicez.

import sqlite3,os

dosya = "vt.sqlite"
dosyaMevcut = os.path.exists(dosya)
# burada böyle bir veritabanı olup olmadığını kontrol ettik.
vt = sqlite3.connect(dosya)
im = vt.cursor()

im.execute("""CREATE TABLE IF NOT EXISTS faturalar ('fatura','miktar',
'ilk_ödeme_tarihi','son_ödeme_tarihi') """) 

if not dosyaMevcut:
    im.execute("""INSERT INTO faturalar VALUES ('Elektrik',45,
                '23 Ocak 2020','30 Ocak 2020')""")
    vt.commit()

im.execute("""SELECT * FROM faturalar""")  

veriler = im.fetchall()
print(veriler) #  [('Elektrik', 45, '23 Ocak 2020', '30 Ocak 2020')] 

#%% veri tabanındaki tabloların adını öğrenmek için
import sqlite3
vt = sqlite3.connect("vt.sqlite")
im = vt.cursor()
im.execute("SELECT name FROM sqlite_master")
im.fetchall() # [('personel',), ('faturalar',)]  çıktısı verdi.

#%%           ---  fetchone() Metodu  ---

# bir veritabanında seçilen verilerin tek tek alınmasını sağlar.

import sqlite3

vt = sqlite3.connect("vt.sqlite")
im = vt.cursor()
im.execute("SELECT * FROM personel")# tablodan bütün verileri seçtik.
im.fetchone()# şimdi tek tek alıyoruz.bu ilk satır.
im.fetchone()# bu ikinci satır.

#%%          ---  fetchmany() Metodu  ---

# bu emtot bir veritabanında seçtiğimiz verilerin istediğimiz kadarını alabilmemizi sağlar.
import sqlite3

vt = sqlite3.connect("vt.sqlite")
im = vt.cursor()
im.execute("SELECT * FROM personel")
im.fetchmany(3)# tabloda 3 satırı göstermesini istedik.

#%%            ---  Veri Süzme  ---

# im.execute("SELECT * FROM personel WHERE isim = 'Serhat'")

# burada SQL'in WHERE komutunu kullandık.
# 'personel' tablosunun 'isim' sütununda 'Serhat' bulunan bütün kayıtları seçiyoruz. 

#%%         ---  Veritabanı Güvenliği  ---

# içe aktardık.
import sqlite3 
# veritabanına bağlandık.
db = sqlite3.connect("vt.sqlite")
# veritabanında işlemler yapmak için imleç oluşturduk.
im = db.cursor()
# kullanicilar adlı tablo oluştrup iki sütun ekledik.
im.execute("""CREATE TABLE IF NOT EXISTS kullanicilar (kullanici_adi,parola)""")
# tabloya yerleştirdiğimiz verileri hazırladık.
veriler = [("ahmet123","1234567"),
           ("mehmet321","7654321"),
           ("selin456","1231230")]
# 'veriler' içindeki bütün verileri tabloya yerleştiriyoruz.tek ögeli demet tanımladık:%(i,)
for i in veriler:
    im.execute("""INSERT INTO kullanicilar VALUES %s"""%(i,))
# yapılan değişikliklerin tabloya işlenmesi için commit() uyguladık.    
db.commit()
# kullanıcıdan username ve password bilgilerini alıyoruz.
kull = input("Kullanıcı Adı :")
paro = input("Parola :")
# bu komutla da iki sütundaki bilgileri seçiyoruz.
im.execute("""SELECT * FROM kullanicilar WHERE kullanici_adi = '%s'
           AND parola = '%s'"""%(kull,paro))
# verileri tek tek alıp data değişkenine atadık.
data = im.fetchone()
# eğer data True ise hosgeldin değil ise parola kullanıcı yanlış.
if data:
    print("\nHoşgeldin.{}.".format(data[0]))
else:
    print("\nParola veya kullanıcı adı yanlış.")

# şimdi burada sistemin zaaflarından yararlanarak içeri girecez.
# kullanıcı adı ve parolaya bunu yazalım.

# x' OR '1' = '1
    
# hatta şunu girip parolayı boş bıraksak bile olur.

# x' OR '1' = '1' --

# işte bu işlmelere SQL Sızdırma(injection) denir.

# gelelim bu sızdırmanın olduğu komuta.

#im.execute("""SELECT * FROM kullanicilar WHERE kullanici_adi = 'x' or '1' = '1'
#           AND parola = 'x' or '1' = '1'"""%(kull,paro))

# böyle daha iyi anlaşıldı.
    
#(kullanici_adi == 'x' or '1' == '1') and (parola == 'x' or '1' == '1')

# burası True çıktısı verir.

# Python'da yazdığımız kodlara örnek eklemek için '#' kullanırız,
# SQL komutlarına yorum yazmak için de '-' kullanılır.

#%% bu olayı önlemek için '%s' yerine '?' koymalıyız aşağıda gösterelim.

# içe aktardık.
import sqlite3 
# veritabanına bağlandık.
db = sqlite3.connect("vt.sqlite")
# veritabanında işlemler yapmak için imleç oluşturduk.
im = db.cursor()
# kullanicilar adlı tablo oluştrup iki sütun ekledik.
im.execute("""CREATE TABLE IF NOT EXISTS kullanicilar (kullanici_adi,parola)""")
# tabloya yerleştirdiğimiz verileri hazırladık.
veriler = [("ahmet123","1234567"),
           ("mehmet321","7654321"),
           ("selin456","1231230")]
# 'veriler' içindeki bütün verileri tabloya yerleştiriyoruz.tek ögeli demet tanımladık:%(i,)
for i in veriler:
    im.execute("""INSERT INTO kullanicilar VALUES (?,?)""",i)
# yapılan değişikliklerin tabloya işlenmesi için commit() uyguladık.    
db.commit()
# kullanıcıdan username ve password bilgilerini alıyoruz.
kull = input("Kullanıcı Adı :")
paro = input("Parola :")
# bu komutla da iki sütundaki bilgileri seçiyoruz.
im.execute("""SELECT * FROM kullanicilar WHERE kullanici_adi = ?
           AND parola = ?"""%(kull,paro))
# verileri tek tek alıp data değişkenine atadık.
data = im.fetchone()
# eğer data True ise hosgeldin değil ise parola kullanıcı yanlış.
if data:
    print("\nHoşgeldin.{}.".format(data[0]))
else:
    print("\nParola veya kullanıcı adı yanlış.")


    















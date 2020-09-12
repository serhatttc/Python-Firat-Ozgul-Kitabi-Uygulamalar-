# -*- coding: utf-8 -*-
#                         --------SÖZLÜKLER-(DİCTİONARY)--------                                  

kelimeler = {"kitap":"book"}
print(type(kelimeler))# <class 'dict'> çıktısı verdi.
print(len(kelimeler))# 1 çıktısını verdi yani içinde 1 öge var.

dictionary = {"bilgisayar":"computer",
          "masa"      :"table" ,
          "programlama":"programming"}
print(len(dictionary))

#%%                    Sözlük Ögelerine Erişmek

dictionary = {"bilgisayar":"computer",
          "masa"      :"table" ,
          "programlama":"programming"}

print(dictionary["Bilgisayar".lower()])# computer çıktısı aldık.

# sözlükte yuarıdan örnek verelim ||bilgisayar = keyword.||.computer = value||
# tek tek yazıp çıktı almaya gerek yok for döngüsü kullanalım.
for i in dictionary:
    print(dictionary[i])

#%%
telefonRehberi = {"ahmet öz":"111111111",
                  "mehmet kaz":"2222222",
                  "ali çok":"33333333",
                  "veli az":"4444444"}    
kisi = input("numara öğrenmek için isim giriniz : ")

if kisi in telefonRehberi:
    cevap="{} kişisinin numarası :{}"
    print(cevap.format(kisi,telefonRehberi[kisi]))
else:
    print("böyle bir kişi rehberde yok.")
    
#%%                    Sözlüklerin Yapısı
    
kisiler = {"serhat çağlar":{"memleket":"bilecik",
                              "yaş"   :   23,
                            "meslek"  :"öğrenci"},
           "serdar çağlar":{"memleket":"bilecik",
                              "yaş"   :   32,
                            "meslek"  :"muhasebeci"}}
    
print(kisiler["serhat çağlar"]["yaş"])    
print(kisiler["serdar çağlar"]["memleket"])   
    
# sözlük içinde sözlük yaptığımız gibi liste de yapabiliriz.   
    
#%%                  Sözlüklere Öge Eklemek    
sozluk = {}
sozluk["ahmet"] = "çağlar"# keyword ahmet,value çağlar olan bir öge ekledik.
print(sozluk)
sozluk["serhat"] = "çağlar"
sozluk["serdar"] = "çağlar"
sozluk["nimet"] = "çağlar"
print(sozluk)

# sözlüklere keyword olarak demet,sayı,karakter dizisi ekleyebiliriz.
# ama liste ve sözlük ekleyemeyiz. value olarak hepsini ekleyebiliriz.

#%%                  Sözlük Ögeleri Üzerinde Değişilik Yapmak
sozluk = {'ahmet': 'çağlar', 'serhat': 'çağlar',
          'serdar': 'çağlar', 'nimet': 'çağlar'}
print(sozluk)
sozluk["serdar"] = "ezgi" # çağlar olan değeri ezgi olarak değiştirdik.
print(sozluk)

#%%                Sözlük Üreteçleri(Dictionary Comprehensions)

isimler = ["serhat","serdar","ahmet","nimet","ezgi"]
# amacımız bu isimleri ve herbir ismin kaç harften oluştuğunu gösteren sözlük yapmak.
sozluk = {i: len(i) for i in isimler}
print(sozluk)

#%%                       Sözlüklerin Metotları

#                keys()

# bir sözlüğün sadece anahtarlarını (keywords) almak için kullanılır.
sozluk = {'ahmet': 'çağlar', 'serhat': 'çağlar',
          'serdar': 'çağlar', 'nimet': 'çağlar'}

print(sozluk.keys())# dict_keys(['ahmet', 'serhat', 'serdar', 'nimet']) çıktısı.
# bu çıktıyı liste,demet,kardiz. dönüştürebiliriz.
#%%             values()
sozluk = {'ahmet': 'çağlar', 'serhat': 'çağlar',
          'serdar': 'çağlar', 'nimet': 'çağlar'} 
print(sozluk.values())# dict_values(['çağlar', 'çağlar', 'çağlar', 'çağlar'])
# sadece values (değerleri) verir.
# bu çıktıyı liste,demet,kardiz. dönüştürebiliriz.

#%%             items()   
sozluk = {'ahmet': 'çağlar', 'serhat': 'çağlar',
          'serdar': 'çağlar', 'nimet': 'çağlar'} 

print(sozluk.items())
# dict_items([('ahmet', 'çağlar'), ('serhat', 'çağlar'),
# ('serdar', 'çağlar'), ('nimet', 'çağlar')])

# bir liste içinde iki ögeli demetler halinde bir çıktı verdi.
for anahtar,değer in sozluk.items():
    print("{} = {}".format(anahtar,değer))
# bu şekilde de sıralayabiliriz.
    
#%%             get()
sozluk = {"dil":"language","bilgisayar":"computer",
          "kitap":"book","defter":"notebook"}    
sorgu = input("anlamını öğrenmek istediğiniz kelime : ")

if sorgu not in sozluk:
   print("bu kelime veritebanımızda yoktur.")
else:
    print(sozluk[sorgu])

#%% yukarıda yaptığımız olayın kolay yolu get() ile yapılır.
sozluk = {"dil":"language","bilgisayar":"computer",
          "kitap":"book","defter":"notebook"}    
sorgu = input("anlamını öğrenmek istediğiniz kelime : ")

print(sozluk.get(sorgu,"bu kelime veritebanımızda yoktur."))

#%%             clear()
# sözlüğü boşaltmamızı sağlar.
sozluk = {"dil":"language","bilgisayar":"computer",
          "kitap":"book","defter":"notebook"}  
print(sozluk)
sozluk.clear()
print(sozluk)# {} çıktısı yani boş.

#%%            copy()
havaDurumu = {"bilecik":"sisli","eskişehir":"yağmurlu",
              "bursa":"bulutlu"}
yedekHavaDurumu = havaDurumu.copy() # kopyalama işlemi yaptık.
# şimdi havaDurumu sözlüğüne öge ekleyelim.
havaDurumu["afyon"] = "karlı"
print(havaDurumu) # yaptığımız ekleme kopyaladığımızı etkilemedi.
print(yedekHavaDurumu)

#%%              fromkeys()
elemanlar = "ahmet","mehmet","can"
adresler = dict.fromkeys(elemanlar,"kadıkoy")
print(adresler)
# bu metotla "ahmet","mehmet","can" anahtar kelimeler oldu "kadıkoy" ise
# değer kelimemiz oldu. hepsine tek tek "kadıkoy" atadık.

#%%              pop()
# bu metot listede de var yaptığı iş öge silip onu ekrana basar.
# listede sırasını belirleyipte silebiliyoruz ama sözlükte mutlaka ögeyi belirtmeliyiz.
sozluk = {"dil":"language","bilgisayar":"computer",
          "kitap":"book","defter":"notebook"}   
sozluk.pop("dil")# bu ögeyi sildik.
print(sozluk)
#print(sozluk.pop("araba"))# KeyError: 'araba'  hatası verdi.
# hatayı kendimiz düzenlemek için get() gibi kullanabiliriz.
print(sozluk.pop("araba","silinecek öge yok"))

#%%             popitem()
# ögeleri rastgele siler, sözlükler zaten sırasız veri tipleridir.
# () içinde parametre yer almaz.
sozluk = {"dil":"language","bilgisayar":"computer",
          "kitap":"book","defter":"notebook"}  
sozluk.popitem()# defter ögesini silmiş.
print(sozluk)

#%%              setdefault()
sepet = {"meyveler":("elma","armut"),"sebzeler":("pırasa","fasulye")}

sepet.setdefault("içecekler",("su","süt"))# bu ögeyi ekledik.
print(sepet)
sepet.setdefault("meyveler",("çilek","muz"))
print(sepet)
# setdefault() öge eklettirir.varolan ögeyi değiştirtmez.

#%%             update()
stok = {"elma":5,"armut":10,"peynir":6,"sosis":15}
yeniStok = {"elma":3,"armut":20,"peynir":8,"sosis":4,"sucuk":6}
# yapmamız gereken şey stoğumuzu yeni bilgilere göre güncellemektir.
# bu işlem update() ile yapılır.
stok.update(yeniStok)
print(stok)























   
    
    



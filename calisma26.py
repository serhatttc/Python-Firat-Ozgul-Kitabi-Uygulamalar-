# -*- coding: utf-8 -*-
#                                       ----  DÜZENLİ İFADELER  ----

#               ----  Düzenli İfadelerin Metotları  ----

# Python'da düzenli ifadelere ilişkin herşey bir modül de tutulur.
# bu modülün adı 're'.
#import re
#print(dir(re))
# şu komut ile de metot ve fonksiyon hakkında yardım alabiliriz.
# help(metot_veya_fonksiyonAdı)...örnek vermek gerekirse
#help(re.match)
# yardım bölümünden çıkmak için q tuşuna basmamız gerekir.

#%%          ----  match() Metodu  ----
import re

a = "Python güçlü bir programlama dilidir."
# diyelim ki biz bu karakter dizisi içinde 'Python' kelimesi geçip geçmediğini öğrenmek istiyoruz.
print(re.match("Python",a))# burada 'python' şeklinde düzenli ifade kalıbı oluşturduk.
# düzenli ifade kalıpları (parantez içindeki ilk değer)'dir.
# ikinci argüman ise 'a' hazırladığımız kalıbı kendisiyle eşleştireceğimiz karakter dizisidir.

# <re.Match object; span=(0, 6), match='Python'> ||| çıktısı verdi.
print(a[0:6])# span=(0,6) demek.
# Python'ı buldu eğer kelime olmasaydı None çıktısı verecekti.
a.split()[0] == "Python"
# match()'in yaptığı işlemi split()'de yapar.
# çünkü match() sadece karakter dizisinin başındaki  kelimeye bakar diğerlerini aramaz.
# aynı işi startswith() metoduylada yapabiliriz.
a.startswith("Python")
#%% 
import re
a = "serhat çağlar"
eşleşme = re.match("serhat",a)
eşleşme
# span değerine span adlı metottan da ulaşaniliriz.
eşleşme.span()#  (0,6) çıktısı verdi.

#%%        ----  search() Metodu  ----
import re
# match() metodu karakter dizisinin sadece başına bakıp eşleşme yapar.
# search() mettodu ise karakter dizisinin geneline bakıp arama işlemi yapar. 
# yani biri eşleştirir diğeri arar.
b = "Python güçlü bir dildir."
print(re.search("dildir",b))
# <re.Match object; span=(17, 23), match='dildir'>  || çıktısı verdi.
arama = re.search("dildir",b)
arama.span() # (17, 23)  || çıktısı . hangi aralıkta olduğunu gösterir.
arama.group()#  'dildir'  || çıktısı verdi. aranan şeyin ne olduğunu gösterir.

#%% gelin birazda listeler üzerinde örnekler yapalım.

liste = ["elma","armut","kebap"]
# re.search("elma",liste)
# bu hata verir çünkü düzenlü ifadeler karakter dizileri üzerinde işler.
# bu yüzden Python'a biraz yardımcı olmamız lazım.
for i in liste:
    nesne = re.search("kebap",i)
    if nesne:
        print(nesne.group())
        print(nesne.span())
    
#%%         ----  findall() Metodu  ----

metin = """ asdd asfsa lskdnavşl slkf laksf laksf Python asldf cd
           sadkamsd askdm asd Python asasd Python asdsa Python
           asafd Python kfmsklkm Python."""
           
print(re.findall("Python",metin))
# ['Python', 'Python', 'Python', 'Python', 'Python', 'Python']
# liste halinde bir çıktı veri

# bunu searc() metodu ile yapmak istersek.
liste = metin.split()
for i in liste:
    nesne = re.search("Python",i)
    if nesne:
        print(nesne.group())
    
#%%                  -----  Metakarakterler  -----    
import re
# mesela elimzide bir liste olsun.
liste = ["serhat","özkan","serdar","özhan","serap","özcan","murat"]
# şimdi bu listeden özkan,özhan,özcan kelimelerini ayıklayalım.
for i in liste:
    nesne = re.search("öz[chk]an",i)
    if nesne:
        print(nesne.group())
# bize bu kolaylığı sağlayan '[]' adlı metakarakterdir.


#%%     -----  '[]' Köşeli Parantez  ----
# yukarıdaki örnekte bunun neişe yaradığını gösterdik.
a = ["12asd1","b12ads2","45sa65s","es45as4d"]
# şimdi biz bu listede sayıyla başlayanları yıklayalım.
for i in a:
    if re.match("[0-9]",i):
        print(i)
# match() kullandık çünkü bu sadece karakter dizilerinin başına bakar.
print("-"*33)
for i in a:
    if re.match("[a-z][a-z][0-9]",i):
        print(i)
# burda bunu bulduk "es45as4d" ilk iki yazdığımız iki küçük harfi diğeri sayıyı temsil eder.

#%%          ---- '.' Nokta  ----

liste = ["esma","esra","serap","aysu"]
# '.' tek bir karakterin yerini tutar.        
for i in liste:
    nesne = re.match("es.a",i)
    if nesne:
        print(nesne.group())
# esma ve esra yı buldu .
#%% bu şekilde yazılabilirdi.
liste = ["esma","esra","serap","aysu"]
for i in liste:
    if re.match("es.a",i):
        print(i)
#%% bir örnek daha verelim.

a = ["12345","AV12W","15SDF7","E14E6","1agA5"]

for i in a:
    if re.match(".[0-9a-z]",i):
        print(i)
# bu demek ki aradığımız karakter dizisi ilk karakteri önemli değil istediğiyle
# başlayabiliri ama ardından ya sayı ile ya da küçük harf ile devam edecek diyoruz.
        
#%%         ----  '*' Yıldız  ----        
        
yeniListe = ["st","sat","saat","saaat","falanca"]        
# yıldız sembolü kendinden önce gelen 'a' karakterini sıfır veya daha fazla sayıda eşleştiriyor.         
for i in yeniListe:
    if re.match("sa*t",i):
        print(i)        
# mesela 'st' içinde 0 'a' karakteri var bunu eşleştiriyor.
# diğerlerinde de 'a' var ve onlarıda eşleştiriyor.        
#%%
a = ["ahmet","serhat","mehmet","serap"]
for i in a:
    if re.match(".*met",i):
        print(i)
# bunu yukarıda sadece '.' ile yapamamıştık.şimdi oldu.      
#%%
# yukarıda bir şey daha hata vermişti sadece match() ile yapamamıştık.

a = "python güçlü bir dildir."
print(re.match("güçlü",a)) # None değeri vermişti.
print(re.match(".*güçlü",a)) # şimdi istediğimizi verdi.    
        
#%%          ----  '+' Artı  ---- 
import re
a = ["ahmet","serhat","met","mehmet","serap"]
for i in a:
    if re.match(".*met",i):
        print(i)
# burda 'met' ögesini de alır ama biz bunu almak istemiyoruz.
print("-"*33)
for i in a:
    if re.match(".+met",i):
        print(i)        
# işte '+' ile bunu çözdük.
#%%
yeniListe = ["st","sat","saat","saaat","falanca"]        
# yıldız sembolü kendinden önce gelen 'a' karakterini sıfır veya daha fazla sayıda eşleştiriyor.         
for i in yeniListe:
    if re.match("sa*t",i):
        print(i)  
# burda 'st' ögesini de alıyor ama biz 'a' en az 1 tane olan ögeleri istiyoruz.
print("-"*33)        
for i in yeniListe:
    if re.match("sa+t",i):
        print(i) 

#%%         ----  '?' Soru İşareti  ----

# '*' karakteri sıfır ya da daha fazla eşleşmeleri,'+' bir veya daha fazla 
# eşleşmeleri '?' ise sıfır veya bir tane olan eşleşmeleri yapar.
yeniListe = ["st","sat","saat","saaat","falanca"]        
        
for i in yeniListe:
    if re.match("sa?t",i):
        print(i)          
# mesela bir metinde ki uluslararası kelimesini arayacağız ama metinin içine 
# uluslar arası diye de geçiyor.bunu yapmak için
# if re.match("[Uu]luslar ?arası",metin)
# yaparak ayarladık burda 'boşluk' sıfır ya da bir tane olsa da eşleştir dedik.
#%%         ----  '{}' Küme Parantezi  ----

# '{}' adlı metakarakterimiz ile bir eşleşmeden kaç adet istediğimizi belirtebiliyoruz.
yeniListe = ["st","sat","saat","saaat","falanca"]        
        
for i in yeniListe:
    if re.match("sa{3}t",i):
        print(i) 
# burda 'a' karakterinin 3 kez tekrar etmesini istediğimizi belirttik.
print("-"*33)
for i in yeniListe:
    if re.match("sa{0,3}t",i):
        print(i) 
# burda da en az ve en çok kaç kez tekrar etmesini istediğimizi belirttik.

#%%        ----  '^' Şapka  ----
a = ["12345","AV12W","15SDF7","E14E6","1agA5"]

for i in a:
    nesne = re.search("[A-Z]+[0-9]",i)
    if nesne:
        print(nesne.group())
print("-"*33)
# burda sadece istediğimiz bölümleri kesip verdi.
for i in a:
    if re.search("[A-Z]+[0-9]",i):
        print(i)
# burada istediğimiz durumun bulunduğu ögeleri kesmeden verdi.
# üstteki kod bize daha ayrıntılı bir çıktı verdi.
print("-"*33)
for i in a:
    nesne = re.search("^[A-Z]+[0-9]",i)
    if nesne:
        print(nesne.group())
# bunu yaparak karakter dizilerinin sadece en başına bak dedik.match() gibi.
# burda da sadece en başını kesip attı önümüze.
# eğer ögelerin devamını da istiyorsak aşağıdakini yapıcaz.
print("-"*33)
for i in a:
    nesne = re.search("^[A-Z]+[0-9].*",i)
    if nesne:
        print(nesne.group())        
# burda sadece başına bak uyanları eşleştir ama kesip atma devamını da yaz dedik.      
#%% '^' başka bir görevi de 'hariç' anlamına gelmesi ama '[]' içinde kullanılır.
a = ["12345","AV12W","15SDF7","E14E6","1agA5"]
for i in a:
    nesne = re.match("^[A-Z0-9][^a-z]+",i)
    if nesne:
        print(nesne.group())         
# aradığımız öge bir sayı veya büyük harf ile başlamalı.
# en baştaki sayı veya büyük harften sonra küçük harf GELMEMELİ dedik.'^' ile yaptık.
# üstelik bu küçük harf gelmeme durumu bir veya daha fazla sayıda tekrar etmeli.'+' ile yaptık.

#%%         ----  '$' Dolar  ----
# bu işaret karakter dizilerinin nasıl biteceğini belirliyor.
# '^' işareti de nasıl başlayacağını belirliyordu.       
a = ["ahmet","serhat","met","mehmet","serap","mehtap"]
for i in a:
    if re.search("ap$",i):
        print(i)
#%%       ----  '\' Ters Bölü  ----
liste = ["10$","20$","20€","50TL"]
# DOLARLI ögeleri ayıklamaya çalışıcaz peki napıcaz.
for i in liste:
    if re.search("[0-9]+$",i):
        print(i)
# Python bizim sayıyla biten bir karakter dizisi aradığımızı zannedecek.
# ve çıktı vermicek.Bunu düzeltmek için şöyle yapıcaz.
for i in liste:
    if re.search("[0-9]+\$",i):
        print(i)
# ve istediğimize ulaştık.

#%%     ----  '|' Dik Çizgi  ----

# birden fazla düzenli ifade kalıbını birlikte eşleştirmemizi sağlar.
liste = ["at","katkı","fakat","atkı","rahat","mat","yat",
         "sat","satılık","katılım"]

for i in liste:
    if re.search("^at|at$",i):
        print(i)
# burda at ile başlayan veya at ile biten ögeleri ayırdık.

#%%     ----  '()' Parantez  ----  ---------SAYFA---808-----

#%%            ----  Eşleşme Nesnelerinin Metotları  ----

#        ----  group() Metodu  ----
        
# bu metot düzenli ifadeleri kullanarak eşleştirdiğimiz karakter dizilerini
# görmemizi sağlar.
import re
kardiz = "Python bir programlama dilidir"
nesne = re.search("(Python) (bir) (programlama) (dilidir)",kardiz)
print(nesne.group())
# şimdi bu grupladığımız bölümlere tek tek erişelim.
nesne.group(0)# 0 indeksi eşleşen karakter dizisinin hepsini veriyor.
nesne.group(1)# burda grubun 1 numaralı ögesi 'Python'u aldık.
dir(nesne)# kullanacağımız metotlar bunlar.

#%%        ----  groups() Metodu  ----

# bu metot bize kullanabileceğimiz bütün grupları demet halinde sunar.
nesne.groups()# ('Python', 'bir', 'programlama', 'dilidir') || çıktısı.

#%%                    ----  Özel Diziler  ----

#     ----  Boşluk Karakterinin Yerini Tutan Özel Dizi (\s) ----
a = ["5 ocak","27mart","4 ekim","nisan 3"]
for i in a:
    nesne = re.search("[0-9]\\s[A-Za-z]+",i)
    if nesne:
        print(nesne.group())
# burda bir sayı ile başlayan ardından bir adet boşluk karakteri içeren 
# sonra da bir büyük yada küçük harfle devam eden karakter dizilerinin ayıkladık.
        
#%%     ----  Ondalık Sayıların Yerini Tutan Özel Dizi (\d)  ----        
    
# bu sembol bir karakter dizisinde geçen ondalık sayıları eşlemek için kullanılır.
# buraya kadar '[0-9]' dan yararlanıyorduk.Şimdi '\d' bunu kullanıcaz.
a = ["5 ocak","27mart","4 ekim","nisan 3"]
for i in a:
    nesne = re.search("\d\s[A-Za-z]+",i)
    if nesne:
        print(nesne.group())
# aynı eşleşmeyi elde ettik.kısa yoldan.

#%%     ----  Alfanümerik Karakterlerin Yerini Tutan Özel Dizi (\w)  ----

# bu sembol bir karakter dizisi içindeki alfanümerik karakterleri ve '_' bulur.
a = "abc123_$%+"
nesne = re.search("\w*",a)
print(nesne.group())
#%%
# bir de '\s,\d,\w' dizilerinin büyük harfli olanları vardır.'\S,\D,\W'
# bunlar diğerlerinin yaptığı işin tam tersini yapar.

#%%              ----  Düzenli İfadelerin Derlenmesi  ----

#       ----  compile() Metodu  ----

# düzenli ifade kalıplarını kullanmadan önce compile() metodu ile derleyip
# daha hızlı çalışmalarını sağlayacağız.
liste = ["Python2.7","Python3.2","Python3.3","Python3.4","Java"]
derli = re.compile("[A-Za-z]+[0-9]\.[0-9]")
for i in liste:
    nesne = derli.search(i)
    if nesne:
        print(nesne.group())

#%%            ----  compile() ile Derleme Seçenekleri  ----

# bu bölümde 'compile()' işlemi sırasında kullanılabilecek seçenekleri anlatıcaz.

#%%     ----  re.IGNORECASE veya re.I

# büyük ve küçük harfe dikkat etmeden arama işlemini yapar.
import re

metin = """Programlama asdas asd asdaf fsd programlama Asf as
        asda asd Programlama asdasd asdasasd Adfgdf programlama"""
derli = re.compile("programlama",re.IGNORECASE)
print(derli.findall(metin))

#%%     ----  re.DOTALL veya re.S  ----

# '.' metakarakteri yeni satır karakterlerinin yerini tutmaz.
# bir örnek yapalım.
a = "Ben Python, \nMonty Python"
# Python kelimesini temel alarak bir arama yapmak istiyoruz.Şimdi yazacağımız
# istediğimiz şeyi yeterince vermez.
print(re.search("Python.*",a).group())
# bize sadece ilk satırdaki Python kelimesini verdi.
# ama bu şekil bir arama yaparsak.
derle = re.compile("Python.*",re.DOTALL)
nesne = derle.search(a)
if nesne:
    print(nesne.group())

#%%  -- Düzenli İfadelerle Metin/Karakter Dizisi Değiştirme İşlemleri --

#        ----  sub() Metodu  ---------SAYFA------817---

# düzenli ifadeler sadece karakter dizisini bulmakla ilgili değildir.
# aynı zamanda karakter dizisini değiştirmeyi de kapsar.
# şöyle kullanabiliriz.
a = """Kırmızı başlıklı kız, kırmızı elma dolu sepetiyle \
annenannesinin evine gidiyormuş!"""
derle = re.compile("kırmızı",re.IGNORECASE)
print(derle.sub("yeşil",a))
# burada kırmızı kelimesini yeşil olarak değiştirdik.

#%%     ----  subn() Metodu

# sub() metoduyla aynıdır, fakat sub()'dan farklı olarak kaç tane değişiklik yapıldığını gösterir.

#ab = derle.subn(değiştir,metin)
#print("toplam {} değişiklik yapılmıştır.".format(ab[1]))

# gibi yukardı yaptığımız yeri böyle değiştirebiliriz.





















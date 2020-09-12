# -*- coding: utf-8 -*-
#                              -------FONKSİYONLAR-------

# Görevi karmaşık işlemleri bir araya toplayarak bu işlemleri tek adımda yapmamızı sağlar.

#%%                 Fonksiyon Tanımlamak Ve Çağırmak
def kayitOlustur(isim,soyİsim,isSis,sehir):# fonksiyon tanımladık.
    print("-"*30)  # hangi işlemleri yapacağını buraya doldurduk.
                   # burada yazdıklarımız gövde olarak tanımlanır.
    print("isim             :",isim)
    print("soyisim          :",soyİsim)
    print("İşletim sistemi  :",isSis)
    print("Şehir            :",sehir)
    
    print("-"*30)

kayitOlustur("serhat","çağlar","ubuntu","bilecik")# fonksiyonu çağırdık.
kayitOlustur("serdar","çağlar","debian","bilecik")
kayitOlustur("ahmet","çağlar","mint","bilecik")
# print() ile kayitOlustur() aynı fonksiyonlar sadece birini Python oluşturdu birini biz.

#%%                      Fonsiyonların Yapısı
# bir fonksiyonu tanımlamak için 'def' adlı parçacıktan yararlandık.
def selamla():
    print("merhaba")
selamla()
# Python'da iki tip fonksiyon bulunur.1.Gömülü Fonksiyonlar(Builtin Functions),
# öteki ise özel fonksiyonlar(custom functions) bu kullanıcı tarafından üretilen fonk.

# ortada bir fonksiyon varsa tanımıda vardır.
#%%
def sistemBilgisi():
    import sys
    print("\nSistemde kurulu Python'ın;")
    print("\tana sürüm numarası   : ",sys.version_info.major)
    print("\talt sürüm numarası   : ",sys.version_info.minor)
    print("\tminik sürüm numarası : ",sys.version_info.micro)

    print("\nKullanılan işletim sisteminin;")
    print("\tAdı : ",sys.platform)

sistemBilgisi()
  
#%%                      Fonksiyonlar Ne İşe Yarar?
# Program içinde aynı şeyleri tekrar tekrar yazmamıza gerek bırakmaz.
def kareBul(sayi):
    cikti = "{} sayısının karesi : {}"
    print(cikti.format(sayi,sayi**(2)))
kareBul(11)
kareBul(22)
#%%   len() fonk. yerine bunu yapabiliriz.
def uzunluk(öge):
    c = 0
    for i in öge:
        c += 1
    print(c)
uzunluk("serhat")
uzunluk("serdar")
#%%                    Parametreler Ve Argümanlar
# Bir fonksiyonu tanımlarken tanımladığımız adlara parametre, aynı fonksiyonu 
# çağırırken belirlediğimiz adlara argüman denir.           
# yani yukarıdaki örnekte (öge)=parametre||("serhat")=argüman||

#%%               Sıralı (veya İsimsiz) Parametreler
# Veriliş sırası önem taşıyan parametrelerdir.
# def kayitOlustur(isim,soyİsim,isSis,sehir): bunun gibi.
# sırasına göre argüman girmezsek çıktı karışık gelir.

#%%                      İsimli Parametreler
# def kayitOlustur(isim,soyİsim,isSis,sehir):
# kayitOlustur(sehir="bilecik",isim="serhat",soyİsim="çağlar",isSis="ubuntu")
# böylece parametreleri istediğimiz sırada kullanabildik.

# Dikkat etememiz gereken konun ise isimli parametrenin ardından sıralı
# parametre gelmez.Hata verir.

#%%                    Varsayılan Değerli Parametreler
# biz bu şekilde kolayca yazıp çıktı alırız.
print("serhat","çağlar")
# ama aslında python bunu bu şekilde algılıyor.
import sys
print("serhat","çağlar",sep=" ",end="\n",file=sys.stdout,flush=False)
# yani biz görmesekte python sep,end,file,flush parametrelerini de içeriyor.
# biz bu parametreleri değiştirmeden en üstteki parametreyi yazarsak
# sep,end,file,flush parametrelerini bu şekil alacak buna varsayılan değerli parametre denir.
#%%    Bizde kendi varsayılan değerli parametrelerimizi yazabiliriz.
def kur(kurulumDizini="/usr/bin/"):
    print("Program {} dizinine kuruldu.".format(kurulumDizini))
# biz tanımladığımız fonk böyle çağırırsak.
kur()# Program /usr/bin/ dizinine kuruldu.|| çıktısı verecek.
# burda kur fonksiyonunun kurulumDizini adlı parametresi var ve varsayılan değeride
# "/usr/bin/" ' dir.
# biz bunu şöyle çağırırsak.
kur("/usr/serhat/")# Program /usr/serhat/ dizinine kuruldu.|| çıktısı verecek.

#%%               Rastgele Sayıda İsimsiz Parametre Belirleme
# sınırsız parametre alabilen fonksiyon üretmeye çalışalım.
def fonksiyon(*parametreler):
    print(parametreler)
fonksiyon(1,2,3,4)# (1, 2, 3, 4) || demet çıktısı verdi. 
#%%
def carp(*sayilar):
    sonuc = 1
    for i in sayilar:
        sonuc*=i
    print(sonuc)
carp(1,2,3,4)
# * koyarak istediğimiz kadar parametre girebiliriz demek istiyoruz.

# * işaretlerinin betimlediği parametreler 'args' olarak adlandırılır.

#%%              Rastgele Sayıda isimli Parametre Belirleme
def fonksiyon(**parametreler):
    print(parametreler)
fonksiyon(isim="serhat",soyİsim="çağlar",sehir="bilecik")
# {'isim': 'serhat', 'soyİsim': 'çağlar', 'sehir': 'bilecik'}
# boyle bir çıktı verir.bize bir sözlük olarak çıktı verdi.
#%%
def function(**bilgiler):
    print("-"*30)
    
    for anahtar,değer in bilgiler.items():
        print("{:<11}: {}".format(anahtar,değer))
# {:<11} burda <11 demek boşluk bırakmak demek. sola yaslamak demek      
# {:>11} burda >11 demek boşluk bırakmak demek. sağa yaslamak demek    
    print("-"*30)
function(ad="serhat",soyad="çağlar",tel="05348911500")   


# ** işaretlerinin betimlediği parametreler 'kwargs' olarak adlandırılır. 
#%% şimdi print() fonk. kendimiz isimli bir parametre ekleyelim.
def bas(*args,start=" ",**kwargs):
    for öge in args:
        print(start+öge,**kwargs)
        
bas("öge1","öge2","öge3",start="#.")
# start adında isimli bir parametre ekledik ve ögelerin başına istediğimizi getirdik.

# bas fomksiyonunun *args parametresi ile kullanıcıya istediği kadar parametre
# verme imkanı sağladık.**kgwars parametresi ise sep,end,file,flush
# parametrelerinin aynı şekilde kullanılmasını sağlıyor.
# **kgwars şeklinde bir tanımlama sayesinde print() fonksiyonunun isimli
# parametrelerini tek tek belirtmek zorunda kalmıyoruz. 

#%%                 return Deyimi
def isimNe():
    isim = input("İsmin ne :")
    print(isim)
isimNe()    

print("merhaba {} nasılsın.".format(isimNe()))    
# burada tekrardan isimNe() fonk. kullanamadık.

#%% kullanabilmemiz için return adlı deyimi kullanmalıyız.
# eğer onu kullanmazsak Python None adlı bir veriyi döndürür.
def isimNe():
    isim = input("İsmin Ne: ")
    return isim
isimNe()
# göründüğü gibi fonk. çalıştırdıkv ama sadece input() çalıştı fakar ismi 
# yazdırmadı.çünkü biz bas(print) demedik.    
print("merhaba {} nasılsın.".format(isimNe()))     
# return sayesinde isimNe() fonk. burda kullanabildik.   
#%% return sayesinde başka bir değişkene de atayabildik.
ad = isimNe()
print(ad)    
# ayriyetten Python return satırından sonra gelen hiçbir kodu okumaz.   
    
#%%     ÖRNEK UYGULAMA    
# amacımız belli aralıkta ve belli miktarda sayılar üreten program yazmak.
# ancak bir sayıdan sadece bir tane bulunacak.
import random
def sayiUret(baslangic=0,bitis=500,adet=6):# fonk. tanımladık.
    sayilar=set() # sayilar adlı küme oluşturduk.
    while len(sayilar)<adet:# sayilar kümesinin uzunluğu 6 olana kadar döngü sürer.
        sayilar.add(random.randrange(baslangic,bitis))
    return sayilar # return sayesinde dış dünyaya sayilar adlı değişken bıraktık.
# randrange() fonk. belli aralıkta rastgele sayılar üretmemizi sağlar.    
# random modülü içinde bulunur.   
    
#def sayiUret(baslangic=0,bitis=500,adet=6):# buradaki 0,500,6 değerleri 
    # varsayılan değerlerdir.
print(sayiUret())    
print(sayiUret(0,100,5))# 0-100 arasında 5 adet sayı uret dedik.   
print(*sayiUret(1,54,6),sep="-")# süper loto çekilişi yaptık :)    
    
#%%                 Fonksiyonların Kapsamı Ve Global Deyimi
isim = "serhat"
def fonk():       # fonk. bu şekilde hata verir.
    isim+="çağlar"
    return isim
fonk()
#%% 
isim = "serhat" # burası global
def fonk():     
    global isim
    isim+="çağlar" # burası lokal
    return isim
fonk()

# eğer bir nesne değiştirilebilir nesne ise onun değerini lokal isim alanlarından
# değiştirebilirsiniz.

#değiştirilemeyen bir nesne ise bunuda global deyimiyle hallediyoruz.

#%%                      --------GÖMÜLÜ FONKSİYONLAR-------
# Python tarafından tanımlanmış hizmete sunulmuş bir takım araçlardır.

#                     abs()
# bir sayının mutlak değerini bulmak için kullanılır.
print(abs(-20))
print(abs(20))
print(abs(20+3j))
#%%                 round()
# sayıyı yuvarlamamızı sağlar.
print(round(2.51))# 3'e yuvarladı. 
print(round(2.50))# 2'ye yuvarladı.
print(round(20/7,3))# 2. parametre virgülden sonra kaç basamak olmasını söyler.
#%%                  all()
# herhengi bir dizi içinde bulunan değerlerin True ya da False olduğunu söyler.

# 0 hariç bütün sayıların bool değeri True'dur.
# '' boş karakter dizisi de False'dir.İçinde hiç birşey yok.
a = 3
t1 = a ==3         # sayı 3 mü?
t2 = a % 2 ==1    # sayı tek mi?
t3 = a < 4        # sayı 4'ten küçük mü?
print(all([t1,t2,t3]))  #  sayı bu özelliklerin hepsine sahip mi? || True ||
#%%                  any()
# all() ile aynıdır farkı sadece 1 tanesi bile True ise True çıktısı verir.
a = ["serhat","serdar"," "]
print(any(a))
#%%                   ascii()
a = "ışık"
print(ascii(a))# '\u0131\u015f\u0131k' || Türkçe karakterleri UNICODE temsiline döndürdü.
liste = ["serhat","serdar","ahmet"]
temsil = ascii(liste)# listeyi karakter dizisine dönüştürür.
print(temsil)
print(type(temsil))# <class 'str'>  çıktısı verdi.
#%%                 repr()
# ascii() ile aynıdır.
print(ascii("şeker"))# '\u015feker'
print(repr("şeker"))# 'şeker'
# repr yine de bize çıktı olarak karakter karşılıklarını verir.
#%%           bool()
# bir nesnenin bool değerini verir.
print(bool(0))
print(bool(''))
print(bool(1))
print(bool("serhat"))
print(bool([]))
#%%                 bin()
# bir sayının ikili düzendeki karşılığını verir.
print(bin(33))# 0b100001 çıktısı verdi.
#%%                bytes()
print(bytes(10))# bu bize herbir ögesinin değeri 0 olan 10 baytlık veri döndürdü.
# karakter dizilerini doğrudan parametre veremeyiz hata verir.
# bayta dönüştürme işlemini hangi kod çözücü ile yapmak istediğimizi belirtmeliyiz.
print(bytes("ışık".encode("cp1254")))
print(bytes("ışık","cp1254"))# ikiside aynı.
# kodların çökmesini engellemek için errors parametresini kullan.
print(bytes("ışık",encoding="ascii",errors="replace"))
#%%              bytearray()
# baytlar değiştirilemeyen veri tipleridir.
# baytın herhengi bir ögesini başka bir değerle değiştiremeyiz.
# değiştirebilmek için bunu kullanacağız.
a = bytearray("serhat","ascii")
print(a)
a[0]=65
print(ord("S"))# 83 çıktısı.
a[0] = 83
print(a)
#%%              chr()
# bir sayının hangi karaktere karşılık geldiğini gösteren fonk.
print(chr(83))# S
# bu fonk. sayıları karaktere dönüştürürken UNICODE sistemini temel alır.
#%%               list()
a = list()
b = "serhat"
print(list(b))# karakter dizisini listeye dönüştürdük.
#%%                 set()
k = set()
print(set("serhat"))# karakter dizisini kümeye dönüştürdük.
#%%                 tuple()
print(tuple("s"))# ('s',)  çıktısı verdi.
#%%                 frozenset()
k = set("serhat")
dk = frozenset(k)
print(dk)
# dondurulmuş kümeye dönüştürür.
#%%                 complex()
# sayıyı karmaşıl sayıya dönüştürmemizi sağlar.
print(complex("33"))# sanal kısmı 0 verdi = +0j
print(complex(33,2))# sanal kısmı değiştirdik. = +2j
#%%             float()
print(float("33"))
print(float(33))
#%%             int()
print(int("33"))
print(int(11.1))
# bunu herhangi bir sayma sistemindeki sayıyı onlu sisteme de dönüştürür.
print(int("12",8))
# burda 8 li sistemdeki 12'yi 10'lu sistemdeki haline döndürdük.
print(int("4cf",16))
# burda da 16 lı sistemdekini 10 lu sisteme çevirdik.
#%%                  str()
print(str(12))
bayt = b'serhat'
karDiz = str(bayt,encoding="utf-8")
print(karDiz)
# bayt olan bir veriyi encoding ile kodlama biçimini belli ederek kar.diz. çevirdik.
#%%                dict()
s = dict()
a = (["a",1],["b",2])
print(dict(a))
#%%              callable()
# bir nesnenin çağırılabilir olup olmadığını sogular.
# fonksiyonlar çağırılabilir,değişkenler çağırılabilir değildir.
print(callable(open))# True
import sys
print(callable(sys.version_info))# False
#%%              ord()
# bir karakterin ondalık sayı karşılığını verir.
print(ord("S"))# 83
#%%              oct()
# bir sayının sekizli düzendeki karşılığını verir.
print(oct(11))# 0o13
#%%             hex()
# bir sayının onaltılı düzendeki karşılığını verir.
print(hex(11))# 0xb 

#%%            eval(),exec(),globals(),locals(),compile()
# eval() fonk. bir şeyi parametre olarak verdiğimizde hara almıyorsak o ifadedir.
# hata alıyorsak o deyimdir.
# ama exec() fonk deyimleri parametre olarak alır.
# global isim alanını gösteren sözlükte hangi anahtar,değerlerin old. görmek için yaptık.

def fonk(param1,param2):
    x = 10
    print(locals())
fonk(10,20) # {'param1': 10, 'param2': 20, 'x': 10}  çıktısı.
# locals() bize fonk. içindeki lokal değerleri verir.
#%%
a = 20
exec("a = 3")
print(a)
# exec() ile oluşturduğumuz değişkenler global isim alanı yerıne farklı bir yere gider.
#%%
a = 20
ia = {}
exec("a=3",ia)
print(a)# 20 global isim alanındaki a'ya dokunmadık.
print(ia["a"])# 3 

#%%            copright()
# Pyhton'ın telif haklarına ilişkin bilgilere erişmek için kullanılır.
print(copyright())
#%%            credits()
# Python'a katkıda bulunanlara teşekkür içeren küçük bir metin çıkarır.
print(credits())
#%%            license()
# Python lisansına ilişkin metinleri çıkartır.
print(license())
#%%             dir()
# bir nesnenin özellikleri hakkında bilgi edinme imkanı verir.
#%%              divmod()
# girdiğimiz parametrelerin bölümünü ve kalanını verir.
print(divmod(10,2))# (5,0) çıktısı.
#%%              enumerate()
# nesneleri numaralandırmamızı sağlar.
enumerate("serhat")

print(*enumerate("serhat"))

print(list(enumerate("serhat")))

for i in enumerate("serhat"):
    print(i)
# 3 şekildede enumerate nesnesinin içeriğine erişebiliriz.
for sira,oge in enumerate("serhat"):
    print("{}. {:>2}".format(sira,oge))
# bu demetin herbir ögesine bu şekilde ulaşabiliriz.
for sira,oge in enumerate("serhat",1):
    print("{}. {:>4}".format(sira,oge))
# enumerate'ye 1 parametresi ekleyerek saymaya 1'den başla diyoruz.

#%%                exit()
# o anda çalışan programdan çıkmamızı sağlar.
#%%              help()
# herhangi bir nesne hakkında bilgi almak için kullanılır.
print(help(dir))
print(help(print))
print(help(help))
#%%              id()
print(id(11)) 
print(id("S"))
#%%               input()
# kullanıcı ile alışverişte bulunmak için kullanılır.   
#%%              format()
print(format(12,".2f")) # bu format fonksiyonu
print("{:.2f}".format(12)) # bu format metodu 
#%%             filter()
# dizi niteliği taşıyan nesnelerin içindeki ögeleri süzmemizi sağlar.
l = [11,22,5,78,123,541,21,785,38,42,88,444]   
# şimdi listede ki tek sayıları süzelim.
for i in l:
    if i%2==1:
        print(i)
# ya da
print([i for i in l if i %2 ==1])
# şimdi de filter() ile yapalım
def tekSayi(sayi):
    return sayi%2==1
print(*filter(tekSayi,l))
# oluşturduğumuz fonk. görevi kendisine parametre olarak verilen sayının tek 
# olup olmadığını sorgulamak.
print(tekSayi(22))# False çıktısı verdi.     
print(tekSayi(11))# True çıktısı verdi.   
    
print(filter(tekSayi,l))# <filter object at 0x000000D0968F1D48> çıktısı verdi.  
# bu nesne içindeki ögeleri görebilmek için yapacaklarımız belli.
print(list(filter(tekSayi,l)))    
print(i for i in filter(tekSayi,l))    
#%% 
notlar = {"serhat"   :45,
          "serdar"   :60,
          "ahmet"    :90,
          "nimet"    :80,
          "ezgi"     :65}
def suz(n):
    return n >= 70
print(*filter(suz,notlar.values()))

#%%               hash()
# belli türdeki nesnelere karma deger vermemizi sağlar.
print(hash("serhat"))
#%%              isinstance()
# nesnenin hangi veri tipinde olduğunu sorgulamamızı sağlar.
print(isinstance("serhat",str))# True çıktısı.
print(isinstance("serhat",list))# False çıktısı.
#%%            len()
# nesnelerin uzunluklarını hesaplar.
print(len(["serhat",1,"serdar"]))
print(len("serhatttc"))
#%%              map()
# liste içindeki her sayının karesini almak istiyoruz.
l = [2,5,1,8,11]
for i in l:
    print(i**2)
# map() ile de yapalım.
def karesi(n):
    return n ** 2
print(list(map(karesi,l)))
#%%               max()
# dizi içindeki en büyük ya da en uzun ögeyi verir.
l = [3,5,11,9]
print(max(l))# 11
a = "serhat","serdar","abdurrezzak","murat"
print(max(a,key=len))# max kavramını hangi ölçüte göre alacağını belirledik.
#%%               min()
# max() fonk. tam tersidir.
#%%              open()
# dosyayı açmak veya oluşturmak için kullanılır.
open("dosyaAdi.txt")
# DOSYA KİPLERİ SAYFA ------580-----
# .fileno ile dosyanın tanımlayıcısını bulabilirsiniz mesela '5'
# dosyayı açarken de bu tanımlayıcı kullanabiliriz.f = open(5)
#%%               pow()
# 3 parametre alabilir.
print(pow(5,3,2))# 1 çıktısı verdi.
# bu demek 5'in küpünü al 2 ye bölümünden kalanı yaz.
#%%              print()
#print(deger1,deger2,deger3,.....,sep=' ',end="\n",file=sys.stdout,flush=False)
# bu parametreleri bulundurur.
# biz flush=True yaparsak değerler doğrudan dosyaya yazılır.
#%%               range()
# belli aralıktaki sayıları göstermek için kullanılır.
a = range(1,12,2)
print(a)
print(list(a))
print(tuple(a))
print(set(a))
print(frozenset(a))
# 3 parametre alır ilki başlangıç değeri ikinci bitiş değeri(dahil değil)
# üçüncüsü atlama değeri kaçar kaçar atlasın diyoruz.
#%%               reversed()
# nesnenin ögelerini ters cevirmek için kullanırız .
l = ["serhat","serdar","ahmet","nimet"]
print(l[::-1]) # bunu kullanabiliriz. ya da aşağıdakini.
print(list(reversed(l)))
#%%                sorted()
# dizi içindeki ögeleri belirli bir ölçüte göre dizmemizi sağlar.
print(sorted("serhat"))# alfabeye göre liste şeklinde sıraladı.
print(sorted(["serhat","ahmet","nimet","serdar"]))
# sorted fonk. ile aldığımız her çıktı liste olacaktır.
print(sorted(["izel","ışık","ahmet","serdar"]))
# bu fonk. türkçe karakter içeren ögeleri düzgün sıralayamaz.
#bu sorunu çözebilmek için locale modülün içindeki strxfrm() fonk. kullanıcaz.
isimler = ["izel","ışık","ahmet","serdar"]
import locale # modülü içe aktardık.
# şimdide yereli(locale) türkçe olarak ayarlayalım.
locale.setlocale(locale.LC_ALL,"Turkish_Turkey.1254")
# şimdi sıralama işlemini deneyelim.
print(sorted(isimler,key=locale.strxfrm))
#%%               slice()
# ögelerden oluşan nesnenin belli kısımlarını ayırmamızı sağlar.(dilimleme)
l = ["serhat","serdar","ahmet","murat","nimet"]
print(l[:2])
print(l[2:])
# l[başlangıç:bitiş:atlama değeri]
print(l[::2])
# şimdi slice() ile deneyelim.
dl = slice(0,3)# bir slice nesnesi oluşturuyoruz.
print(l[dl])# bu nesneyi liste üzerine uyguladık.
# slice(başlangıç,bitiş,atlama)
#%%                 sum()
# bir dizi içindeki değerlerin toplamını bulur.
l = [3,5,1,22,71,53,11]
print(sum(l))# 166
print(sum(l,10))# 176
# verdiğimiz 2. parametre '10' sayısı listenin toplamına eklendi.
#%%                  type()
# nesnenin hangi veri tipinde olduğunu söyler.
#%%                 zip()
a1 = ["a","b","c"]
a2 = ["d","e","f"]
# listelerin ögelerini birbiriyle eşitlemek için kullanabiliriz.
print(zip(a1,a2))# <zip object at 0x000000DEEEEC30C8> çıktısı verdi.
# bu çıktıyı düzeltmek için yani nesnenin ögelerine ulaşmak için.
print(*zip(a1,a2))
print(list(zip(a1,a2)))
print(tuple(zip(a1,a2)))
for x,y in zip(a1,a2):
    print(x,y)
#%%                vars()
# mevcut isim alanı içindeki metot,fonk. ve nitelikleri listeler.
print(vars(str))
print(vars(int))
print(vars(list))






















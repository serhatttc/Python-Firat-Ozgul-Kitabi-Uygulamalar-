# -*- coding: utf-8 -*-
#                        -----TEMEL DOSYA İŞLEMLERİ-----
#                  Dosya Oluşturmak  
f = open(r"C:\Users\hp\Desktop\Python\deneme2.txt","w")# bu şekil yerini de belirleyebiliriz.
#%%                Dosyaya Yazmak
file = open(r"C:\Users\hp\Desktop\pythonDemos\deneme2.txt","w")
file.write("Serhat Çağlar 1996 BİLECİK")
file.close()
#%%                 Dosya Okumak
#              read   
file = open(r"C:\Users\hp\Desktop\pythonDemos\deneme3.txt","r")# "r" harfini hiç koymasakta dosyayı okumak için açacak.
# okumak için 'read'-'readline'-'readlines' olarak 3 metottan yararlanıcaz.
print(file.read())# hepsini okudu.
file.close()
#%%               readline
file = open(r"C:\Users\hp\Desktop\pythonDemos\deneme3.txt","r")# "r" harfini hiç koymasakta dosyayı okumak için açacak.
# okumak için 'read'-'readline'-'readlines' olarak 3 metottan yararlanıcaz.
print(file.readline())# ilk satırı okudu.
print(file.readline())# ikinci satırı okudu
file.close()
#%%             readlines
file = open(r"C:\Users\hp\Desktop\pythonDemos\deneme3.txt")
print(file.readlines())# bu tarz okuma bize liste çıktısı verir diğerleri,
#                       karakter dizisi çıktısı verir.
file.close()
#%%                        Dosyaları Otomatik Kapatma
try:
    file = open("dosyaAdı","r")
# burada dosyada bazı işlemler yapıyoruz ve ansızın bir hata oluşuyor.
except IOError:
    print("bir hata oluştu.")
finally:
    file.close()
#%%  yukardakinin aynısın daha pratik yöntemi.   
with open("dosyaAdı","r") as file:# with kullandığımız için ne olursa olsun Python 
    print(file.read()) # bizim için dosyayı her türlü kapatır.
#%%                        Dosayayı İleri-Geri Sarmak
file = open(r"C:\Users\hp\Desktop\pythonDemos\deneme3.txt","r")
print(file.read())
print(file.read())
print(file.seek(0))# dosyanın 0. baytını oku dedik yani en başını
print(file.read())
print(file.seek(11))# dosyanın 11. baytından itibaren ou dedik.
print(file.read())
print(file.tell())# dosyanın o anda hangi bayt üzerinde olduğunu söyler.
file.close()
#%%                         Dosyalarda Değişiklik Yapmak
#             Dosyaların Sonunda Değişiklik Yapmak
#f = open("dosyaAdı","a")# dosyayı tamamen silmeden değişiklik yapmak için.'a' 
with open("deneme3.txt","a")as f:
    f.write("\nSERAP 1990\n")# son satıra ekledik.
f.close()
#%%          Dosyaların Başında Değişiklik Yapmak
with open("deneme3.txt","r+")as f:# 'r+' hem okuma hem yazma kipi demek            
    veri = f.read()
    f.seek(0)
    print(f.write("MURAT 1975\n"+veri))#listenin başına ekledik.ardından devam etti.
f.close()
#%%        Dosyaların Ortasında Değişiklik Yapmak
with open("deneme3.txt","r+")as f:
    veri = f.readlines()
    veri.insert(2,"Bilecik Merkez\n")# listenin 2. sırasına bunu ekledik demek.
    f.seek(0)
    f.writelines(veri)#dosyaya liste tipinde verileri yazma imkanı verir.'.writelines'
f.close()

#%%          ------------DOSYAYA ERİŞME KİPLERİ (SAYFA 417)------------------
#%%
#                           Dosyaların Metot ve Nitelikleri
#                .closed
print(f.closed)# dosyanın kapalı olup olmadığını sorgular.
#%%              .readable()
# dosyanın okuma yetkisine sahip olup olmadığını sorgular.
#%%              .writable()
# dosyanın yazma yetkisine sahip olup olmadığını sorgular.
#%%              .truncate()
#with open("falancaDosya","r+") as f:
   # print(f.truncate())
# kodu böyle yazarsak dosyada ki hersey silinir.
#with open("falancaDosya","r+") as f:
   # print(f.truncate(10))
# 10 poarametresini ekleyipte yazarsak dosyada sadece 10 baytlık veri bulundurur
    #   gerisini siler.
with open("deneme3.txt","r+") as f:# dosyamızı hem okuma hem yazma kipinde açtık.
    f.readline()#sonra dosyadan tek bir satır okuduk
    f.seek(f.tell())
    f.truncate(0)
f.close()
f.name
f.encoding
#%%    aynı zamanda .truncate() kullanarak dosyaların boyutunu büyütebiliriz.
f = open("falancaDosya","r+")
f.truncate(1024*3)# boyutu 1KB olan dosyayı 3KB'ye çıkardık.
f.close()
#%%               .name
#   f.name   bize dosyanın adını verir.
#%%               .encoding
#   f. encoding   bize dosyanın hangi dil kodlaması ile kodlandığını söyler.
#%%            --------------İKİLİ(BİNARY) DOSYALAR--------------
#  resim,müzik,video ve diğer dosyalar ikili dosyadır.

#         PDF dosyaları   bunlarda ikili dosyalardır.
f = open(r"C:\Users\hp\Downloads\2019-20 BAHAR PRG..pdf","rb")
print(f.read(10)) # dosyadan 10 baytlık veri okuduk.
#%%
f = open(r"C:\Users\hp\Downloads\2019-20 BAHAR PRG..pdf","rb")
okunan = f.read()
producer_index = okunan.index(b"/Producer")
print(producer_index)# bu değişken /Producer ifadesinin ilk baytının
#     dosya içindeki konumunu tutar.
print(okunan[producer_index])
print(chr(okunan[producer_index]))#yukardai sayının hangi karaktere denk geldiğini bulduk.
print(okunan[producer_index:producer_index+300])
#%%         Resim dosylarının türünü tespit etmek
#        
for f in dosyalar:
    okunan = (f,"rb").read(10)
    if okunan[6:11] in [b"JFIF",b"Exif"]:
        print("{} adlı dosya bir JPEG.".format(f))
    elif okunan[0:8] == b"\211PNG\r\n\032\n":
        print("{} adlı dosya bir PNG.".format(f))
    elif okunan[:3] == b"GIF":
        print("{} adlı dosya bir GIF.".format(f))
    elif okunan[:2] in [b"II",b"MM"]:
        print("{} adlı dosya bir TIFF.".format(f))
    elif okunan[:2] in [b"BM"]:
        print("{} adlı dosya bir BMP.".format(f))
    else:
        print("Türü bilinmeyen dosya : {}".format(f))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    








   
    
    
    
    
    
    
    
    
    
    
    
    
    
    













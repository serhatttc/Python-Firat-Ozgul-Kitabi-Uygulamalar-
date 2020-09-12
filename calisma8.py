# -*- coding: utf-8 -*-
#                      KARAKTER DİZİLERİNİ BİÇİMLEDİRMEK

#               %  İşareti İle Biçimlendirme
#                            %s
parola = input("parola : ")
print("Girdiğiniz parola (%s) kurallara uygun bir paroladır." %(parola))

print("%s ile %s iyi bir ikilidir." %("Python","Django"))
#%%
karDiz = "istihza"
for sira,karakter in enumerate(karDiz,1):
    print("%s. karakter : '%s'" %(sira,karakter))
#%%
for i in range(100):
    print("%%%s" %i)
#%%  
for i in dir(""): #  burdaki 15 biçimlendirilecek karakter dizisinin toplam kaç 
    print("%15s" %i) # karakterlik yer kaplayacağını söylüyor.
    
print("|%15s|" %"istihza")# soldan yazmaya başlar.
print("|%-15s|" %"istihza")# sağdan yazmaya başlar.
print("depoda %(miktar)s kilo %(ürün)s kaldı." %{"miktar":25,
                                                 "ürün":"elma"})
#%%                  BİÇİMLENDİRME KARAKTERLERİ
# %s karakter dizileri için kullanılır.
print("şubat ayı bu yıl %d gün çekiyor." %23) # sayılar için kullanılır.
print("%d" %13.5)# ondalık kısmını göstermez sadece tam sayı değerleri için.
sayi = input("sayı : ")
print("%d" %float(sayi))
#%%             %d , %i , %o , %x , %X , %f  kullanımları aynıdır.
print("|%7d|" %33)
print("|%-7d|" %33)
print("%(sayı)d" %{"sayı":23})
print("%06d" %22)
print("%.6d" %22)
print("%10.5d" %22)# 22 sayısının 10 boşlukluk yer kaplamasını ve 5 tanesinin
#                  içine 0 ve 22 sayısını yazmasını istedik.
print("%0010.5d" %22)# 22 sayısının toplam 10 boşluklu yer kaplamasını ve
# 10 tane boşluğa 22 sayısını yerleştirdikten sonra geri alan yerlere 0 yerleştir dedik. 
print("%i sayısının sekizlik düzende karşılığı %o" %(10,10))
# %x on altılı düzendeki karşılığını gösterir.
# %X yukardakiyle aynıdır büyük harfle gösterir.
# %f noktalı sayıları temsil etmek için kullanılır.
# %c , %s ile aynıdır.Tek bir karakteri temsil eder.
#%%                       format fonksiyonu
isim = input("isminiz : ")
print("merhaba {} nasılsın.".format(isim))
#%%
print("{0} {1}".format("Serhat","Çağlar"))# sıralarını ayarlayabiliyoruz.
print("{1} {0}".format("Serhat","Çağlar"))
print("{dil} dersleri".format(dil="Python"))
print("|{:>15}|".format("serhat"))# sağa yaslama
print("|{:<15}|".format("serhat"))# sola yaslama
print("|{:^15}|".format("serhat"))# ortalama
#%%         format ile birlikte şu harfleri kullanabiliyoruz.
#                                    s
print("{:s} ile {:s} iyi bir ikilidir.".format("python","django"))
# s ile sadece karakter dizileri kullanılır sayı değil.
#%%                         c
print("{:c}".format(65)) 
# c 0 ile 256 arası sayıların ASCII tablosundaki karşılıkları verir.
#%%                         d
print("{:d}".format(65))
# d ile sadece sayılar kullanılır.
#%%                          ,
print("{:,}".format(123456789))
# sayıyı basamaklarına ayırmak için kullanılır.
#%%                     















































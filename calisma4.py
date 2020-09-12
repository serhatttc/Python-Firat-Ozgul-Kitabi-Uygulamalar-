# -*- coding: utf-8 -*-

number = int(input("Sayı giriniz : "))

if number % 2 == 0:
    print("Sayı çifttir.")
else:
    print("Sayı tektir.")
#%%
divided = int(input("Sayı Giriniz : "))
dividing = int(input("Bir sayı daha giriniz : "))
template = "{} sayıyısı {} sayısına tam".format(divided,dividing)

if divided % dividing == 0:
    print(template,"bölünüyor.")
else:
    print(template,"bölünmüyor.")
#%%
print(round(2.50)) # sayıları yuvarlar.
print(round(2.55,1)) # noktadan sonra 1 basamak göster demek.
#%%
a = 1
print(a==1) # bool işleçleri.
print(a==3//2)
print(a==2)
#%%                # 0 değeri ve boş karakter dizileri False, diğerleri True.
print(bool(3))
print(bool(""))# false
print(bool(0)) # false
print(bool("0"))
print(bool("  "))
print(bool("serhat"))
#%%
user = input("Kullanıcı Adı : ")

if bool(user)==True:  # Bunu şu şekilde yazabiliriz -- if user: -- bu kadar.
    print("THANKS!")
else:
    print("This field cannot be left blank!")
#%%
userName = input("Kullanıcı Adı : ")
password = input("Parola : ")

if userName == "serhatttc":
    if password == "123456":
        print("Welcome!")
    else:
        print("Wrong Password or Username!")
else:
    print("Wrong Username or Password!")
#%%  # Yukardakinin aynısını and ile yazdık.
userName = input("Kullanıcı Adı : ")  
password = input("Parola : ")

if userName == "serhatttc" and password == "123456":
    print("Welcome!")
else:
    print("Wrong Password or Username!")
#%%
x = int(input("Notunuz : "))

if x>100 or x<0:
    print("Böyle bir not yok.")
elif x>=90 and x<=100:   # 90<= x <=100  böylede yazılabilir.
    print("A aldınız.")
elif x>=80 and x<=89:    # x >=80 <=89   böylede yazılabilir.
    print("B aldınız.")
elif x>=70 and x<=79:
    print("C aldınız.")
elif x>=60 and x<=69:
    print("D aldnız.")
elif x>=0 and x<=59:
    print("F aldınız.")
#%%
a = ""
print(not a)
b = 22
print(not b)
#%%
password = input("Parola : ")

if not password:
    print("Parola boş bırakılamaz.")
#%%
password = ""
print(bool(password))  # Parola boş bırakılmamış değil mi? Hayır boş bırakılmış.
print(bool(not password)) # Parola boş bırakılmış değil mi? Evet boş bırakılmış.
a = "123456"
print(bool(a))
print(bool(not a))
#%%                    DEĞER ATAMA İŞLEÇLERİ
a = 23
a = a + 5 # Bu şekilde de yazılır|| a += 5 ||
print(a)

b = 11
b = b - 5 # bu da || b -= 5 ||
print(b)

c = 40
c = c/8  # bu da || c /= 8 ||
print(c) 

d = 10
d = d * 5 # bu da || d *= 5 ||
print(d)

e = 40
e = e % 3 # 3 ile bölümden kalan demek // bu da || e %= 3 ||
print(e)

f = 11
f = f ** 2 # ** kuvvet alma demek.// bu da || f **= 2 ||
print(f)

h = 17
h = h // 4 # taban bölme demek.// bu da || h //= 4 ||
print(h)
#%%             AİTLİK İŞLEÇLERİ
a = "asdf"
print("a" in a)
print("z" in a)
#%%               KİMLİK İŞLEÇLERİ
a = 100
print(id(a))  # kimlik numarasını yazar. 

b = "serhat"
print(id(b))
#%%
a = 100
print(id(a))  # aynı kimlik numaralarını yazdı.
b = 100
print(id(b))
#%%
a = 1000      # hepsi için farklı kimlik yazdı.
print(id(a))
b = 1000
print(id(b))
print(id(1000))

print(a is 1000) # görünüşte aynı olan iki nesne aslında birbirinden farklı.
print(b is 1000)# is işleci nesnelerin kimliklerine bakıp aynı olup olma. inceler.
                # == işleci nesnelerin aynı değere sahip olup olma. inceler.
print(a == 1000)
#%%    Karakter dizilerindeki durum
a = "python"    # burda "python"u belleğe attı sonra kullandı.
print(a is "python") # True   
print(a == "python") # True
b = "python kolay ve güçlü bir dil."  # Ama burda belleğe atmadı.
print(b is "python kolay ve güçlü bir dil.") # False 
print(b == "python kolay ve güçlü bir dil.") # True

#      Python ufak nesneleri önbelleğe atar ama büyükleri atmaz.
#%%         Peki ufak ve büyük kavramlarının ölçütü nedir?
for k in range(-1000,1000):
    for v in range(-1000,1000):
        if k is v:
            print(k) # bunlar ufak olarak değerlendiriliyor.|| -5,256 ||
#%%
a = 256
print(a is 256) # true

b = 257
print(b is 257) # false

c = -5
print(c is -5) # true

d = -6
print(d is -6) # false

#%%
                 #  Hesap Makinesi
entry = """
(1) Topla
(2) Çıkar
(3) Çarp
(4) Böl
(5) Karesini hesapla
(6) Kare Kök hesapla"""
print(entry,"\n")

option1 = "(1) Topla"
option2 = "(2) Çıkar"
option3 = "(3) Çarp"
option4 = "(4) Böl"
option5 = "(5) Karesini hesapla"
option6 = "(6) Kare Kök hesapla"
print(option1,option2,option3,option4,option5,sep=" || ")

question = input("Yapmak istediğiniz işlemin numarsını giriniz : ")
q = question

if q == "1":
    number1 = int(input("Toplama için birinci sayı : "))
    number2 = int(input("Toplama için ikinci sayı : "))
    print(number1,"+",number2,"=",number1+number2)
elif q == "2":
    number3 = int(input("Çıkarma için birinci sayı : "))
    number4 = int(input("Çıkarma için ikinci sayı : "))
    print(number3,"-",number4,"=",number3-number4)















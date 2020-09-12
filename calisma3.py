# -*- coding: utf-8 -*-

print("""Programa hoşgeldiniz.Programı kullanabilmek 
için en az 13 yaşında olmalısınız.\n""")

print("Lütfen yaşınızı giriniz.")
age = input("Yaşınız\t: ")
print("Yaşınız : ",age,sep="")
#%%

number = int(input("Sayı giriniz."))
n = number

if n>10:
    print("Sayı 10'dan büyüktür.")
if n<10:
    print("Sayı 10'dan küçüktür.")
if n==10:
    print("Sayı 10'a eşittir.")
#%%
print("Hoşgeldiniz.Öncelikle sisteme giriş yapmalısınız.")
password = input("Parola : ")
p = password

if p == "123456":
    print("Hoşgeldiniz.")
if p != "123456":
    print("Parola yanlış.Tekrar deneyiniz.")
#%%
age = int(input("Yaşınız : "))

if age == 18:
    print("18 iyidir.")
elif age < 0:
    print("Siktir git.")
elif age < 18:
    print("Küçüksün.")
elif age > 18:
    print("Büyüksün.")

#%%
question = input("""Programdan çıkmak istediğinize emin misiniz?
Eğer eminseniz 'e' tuşuna basınız : """)
q = question

if q == "e":                # Art arda if bloklarında sıkıntı çıkar mesela 
    print("Güle Güle.")     # burda 'e'ye bastığımızda hem ilk if hemde else 
if q == "b":                # çalışır.Yani bunu için elif kullanılmalı.
    print("Kararsızım.")
else:
    print("Sen bilirsin.")
#%%
question = input("""Programdan çıkmak istediğinize emin misiniz?
Eğer eminseniz 'e' tuşuna basınız : """)
q = question

if q == "e":
    print("Güle Güle.")
elif q == "b":
    print("Kararsızım.")
else:
    print("Sen bilirsin.")
#%%
length = int(input("Boyunuz kaç ? "))
l = length

if l < 170:
    print("Boyunuz kısa.")
elif l < 180:
    print("Boyunuz normal.")
else:
    print("Boyunuz uzun.")
#%%
userName = input("Kulanıcı Adı : ")
password = input("Parola : ")

totalLength = len(userName)+len(password)

message = "Kullanıcı adı ve parolanız {} karakterden oluşmaktadır.\n"
print(message.format(totalLength))

if totalLength > 40:
    print("Toplam uzunluk 40 karakteri geçmemeli.")
else:
    print("Sisteme Hoşgeldiniz.")
















